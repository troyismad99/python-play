import os

# create a new path and change back to where we started
def make_at(path, dir_name):
    original_path = os.getcwd()
    os.chdir(path)
    os.mkdir(dir_name) # if this fails we do not change back
    os.chdir(original_path)

def make_atFIX(path, dir_name):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        os.mkdir(dir_name)
    except OSError as e:
        print(e)
        raise
    finally:
        # runs always
        os.chdir(original_path)
