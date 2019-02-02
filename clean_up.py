import os
import shutil

def clean_up_pycache(current_dir=None):

    if current_dir is None:
        current_dir = os.getcwd()

    for dir in os.listdir(current_dir):
        if current_dir is not None:
            dir = current_dir + os.sep + dir

        if dir.endswith('.git') or dir.endswith('.vscode') or os.path.isfile(dir):
            print('skipping {}'.format(dir))
            continue
        elif os.path.isdir(dir) and dir.endswith('__pycache__'):
            shutil.rmtree(dir)
            print('\nremoved pycache from {}\n'.format(dir))
        else:
            print('\nTraversing {}\n'.format(dir))
            clean_up_pycache(dir)
        
if __name__ == "__main__":
    clean_up_pycache()