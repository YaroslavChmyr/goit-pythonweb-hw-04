import asyncio
import logging
import os
from pathlib import Path
import shutil

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ArgumentParser:
    def __init__(self):
        self.args = {}

    def add_argument(self, name, type=str, help=""):
        self.args[name] = {"type": type, "help": help}

    def parse_args(self):
        result = {}
        for arg_name, arg_props in self.args.items():
            value = input(f"{arg_props['help']} ({arg_name}): ")
            result[arg_name] = arg_props["type"](value)
        return result

async def read_folder(source: Path, destination: Path):
    if not source.exists():
        logging.error(f"Вихідна папка {source} не існує.")
        return

    tasks = []
    for item in source.rglob("*"):
        if item.is_file():
            tasks.append(copy_file(item, destination))

    await asyncio.gather(*tasks)

async def copy_file(file_path: Path, destination: Path):
    try:
        extension = file_path.suffix.lstrip(".").lower() or "unknown"
        target_folder = destination / extension
        target_folder.mkdir(parents=True, exist_ok=True)

        target_path = target_folder / file_path.name

        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, shutil.copy2, file_path, target_path)

        logging.info(f"Файл {file_path} скопійовано у {target_path}.")
    except Exception as e:
        logging.error(f"Помилка при копіюванні {file_path}: {e}")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("source", type=str, help="Вкажіть шлях до вихідної папки")
    parser.add_argument("destination", type=str, help="Вкажіть шлях до цільової папки")

    try:
        args = parser.parse_args()
        source_folder = Path(args["source"])
        destination_folder = Path(args["destination"])

        asyncio.run(read_folder(source_folder, destination_folder))
    except ValueError as e:
        logging.error(e)
        print("Помилка: введіть коректні шляхи до папок.")


