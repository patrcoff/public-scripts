#adapted from previous cmd based script for filtering the Mayo/Sligo run on Mondays
#this is a specific script for filtering the PODfather files at Flanagan Flooring on Mondays when a manual re-upload must be performed for only the Mayo/Sligo ren
#That's as much as I can say, I don't really understand the reason why it needs to happen, I just know what needs done and how to do it lol
#This is a very basic gui version from which I generate an exe via pyinstaller to give to my manager to use after I move on to another role.
#This is a messy script just to get the job done, not a good example of best practice
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
#------------------------------------------------------------------------------
#import tkinterDnD  # Importing the tkinterDnD module
#------------------------------------------------------------------------------
from csv import *
import sys

# You have to use the tkinterDnD.Tk object for super easy initialization,
# and to be able to use the main window as a dnd widget
root = tk.Tk()
root.title("Podfather Mayo/Sligo filter.")
root.geometry('300x150')

file = "Empty"
stringvar = tk.StringVar()
stringvar.set('Drop Podfather file here!')

def myAction(string):
    global file
    if string[0] == "{":
        #print("debug")
        file = string[1:-1]
    else:
        file = string
    print(file)

def selectFile():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    #showinfo(
    #    title='Selected File',
    #    message=filename
    #)
    myAction(filename)
#def drop(event):
    # This function is called, when stuff is dropped into a widget
#    stringvar.set(event.data) #stringvar was in copied code but not sure if I need it
#    myAction(event.data)

def processFile():
    global file
    filename = file
    routes = ['CORK','COURIER','DONEGAL','DUBLIN','GALWAY','LIMERICK','MAYO/SLIGO','WATERFORD','WEXFORD','OMAGH', 'SPECIAL']#I should move this to a separate json file which Pual could then edit, so he won't have to edit source and recompile/install python even
    #print("This is a placeholder:",file)
    orders = []
    line_string = ''
    print(file[-3:])
    if file[-3:] != 'csv':
        print("You crazy fool! I won't let you!")
        sys.exit()
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
            elif row[0] != 'H' and row[0] != 'D':
                print("You crazy fool! I won't let you!")
                sys.exit()

    output = [] #new array for storing lines to be written to file
    for i in orders:
        #print(i,'\n')
        #if len(i) > 2:
        #    print(i)
        #search for mayo

        if i[0][4] == "MAYO/SLIGO": #HERE WE NEED TO ADD LOGIC FOR IF INAPPROPRIATE COMMMAS HAVE BEEN ENTERED BEFORE ROUTE - I.E. IF I[0][4] NO IN ROUTES[] THEN TELL USER!!! - actually this never happens so never mind
            #print(i)
            for line in i:#for each H and D row in # i:
                line_string = ''
                for el in line:
                    line_string = line_string + el + ',' #adds extra ',' at end of line
                line_string = line_string[:-1] # remove extra ',' at end of line from above command
                output.append(line_string)
        elif i[0][4] not in routes: #if any H entry doesn't have route in correct location (because of rogue ',') then we exit as manual investigation required.
            #NEED TO MAKE ERRORS VISIBLE IN GUI
            print("Error - either rogue comma or new Route added.\nIf new Route has been added please contact your administrator (Patrick Coffey) to update script to a new version.")
            print("Orderline: ",i[0])
            input("Press enter to exit.")
            #quit() #this doesn't work when converted to exe file???
            sys.exit() #maybe not the best way to abort in gui mode?

    with open(filename,'w') as file: #w means overwrite file
            for i in range(len(output)): #i in range (0 to lenght of array) not including last number i.e. range(10) = 0-9
                if i < len(output)-1: #if not last entry in list
                    file.writelines(output[i]+'\n') #write it with a \n
                else:
                    file.writelines(output[i])#write the last line with a \n

    print("Successfully filtered podfather file for MAYO/SLIGO run, file has been overwritten.")
    #input("Press enter to close.")
B_SelectFile = tk.Button(root, text ="Select File", command = selectFile)
B_Overwrite = tk.Button(root, text ="Overwrite!", command = processFile)
#fileSelect = tk.filedialog.askopenfilename()
#-------------------------------------------------------------------------------
#label_2 = ttk.Label(root, ondrop=drop, textvar=stringvar, padding=50, relief="solid")
#label_2.pack(fill="both", expand=True, padx=10, pady=10)
#-------------------------------------------------------------------------------
B_SelectFile.pack()
B_Overwrite.pack()

root.mainloop()
