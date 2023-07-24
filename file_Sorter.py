# File sorter by Daniel Torio
# Original script: https://github.com/smahesh29/File-Sorter/blob/master/File_sorter.py

import os, shutil, time
from colorama import init, Fore

#Dictionary of extensions for specific folders
extension_folders = {
    'Applications': ['.exe', '.msi', '.app', '.jar', '.msi', '.bat'],
    'Images': ['.png', '.jpg', '.gif', '.bmp', '.ico'],
    'Documents': ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf', '.txt'],
    'Videos': ['.mp4', '.avi', '.wmv', '.mkv'],
    'Audio': ['.mp3', '.wav', '.wma', 'flac'],
    'Compressed Files': ['.zip', '.rar', '.7z'],
    'Configuration FIles': ['.json', '.ini', '.cfg', '.yaml']
}


init()

#Makes a function to print colored text
def print_colored(text, color):
    print(color + text + Fore.RESET)

#A function to print strings with delay
def print_with_delay(text, delay=1):
    print(text)
    time.sleep(delay)

print_colored('Hello, welcome to the file sorter by Daniel Torio!', Fore.YELLOW)
time.sleep(2)

print_with_delay('''Please enter your downloads folder directory. 
For example, "C:/Users/YourUsername/Downloads". ''', delay=1)

downloads_folder = input("Please enter your Downloads directory: ")

# Create folders (if they don't exist)
for folder_name, extensions in extension_folders.items():
    folder_path = os.path.join(downloads_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# Sorting in progress message
print_with_delay('Sorting in progress...', delay=1)

# Sort files based on their extensions
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)
    if os.path.isfile(file_path):
        for folder_name, extensions in extension_folders.items():
            if os.path.splitext(filename)[1] in extensions:
                target_path = os.path.join(downloads_folder, folder_name, filename)
                shutil.move(file_path, target_path)

# Sorting done message
print_with_delay('Sorting done!', delay=1)