import os

def list_files (path) :
    """
    List all files in the specified path.

    arguments : path

    process : accepts path, uses inbuilt os, uses for loop, if 

    return : list of all files found in that path
    """
    files = []

    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            files.append(file)
        
    return files

def list_file_extensions (path) :
    """
    List all files in the specified path.

    arguments : path

    process : accepts path, uses inbuilt os, uses for loop, if 

    return : Dictionary of all file extensions that found in the current directory with their frequency.
    """
    

def main () :
    path = os.getcwd()
    for file in list_files(path):
        print(file)

if __name__ == "__main__":
    main()