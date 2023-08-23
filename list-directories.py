import os

def list_directories (path) :
    """
    List all directories in the specified path.

    arguments : path

    process : accepts path, uses inbuilt os, uses for loop, if 

    return : directories found in that path
    """
    directories = []

    for directory in os.listdir(path):
        if os.path.isdir(os.path.join(path, directory)):
            directories.append(directory)
        
    return directories

def main () :
    path = os.getcwd()
    for directory in list_directories(path):
        print(directory)

if __name__ == "__main__":
    main()