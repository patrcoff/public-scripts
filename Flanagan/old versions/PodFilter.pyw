#to do:
#preview pane? (separate processing of file and writing of file into two parts)
#gui editing of fields?
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import pgeocode
#------------------------------------------------------------------------------
#import tkinterDnD  # Importing the tkinterDnD module
#------------------------------------------------------------------------------
from csv import *
import sys
from os.path import exists

# You have to use the tkinterDnD.Tk object for super easy initialization,
# and to be able to use the main window as a dnd widget
root = tk.Tk()
root.title("Podfather Filter Application")
#root.geometry('400x200')

file = "Empty"
selected_orders = []
gb_country = pgeocode.Nominatim('gb')
ie_country = pgeocode.Nominatim('ie')
#stringvar = tk.StringVar()
#stringvar.set('Drop Podfather file here!')

def myAction(string): #this is a redundant function used when we were trying with DnD - which did not compile via pyinstaller...
    global file       #the string of the selected filename never includes the "{" symbols using the filedialog method
    if string[0] == "{": #for some reason DnD sometimes encased it in {}s, maybe it sometimes thought it was getting multiple filenames?
        #print("debug")
        file = string[1:-1]
    else:             #but we'll leave this function in just in case we can resolve the tkinterDnD compile issue...
        file = string #would have been nice if it returned a list instead of a string like
    #print(file)

def selectFile():
    filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/C:/Users/patrick.coffey/OneDrive - Flanagan Flooring/Documents/hello_world/podfather_script_general',
        filetypes=filetypes)

    myAction(filename)
    lbl2.config(text = "File selected: " + filename)
def addOrder():
    #we want to add the string in the text box to the selected_orders list
    ord = input_order.get()
    if len(ord) == 8 and ord not in selected_orders:
        selected_orders.append(ord)
        lbl3.config(text = "Orders:" + str(selected_orders))
        input_order.delete(0,'end')#1.0,tk.END
    else:
        tk.messagebox.showinfo(title="Error!",message="You entered an invalid or duplicate order number!")
def processFile():
    global file
    if not exists(file):
        tk.messagebox.showinfo(title="Error!",message="Please select an input file!")
        return None
    filename = file
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
    output = [] #new array for storing lines to be written to file

    #print(user_list)
    for order in orders: #order[0] = Header, order[1] = D ...
        if order[0][3] in selected_orders: #add the order lines specified by the user to the output
            for line in order:#for each H and D row in # i:
                line_string = ''
                for field in line:
                    if field != "hubdoc.cityflooringcentre.ipzg63nj@app.hubdoc.com" and field != "ap@sig.ie": #added logic to remove city flooring and HHI's duplicate email address
                        line_string = line_string + field + ',' #adds extra ',' at end of line
                    else:
                        tk.messagebox.showinfo(title="Please note:",message="Removed duplicate email address from order.")
                line_string = line_string[:-1] # remove extra ',' at end of line from above command
                output.append(line_string)
            #print("\nOrder",order[0][3]," added to output file.")
        #count commas and check
        elif len(order[0]) != 42:
            #print("\nOrder",order[0][3], "has: ",len(order[0])," fields; should be 42.")
            Q = "Order"+order[0][3]+"has: "+str(len(order[0]))+" fields; should be 42. Add to selected orders?"
            question = tk.messagebox.askquestion('Add Entry?', Q)
            if question == "yes":
                selected_orders.append(order[0][3])
                lbl3.config(text = "Orders:" + str(selected_orders))
                input_order.delete(0,'end')#1.0,tk.END
                for line in order:#for each H and D row in # i:
                    line_string = ''
                    for field in line:
                        if field != "hubdoc.cityflooringcentre.ipzg63nj@app.hubdoc.com" and field != "ap@sig.ie": #added logic to remove city flooring's duplicate email address
                            line_string = line_string + field + ',' #adds extra ',' at end of line
                        else:
                            #print("Removed hubdoc.cityflooringcentre.ipzg63nj@app.hubdoc.com email address!")
                            tk.messagebox.showinfo(title="Please note:",message="Removed duplicate email address from order.")
                    line_string = line_string[:-1] # remove extra ',' at end of line from above command
                    output.append(line_string)

            #print("")

        elif (gb_country.query_postal_code(order[0][17]).country_code != order[0][18]) and (ie_country.query_postal_code(order[0][17]).country_code != order[0][18]): #if country code for first postcode/countrycode don't match for either ie or gb ask and add - need to replicate for second postcode...
            Q = "\nOrder: " + order[0][3] + " Postcode: " + order[0][17] + " doesn't match country: " + order[0][18] + "\nAdd to orders?" #we will ask if we want to add to output
            question = tk.messagebox.askquestion('Add Entry?', Q)
            if question == "yes":
                for line in order:#for each H and D row in # i:
                    line_string = ''
                    for field in line:
                        line_string = line_string + field + ',' #adds extra ',' at end of line
                    line_string = line_string[:-1] # remove extra ',' at end of line from above command
                    output.append(line_string)
                selected_orders.append(order[0][3])
                lbl3.config(text = "Orders:" + str(selected_orders))
                input_order.delete(0,'end')#1.0,tk.END
        elif (gb_country.query_postal_code(order[0][27]).country_code != order[0][28]) and (ie_country.query_postal_code(order[0][27]).country_code != order[0][28]): #if country code for second postcode/countrycode don't match for either ie or gb ask and add
            Q = "\nOrder: " + order[0][3] + " Postcode: " + order[0][27] + " doesn't match country: " + order[0][28] + "\nAdd to orders?" #we will ask if we want to add to output
            #question = input("Save order to output Y/N?")
            question = tk.messagebox.askquestion('Add Entry?', Q)
            if question == "yes":
                for line in order:#for each H and D row in # i:
                    line_string = ''
                    for field in line:
                        line_string = line_string + field + ',' #adds extra ',' at end of line
                    line_string = line_string[:-1] # remove extra ',' at end of line from above command
                    output.append(line_string)
                selected_orders.append(order[0][3])
                lbl3.config(text = "Orders:" + str(selected_orders))
                input_order.delete(0,'end')#1.0,tk.END
    #ask save file filename
    out_file = fd.asksaveasfilename(
        title='Output filename:',
        initialfile=file,
        defaultextension='.csv', filetypes=[("csv file", '*.csv')])
    with open((out_file),'w') as f: #w means overwrite file
        for i in range(len(output)): #i in range (0 to lenght of array) not including last number i.e. range(10) = 0-9
            if i < len(output)-1: #if not last entry in list
                f.writelines(output[i]+'\n') #write it with a \n
            else:
                f.writelines(output[i])#write the last line without a \n
#------------------------------------------------------------------------------
def mayo():
    global file
    filename = file
    routes = ['CORK','COURIER','DONEGAL','DUBLIN','GALWAY','LIMERICK','Londonderry','MAYO/SLIGO','WATERFORD','WEXFORD','OMAGH', 'SPECIAL']#I should move this to a separate json file which Pual could then edit, so he won't have to edit source and recompile/install python even
    if exists("./routes_override.txt"):
        with open("./routes_override.txt", 'r+') as override:
            lines = override.readlines()
            if len(lines) > 1:
                tk.messagebox.showinfo(title="Error",message="Routes override file contains more than one row!")
                return None
            elif len(lines) == 1:
                for el in lines[0].split(','):
                    if el not in routes:
                        routes.append(el)
            else:#must be Empty
                tk.messagebox.showinfo(title="Info",message="Routes override file is empty!")
        #tk.messagebox.showinfo(title="Debug",message="This file exists!")
    else:
        tk.messagebox.showinfo(title="Info",message="Proceeding with default routes.")
    #add json file for editing routes post compilation
    orders = []
    line_string = ''
    #print(file[-3:])
    #tk.messagebox.showinfo(title="Please note:",message="")
    if filename[-3:] != 'csv' and filename[-3:] != 'CSV':
        #print("You crazy fool! I won't let you!")
        tk.messagebox.showinfo(title="Error!",message="Source file doesn't quite look right, not a \'csv\' file - try again!")
        #sys.exit()
        return None
    with open(filename, 'r+') as read_obj:#file opened for reading
        csv_reader = reader(read_obj)
        for row in csv_reader:
            print(row)
            #line_string = ''
            #for el in row: #this should get the row as a string
            #    line_string = line_string + el + ',' #maybe break out this logic for later? to keep in lists
            if row[0] == 'H':
                orders.append([row])
            elif row[0] == 'D':
                orders[-1].append(row) #to here, creates a list of lists of lists -> list of orders containing, list of rows (H and D(s)), each containing list of fields
            elif row[0] != 'H' and row[0] != 'D' and len(row) > 0:
                tk.messagebox.showinfo(title="Error!",message="Source file doesn't quite look right, some lines don't start with \'H\' or \'D\' - try again!")
                #sys.exit()
                return None
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
            #print("Error - either rogue comma or new Route added.\nIf new Route has been added please contact your administrator (Patrick Coffey) to update script to a new version.")
            #print("Orderline: ",i[0])
            #input("Press enter to exit.")
            #quit() #this doesn't work when converted to exe file???
            tk.messagebox.showinfo(title="Error!",message="Please check source file for errors: route not recognised: "+i[0][4])
            #sys.exit() #maybe not the best way to abort in gui mode?
            return None

    out_file = fd.asksaveasfilename(
        title='Output filename:',
        initialfile=file,
        defaultextension='.csv', filetypes=[("csv file", '*.csv')])

    with open(out_file,'w') as file: #w means overwrite file
            for i in range(len(output)): #i in range (0 to lenght of array) not including last number i.e. range(10) = 0-9
                if i < len(output)-1: #if not last entry in list
                    file.writelines(output[i]+'\n') #write it with a \n
                else:
                    file.writelines(output[i])#write the last line with a \n

    #print("Successfully filtered podfather file for MAYO/SLIGO run, file has been overwritten.")
    tk.messagebox.showinfo(title="Success!",message="Successfully filter Mayo/Sligo entries.")
#------------------------------------------------------------------------------
def order_enter(event):
    addOrder()
    input_order.delete(0,'end')#1.0,tk.END
def clear_orders():
    input_order.delete(0,'end')#1.0,tk.END
    global selected_orders
    selected_orders = []
    lbl3.config(text = "Orders:" + str(selected_orders))
    #input_order.delete(0,'end')#1.0,tk.END
#------------------------------------------------------------------------------

order_fr = tk.Frame(root)
lbl1 = ttk.Label(root,text="Enter order numbers to extract:\n(One at a time)")#,width=80)
input_order = tk.Entry(root)
input_order.bind('<Return>',order_enter)
B_SelectFile = ttk.Button(root, text ="Select File", command = selectFile)
B_SaveFile = ttk.Button(root, text ="Extract Selected Orders", command = processFile)
B_Mayo = ttk.Button(root, text ="Extract Mayo/Sligo Runs", command = mayo)
B_AddOrder = ttk.Button(root, text ="Add Order No.", command = addOrder)
B_ClearOrder = ttk.Button(root, text ="Clear Orders", command = clear_orders)
lbl2 = ttk.Label(root,text="File selected:")
lbl3 = ttk.Label(root,text=str("Orders:"))
#fileSelect = tk.filedialog.askopenfilename()
#-------------------------------------------------------------------------------
#label_2 = ttk.Label(root, ondrop=drop, textvar=stringvar, padding=50, relief="solid")
#label_2.pack(fill="both", expand=True, padx=10, pady=10)
#-------------------------------------------------------------------------------

#,padx=10,pady=10
separator = tk.Canvas(root)
B_SelectFile.grid(columnspan=3,row=0,padx=10,pady=10)
lbl2.grid(columnspan=3,row=2,padx=10,pady=10)
separator.grid(row=2,column=1,rowspan=9)
separator.create_line(200,0,200,1500, fill="red", width=5)
#row 3 add labels for the two workflows
lbl_wf_left = tk.Label(root,text="General filtering:")
lbl_wf_right = tk.Label(root,text="Mayo/Sligo extract:")
lbl_wf_left.grid(row=3,column=0,sticky=tk.W,columnspan=1)
lbl_wf_right.grid(row=3,column=2,sticky=tk.E,columnspan=1)
lbl1.grid(column=0,row=4,padx=10,pady=10,sticky=tk.W,columnspan=1)
#order_fr.grid(column=0,row=5,padx=10,pady=10,sticky=tk.W,columnspan=1)
input_order.grid(column=0,row=5,padx=10,pady=10,sticky=tk.W,columnspan=1)
B_AddOrder.grid(column=0,row=6,padx=10,pady=10,sticky=tk.W,columnspan=1)
lbl3.grid(column=0,row=7,padx=10,pady=10,sticky=tk.W,columnspan=1)
B_ClearOrder.grid(column=0,row=8,padx=10,pady=10,sticky=tk.W,columnspan=1)
B_SaveFile.grid(column=0,row=9,padx=10,pady=10,sticky=tk.W,columnspan=1)
lbl_routes = tk.Label(root,justify=tk.RIGHT,text="To override routes:\n\nEnter additional routes as comma-separated\nstrings, into file: \'routes_override.txt\' \nlocated in same directory as exe file.")
B_Mayo.grid(column=2,row=4,padx=10,pady=10,sticky=tk.E,columnspan=1)
lbl_routes.grid(column=2,row=9,padx=10,pady=10)

root.mainloop()
