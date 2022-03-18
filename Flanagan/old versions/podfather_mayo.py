from csv import *
import glob
import sys

#read lines in podfather file, extract H and D lines, filter Mayo and output file
filename = ""
filenames = glob.glob('./*.csv')
flanagans = []
routes = ['CORK','COURIER','DONEGAL','DUBLIN','GALWAY','LIMERICK','MAYO/SLIGO','WATERFORD','WEXFORD','OMAGH', 'SPECIAL']
#get all csv filenames in current dir and act if only one matches - CONTAINS "FLANAGAN"
for name in filenames:
    if 'FLANAGAN' in name:
        print('Found -  ',name)
        flanagans.append(name.split('\\')[1]) #strips the 'dir\' part of the filename output from glob
if len(flanagans) > 1 :
    print("Too many possible matching files\n")
    input("Please re-run this script with ONLY ONE podfather .csv file in the same directory.\nPress Enter to close.")

elif len(flanagans) == 1: #the correct number of matching files (1):
    print("processing task")
    filename = flanagans[0]
    #---------------------------------------------------------------------------
    orders = []
    line_string = ''
    with open(filename, 'r+') as read_obj:#file opened for reading
        csv_reader = reader(read_obj)

        for row in csv_reader:
            #line_string = ''
            #for el in row: #this should get the row as a string
            #    line_string = line_string + el + ',' #maybe break out this logic for later? to keep in lists
            if row[0] == 'H':
                orders.append([row])
            elif row[0] == 'D':
                orders[-1].append(row) #to here, creates a list of lists of lists -> list of orders containing, list of rows (H and D(s)), each containing list of fields
            #print(row)
    #file is now closed - it has been read!
    print("File" ,filename,"will be overwritten!")
    execute = input("Continue? Y/N:")
    if execute == "Y" or execute == "y":
        output = [] #new array for storing lines to be written to file
        for i in orders:
            #print(i,'\n')
            #if len(i) > 2:
            #    print(i)
            #search for mayo

            if i[0][4] == "MAYO/SLIGO": #HERE WE NEED TO ADD LOGIC FOR IF INAPPROPRIATE COMMMAS HAVE BEEN ENTERED BEFORE ROUTE - I.E. IF I[0][4] NO IN ROUTES[] THEN TELL USER!!!
                #print(i)
                for line in i:#for each H and D row in # i:
                    line_string = ''
                    for el in line:
                        line_string = line_string + el + ',' #adds extra ',' at end of line
                    line_string = line_string[:-1] # remove extra ',' at end of line from above command
                    output.append(line_string)
            elif i[0][4] not in routes: #if any H entry doesn't have route in correct location (because of rogue ',') then we exit as manual investigation required.
                print("Error - either rogue comma or new Route added.\nIf new Route has been added please contact your administrator (Patrick Coffey) to update script to a new version.")
                print("Orderline: ",i[0])
                input("Press enter to exit.")
                #quit() #this doesn't work when converted to exe file???
                sys.exit()
                #NEED TO EXIT HERE

        #now write file

        with open(filename,'w') as file: #w means overwrite file
            for i in range(len(output)): #i in range (0 to lenght of array) not including last number i.e. range(10) = 0-9
                if i < len(output)-1: #if not last entry in list
                    file.writelines(output[i]+'\n') #write it with a \n
                else:
                    file.writelines(output[i])#write the last line with a \n

        print("Successfully filtered podfather file for MAYO/SLIGO run, file has been overwritten.")
        input("Press enter to close.")
        #---------------------------------------------------------------------------


    elif execute == "N" or execute == "n":
        print("Aborting...")
        input("Press enter to close.")
    else:
        print("Incorrect response!")
        input("Press enter to close, then try again if you are capable...")

else: #handle no file found error
    print("File not found...")
    input("Please re-run this script with an appropriate podfather .csv file in the same directory (must contain \"FLANAGAN\" in filename). \nPress Enter to close. ")
