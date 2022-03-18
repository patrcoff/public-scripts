
from csv import *
import glob
import sys
import pgeocode

#read lines in podfather file, extract H and D lines, filter Mayo and output file
gb_country = pgeocode.Nominatim('gb')
ie_country = pgeocode.Nominatim('ie')
filename = ""
filenames = glob.glob('./*.csv')
flanagans = []
routes = ['CORK','COURIER','DONEGAL','DUBLIN','GALWAY','LIMERICK','MAYO/SLIGO','WATERFORD','WEXFORD','OMAGH']
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
                orders.append([row]) #append orders with new list entry of: list containing row
            elif row[0] == 'D':
                orders[-1].append(row) #to here, creates a list of lists of lists -> list of orders containing, list of rows (H and D(s)), each containing list of fields
            #print(row)
    #file is now closed - it has been read!
    print("File" ,filename,"will be used. Output file will be prefaced by \'output_\'")
    execute = input("Continue? Y/N:")
    if execute == "Y" or execute == "y":

        #algorytgm for general script to replace sligo/mayo script HERE

        #1. ask user what lines didn't work? or possibly just validate lines (as podfather itself does) and retain problem lines
        #2. test common problem  cases
            #a) line has incorrect number of commas (could we find where the wrong comma is? or at least test the address lines)
            #b) country code does not match postcode
            #c)

        #END OF SCRIPT
        output = [] #new array for storing lines to be written to file
        print("\n")
        user_list = []
        user_list_string = input("Please enter order numbers to output to new file separated by commas with no spaces:")
        print("\n")
        for i in user_list_string.split(','):
            user_list.append(i) #this is the list of order numbers we will want to immediately add to output list

        #print(user_list)
        for order in orders: #order[0] = Header, order[1] = D ...
            if order[0][3] in user_list: #add the order lines specified by the user to the output
                for line in order:#for each H and D row in # i:
                    line_string = ''
                    for field in line:
                        if field != "redacted@email.com" and field != "redacted@email.ie": #added logic to remove [REDACTED] duplicate email address
                            line_string = line_string + field + ',' #adds extra ',' at end of line
                    line_string = line_string[:-1] # remove extra ',' at end of line from above command
                    output.append(line_string)
                print("\nOrder",order[0][3]," added to output file.")
            #count commas and check
            elif len(order[0]) != 42:
                print("\nOrder",order[0][3], "has: ",len(order[0])," fields; should be 42.")
                question = input("Save order to output Y/N?")
                if question == "Y" or question == "y":
                    for line in order:#for each H and D row in # i:
                        line_string = ''
                        for field in line:
                            if field != "redacted@email.com" and field != "redacted@email.ie": #added logic to remove [REDACTED]] duplicate email address
                                line_string = line_string + field + ',' #adds extra ',' at end of line
                            else:
                                print("Removed [REDACTED] email address!")
                        line_string = line_string[:-1] # remove extra ',' at end of line from above command
                        output.append(line_string)
                #print("")

            elif (gb_country.query_postal_code(order[0][17]).country_code != order[0][18]) and (ie_country.query_postal_code(order[0][17]).country_code != order[0][18]): #if country code for first postcode/countrycode don't match for either ie or gb ask and add - need to replicate for second postcode...
                print("\nOrder: ", order[0][3]," Postcode: ", order[0][17], " doesn't match country: ", order[0][18]) #we will ask if we want to add to output
                question = input("Save order to output Y/N?")
                if question == "Y" or question == "y":
                    for line in order:#for each H and D row in # i:
                        line_string = ''
                        for field in line:
                            line_string = line_string + field + ',' #adds extra ',' at end of line
                        line_string = line_string[:-1] # remove extra ',' at end of line from above command
                        output.append(line_string)
            elif (gb_country.query_postal_code(order[0][27]).country_code != order[0][28]) and (ie_country.query_postal_code(order[0][27]).country_code != order[0][28]): #if country code for second postcode/countrycode don't match for either ie or gb ask and add
                print("\nOrder: ", order[0][3]," Postcode: ", order[0][27], " doesn't match country: ", order[0][28]) #we will ask if we want to add to output
                question = input("Save order to output Y/N?")
                if question == "Y" or question == "y":
                    for line in order:#for each H and D row in # i:
                        line_string = ''
                        for field in line:
                            line_string = line_string + field + ',' #adds extra ',' at end of line
                        line_string = line_string[:-1] # remove extra ',' at end of line from above command
                        output.append(line_string)


        #for reference - sligo/mayo script below
        """
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
        """
        #now write file
        #for i in output:
        #    print(i,"\n")

        with open(("output_"+filename),'w') as file: #w means overwrite file
            for i in range(len(output)): #i in range (0 to lenght of array) not including last number i.e. range(10) = 0-9
                if i < len(output)-1: #if not last entry in list
                    file.writelines(output[i]+'\n') #write it with a \n
                else:
                    file.writelines(output[i])#write the last line with a \n

        print("\n\nSuccessfully filtered selected records into output_",filename,"\nPlease check this file for manual fixes required before saving in podfather directory. Then move all csv files from directory script runs in.")
        input("\nPress enter to close.")
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




"""
1A Wolfe Tone Rd, Dungarvan, Co. Waterford, X35 DE62, Ireland - post codes X35 not recognised by pgeocode!!!
I contacted the maintainer of this module and they rectified the issue!



"""
