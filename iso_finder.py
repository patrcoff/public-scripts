#script to find .iso files on hard drive
import glob

ext = input("Please enter file extension to search for (default is \'.iso\'):") or '.iso'
path = input("Please enter root directory to search (default is \'C:\\')") or 'C:\\'
print(path)
files = glob.glob(path + "/**/*" + ext, recursive = True)

for ext in files:
    print(ext,'\n')

input("Press Enter to exit.")
