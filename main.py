import os
import shutil
from datetime import datetime, timedelta

def move_files_to_yesterday_folder(source_folder, destination_base_folder):
    # Get yesterday's date
    yesterday = datetime.now() - timedelta(days=1)
    year_folder = yesterday.strftime('%Y')
    date_folder = yesterday.strftime('%Y-%m-%d')

    # Construct the full path for the destination folder
    destination_folder = os.path.join(destination_base_folder, year_folder, date_folder)

    # Create the destination folders if they don't exist
    os.makedirs(destination_folder, exist_ok=True)

    # Move all files and folders from the source folder to the destination folder
    for item in os.listdir(source_folder):
        source_item = os.path.join(source_folder, item)
        destination_item = os.path.join(destination_folder, item)
        if os.path.isdir(source_item):
            shutil.move(source_item, destination_item)
        else:
            shutil.move(source_item, destination_folder)

    print(f"All contents of {source_folder} have been moved to {destination_folder}")

source_folder = os.getenv('SOURCE_DIR')
destination_base_folder = os.getenv('ARCHIVE_DIR')

move_files_to_yesterday_folder(source_folder, destination_base_folder)
