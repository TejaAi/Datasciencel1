import os
import sys
import logging
from pathlib import Path


logging.basicConfig(level=logging.INFO, format='[%(asctime)s : %(message)s]')

project_name = "datasciencel1"

list_of_files = [
    '.github/workflow/.git',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/compounds/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/entity/entity_config.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/constant/__init__.py',
    'config/config.yaml',
    'schema.yaml',
    'params.yaml',
    'app.py',
    'setup.py',
    'research/trail.ipynb',
    'templates/index.html'
]


for filepath in list_of_files:
    filedir,filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"file path created :{filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
    else:
        logging.info(f"file is created file name is :{filename}")

