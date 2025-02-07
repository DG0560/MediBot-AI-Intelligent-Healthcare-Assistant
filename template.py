import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Corrected list with commas between items
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trails.ipynb"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir, filename = os.path.split(file_path)

    # Create the directory if it is not empty
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for the file: {filename}")

    # Create the file if it does not exist or is empty
    if (not file_path.exists()) or (os.path.getsize(file_path) == 0):
        with open(file_path, "w") as f:
            pass
        logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{filename} already exists")
