import os
from datetime import datetime

FILE_PATH = r'C:\path\to\file.txt' 

# Get file size 
size = os.path.getsize(FILE_PATH)

# Get creation timestamp
create_time = datetime.fromtimestamp(os.path.getctime(FILE_PATH))

# Get last modified timestamp
modified_time = datetime.fromtimestamp(os.path.getmtime(FILE_PATH))

# Get MFT entry 
from ntfsutils.mft import MFTEntry
mft = MFTEntry.from_path(FILE_PATH)

# Print some key metadata
print("File:", FILE_PATH)
print("Size:", size)
print("Created:", create_time) 
print("Modified:", modified_time)
print("MFT Record Number:", mft.record_num)
print("Attributes:", mft.attributes)