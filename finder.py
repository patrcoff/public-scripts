import os
string1 = input("Please enter string to search for in files: ")
dir = input("Please enter directory to search \(in linux notation\): ")
found = []
with os.scandir(dir) as entries:
    for entry in entries:
        try:    

#add different file types beyond natively openable types
#this can only manage plain text files atm, annoying, but to handle more would need to import relevant modules, appropriates parse content and search, i.e. excel files - loop through sheets, then rows etc etc

            state = 0
            with open(entry, 'r') as f:
                for line in f:
                    if string1 in line:
                        state = 1        
            if state == 1:
                found.append(entry)
                
        except:
            print("Errors not yet handled. Most likely unsupported file or directory. Failed on: ",entry)
print("Search string found in files: ", found)