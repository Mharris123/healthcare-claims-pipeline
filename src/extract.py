import os
import zipfile

from datetime import datetime

zipped_path = 'data/zipped'
# Create subfolder in extracted with today's date in yyyymm format
subfolder = datetime.now().strftime('%Y%m')
unzipped_path = os.path.join('data', 'extracted', subfolder)

# Ensure the subfolder exists
os.makedirs(unzipped_path, exist_ok=True)

# Handles unzipping data files to the extracted directory
def extract_data(zipped_path, unzipped_path):
    for item in os.listdir(zipped_path):
        if item.endswith('.zip'):
            file_path = os.path.join(zipped_path, item)
            print(f'Extracting {file_path} to {unzipped_path}')
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(unzipped_path)
    

extract_data(zipped_path, unzipped_path)

