import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "python_project_template"

list_of_files = [
    "artifacts/data/.gitkeep",
    "artifacts/dataset/.gitkeep",
    "artifacts/models/.gitkeep",
    "artifacts/results/.gitkeep",
    
    "db/.gitkeep",
    
    "notebooks/trials.ipynb",
    "templates/index.html",
    
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    
    "setup.py",
    "main.py",
    "app.py",
    
    "config.yaml",    
    "params.yaml",
    "dvc.yaml",
    ".env.local",
    "requirements.txt",
]


for filepath in list_of_files:
    filepath = Path(filepath) #to solve the windows path issue
    filedir, filename = os.path.split(filepath) # to handle the project_name folder


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")