import os.path
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

root = tk.Tk()
root.withdraw()

global fileA, FileW
fileA = filedialog.askdirectory()
fileW = open("fileW.txt","w")

def countCharacters(test_str, char):
    count = 0
    for i in test_str: 
        if i == char: 
            count = count+1
    return count


def getFolderSize(file):
    total_size = os.path.getsize(file)
    for item in os.listdir(file):
        itempath = os.path.join(file, item)
        if os.path.isfile(itempath):
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            y = itempath
            if countCharacters(str(itempath), "\\") - 1 == countCharacters(str(fileA), "\\"):
            	x = getFolderSize(itempath)
            	total_size += x
            	z = y[str(y).rfind("\\")+1:]
            	fileW.write("%s : %.2f MB\n" %(z, x/1025/1000))

            else: 
            	x = getFolderSize(itempath)
            	total_size += x
    return total_size

fileW.write("Size: " + str(getFolderSize(fileA)/1025/1000) + "MB")
fileW.close()



