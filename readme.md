# Async File Sorter


## Usage
1. Open a terminal and navigate to the directory containing the script.
2. Run the script using Python:

   ```bash
   python async_file_sorter.py
   ```
3. Enter the required paths when prompted:
   - **Source folder:** The directory containing the files to be organized.
   - **Destination folder:** The directory where the organized files will be placed.

4. The script will begin sorting files and provide updates in the terminal.

---

## Example
### Input
- **Source Folder:**
  ```
  source-folder/
  ├── test.txt
  ├── test2.txt
  ├── cat.jpg
  ├── nested_folder/
      └── test3.txt
  ```

### Output
- **Destination Folder:**
  ```
  destination/
  ├── txt/
  │   ├── test.txt
  │   └── test1.txt
  │   └── test2.txt
  ├── jpg/
  │   └── cat.jpg
  ```

---


