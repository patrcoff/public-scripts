#import time
#start = time.time()
#simple script for paul to replace a problem piece of data in this file which broke his sql script
#converted to exe via pyinstaller

try:
    text = open("F:\\File_Data\\QV.OEINVHEAD.asc", "r")
    text = ''.join([i for i in text]).replace("P:maple lake Ref: Given.   aqua tile ref: McCausland/S:1235751 / 1235751", "Maple lake Ref:Given. Aqua tile Ref:McCausland")
    x = open("F:\\File_Data\\QV.OEINVHEAD.asc","w")
    x.writelines(text)
    x.close()
except:
    print("Error: Either unable to open file or search string not found!")
    input("Press enter to close.")

#-----------------------------------------------------------------------------

try:
    text = open("F:\\File_Data\\QV.OEINVLINE.asc", "r")
    text = ''.join([i for i in text]).replace("P:maple lake Ref: Given.   aqua tile ref: McCausland/S:1235751 / 1235751", "Maple lake Ref:Given. Aqua tile Ref:McCausland")
    x = open("F:\\File_Data\\QV.OEINVLINE.asc ","w")
    x.writelines(text)
    x.close()
except:
    print("Error: Either unable to open file or search string not found!")
    input("Press enter to close.")




#print(time.time()-start)
#F:\File_Data\
#QV.OEINVLINE.asc
