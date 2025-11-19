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
ls=os.listdir()
files=[]
folder=[]
for items in ls:
    if os.path.isfile(os.path.join(os.getcwd(),items)):
        files.append(items)
    else:
        folder.append(items)

print("Files",*(a for a in files),sep='''
   |___''')
print("Folders",*(a for a in folder),sep='''
   |___''')