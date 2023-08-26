import os

def get_root_directories():
  for root, directories, files in os.walk("/"):
    if not directories and not files:
      yield root

if __name__ == "__main__":
  for root in get_root_directories():
    print(root)