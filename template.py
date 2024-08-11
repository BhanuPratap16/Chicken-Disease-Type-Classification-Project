# Instead of creating all folders and files manually, I can create them using this template file to save a lot of time.
import os 
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name= "cnn-Pokemon-Type-Classifier"
 
list_of_files= [ 
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
    
]## We need this during deployment of our project, here we ll be writing all CI/CD commands



for filepath in list_of_files:
    filepath=Path(filepath) # Windows use \ but we used / so, we need to convert into windows compatible
    filedirectory,filename=os.path.split(filepath)
    #path="config/config2/init.py"
    # >>> Path(path)
    # WindowsPath('config/config2/init.py')
    # >>> import os
    # >>> os.path.split(path)
    # ('config/config2', 'init.py')
    
    if filedirectory!="":
        os.makedirs(filedirectory,exist_ok=True) #if already exists,then don`t create it on exist_ok=True,else Replace it.
        logging.info(f"Creating directory: {filedirectory} for the file:{filename}")
        
        
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating file: {filepath}")
            
    else:
        logging.info(f"{filepath} already exists")
    
    