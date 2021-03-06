#to do:
#add clear button for orders field (so you can perform action on another file without closing and reoping)
#fix layout into columns frames etc
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

# You have to use the tkinterDnD.Tk object for super easy initialization,
# and to be able to use the main window as a dnd widget
root = tk.Tk()
root.title("Podfather Mayo/Sligo filter.")
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
    #save file
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
lbl1 = ttk.Label(root,text="Enter order number to filter:",width=30)
input_order = tk.Entry(root)
input_order.bind('<Return>',order_enter)
B_SelectFile = ttk.Button(root, text ="Select File", command = selectFile)
B_SaveFile = ttk.Button(root, text ="Filter", command = processFile)
B_AddOrder = ttk.Button(root, text ="Add Order No.", command = addOrder)
B_ClearOrder = ttk.Button(root, text ="Clear Orders", command = clear_orders)
lbl2 = ttk.Label(root,text="File selected:")
lbl3 = ttk.Label(root,text=str("Orders:"))
#fileSelect = tk.filedialog.askopenfilename()
#-------------------------------------------------------------------------------
#label_2 = ttk.Label(root, ondrop=drop, textvar=stringvar, padding=50, relief="solid")
#label_2.pack(fill="both", expand=True, padx=10, pady=10)
#-------------------------------------------------------------------------------

B_SelectFile.pack()
lbl2.pack()
lbl1.pack()
input_order.pack()
B_AddOrder.pack()
lbl3.pack()
B_ClearOrder.pack()
B_SaveFile.pack()
root.mainloop()
