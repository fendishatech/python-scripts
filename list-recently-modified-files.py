import os
import datetime

def list_recent_files (path) :
    """
    List all files in the current path that has been modified in the past 24 hours.

    arguments : path

    process : accepts path, uses inbuilt os, uses for loop, if 

    return : list of recent_files found in that path
    """
    recent_files = []

    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path) :
            modified_time = os.path.getmtime(file_path)
            time_difference = datetime.datetime.now() - datetime.timedelta(hours =24)
            if modified_time > time_difference.timestamp():
                recent_files.append(file)
        
    return recent_files

def main () :
    path = os.getcwd()
    for file in list_recent_files(path):
        print(file)

if __name__ == "__main__":
    main()