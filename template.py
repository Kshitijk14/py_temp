import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "py_project_template"

list_of_files = [
    "artifacts/data/.gitkeep",
    "artifacts/data_sources/.gitkeep",
    "artifacts/models/.gitkeep",
    "artifacts/results/.gitkeep",    
    "db/.gitkeep",
    
    "notebooks/trials.ipynb",
    
    "utils/__init__.py",
    "utils/common.py",
    "utils/config.py",
    "utils/logger.py",
    "utils/ingestion.py",
    "utils/preprocessing.py",
    "utils/training.py",
    "utils/evaluation.py",
    
    "data_ingestion_pipeline/__init__.py",
    "data_ingestion_pipeline/stage_01_create_sources.py",
    
    "data_preprocessing_pipeline/__init__.py",
    "data_preprocessing_pipeline/stage_01_populate_db.py",
    
    "training_pipeline/__init__.py",
    "training_pipeline/stage_01_create_base_model.py",
    
    "evaluation_pipeline/__init__.py",
    "evaluation_pipeline/stage_01_evaluate_model.py",
    
    "main.py",
    "app.py",
    "test.py",
    "evaluate.py",
    
    "params.yaml",
    "dvc.yaml",
    ".env.local",
    ".env.example",
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