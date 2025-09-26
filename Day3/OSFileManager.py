"""
5) OS File Manager
   - Ask user for a directory path.
   - Automatically:
        - Create a folder "backup" inside it if not exists.
        - Copy all .txt files into "backup".
        - Print summary: how many files copied.
   - If directory invalid, retry until correct.
"""

import os
import shutil


def os_file_manager():
    while True:
        dir_path=input("Enter a directory path:").strip()
        if not os.path.isdir(dir_path):
            print("Invalid directory! Please enter a valid path.")
        else:
            break
        
    backup_folder=os.path.join(dir_path,"backup")
    os.makedirs(backup_folder,exist_ok=True)
    
    txt_files=[f for f in os.listdir(dir_path) if f.endswith(".txt")]
    count=0
    
    for file in txt_files:
        src_path=os.path.join(dir_path,file)
        dest_path=os.path.join(backup_folder,file)
        shutil.copy2(src_path,dest_path)
        count+=1
    
    print(f"Backup completed! {count} .txt file(s) copied to '{backup_folder}'.")