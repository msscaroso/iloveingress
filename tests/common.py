import os

def load_file_from_resources(filename):
    path = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(path, "resources", filename)
    return open(file).read()
