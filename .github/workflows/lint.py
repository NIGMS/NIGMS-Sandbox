import os
import shutil
import nbformat
from nbformat.v4 import new_notebook

def clean_notebook(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)

    # Clean cells
    for cell in notebook.cells:
        if 'outputs' in cell:
            cell['outputs'] = []
        if 'execution_count' in cell:
            cell['execution_count'] = None
        if 'metadata' in cell:
            cell['metadata'] = {}

    # Clean notebook metadata
    if 'metadata' in notebook:
        notebook['metadata'] = {}

    with open(file_path, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)

def delete_checkpoints_dirs(root_dir):
    # Walk through the directory tree
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for dirname in dirnames:
            # Check if the directory name is 'checkpoints'
            if dirname == '.ipynb_checkpoints':
                # Construct the full path to the directory
                dir_to_delete = os.path.join(dirpath, dirname)
                # Delete the directory
                shutil.rmtree(dir_to_delete)
                print(f'Deleted {dir_to_delete}')
                print('Consider adding .ipynb_checkpoints to your .gitignore file!')


if __name__ == "__main__":
    # Change this to the directory containing your notebooks
    notebook_dir = '../../'

    for root, dirs, files in os.walk(notebook_dir):
        for file in files:
            if file.endswith('.ipynb'):
                file_path = os.path.join(root, file)
                clean_notebook(file_path)
                print(f'Cleaned {file_path}')

    # Delete all 'checkpoints' directories
    delete_checkpoints_dirs(notebook_dir)

