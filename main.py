import os
import time

dir=input("Enter directory for scan : ")
if os.path.exists(dir):
    os.chdir(dir)
    print(f"Scanning in {os.getcwd()}")
    time.sleep(2)
else:
    print("Invalid directory ! Try again")
    exit()

def recursive_folders(path, indent, f):
    try:
        items = os.listdir(path)
    except PermissionError:
        print(" " * indent + "|___[Permission Denied]")
        f.write(" " * indent + "|___[Permission Denied]\n")
        return
    
    for item in items:
        if item.startswith('.'):
            continue
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            print(" " * indent + f"|___{item}")
            f.write(" " * indent + f"|___{item}\n")
        
        else:
            # Folder
            print(" " * indent + item)
            f.write(" " * indent + item + "\n")

            recursive_folders(full_path, indent + 4, f)

with open("C:\Python learning\Learning_Os\output.txt", "w", encoding="utf-8") as f:
    recursive_folders(dir, 0, f)
