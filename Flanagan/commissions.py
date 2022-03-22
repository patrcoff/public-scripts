#to do:
#create simple gui for users to feel more secure with than cmd (lol)
#allow user to input month/year for query
#create query generating function based on user entry
#finish accounting for source variances
import pandas as pd
from tkinter import filedialog as fd

def generate_dates(year,month):
    Lyear = int(year)-1

    date = str(year)+"-"+str(month)+"-"+"01"
    Ldate = str(Lyear)+"-"+str(month)+"-"+"01"

    datesThisYear = []
    for i in range(12):
        datesThisYear.append(str(year)+"-"+str(i+1).zfill(2)+"-"+"01")

    datesLastYear = []
    for i in range(12):
        datesLastYear.append(str(Lyear)+"-"+str(i+1).zfill(2)+"-"+"01")


    #print(datesThisYear)
    datesListThisYear = []
    for i in datesThisYear:
        if date >= i:
            datesListThisYear.append(i)

    datesListLastYear = []
    for i in datesLastYear:
        if Ldate >= i:
            datesListLastYear.append(i)

    #print(datesListThisYear)
    return date,Ldate,datesListThisYear,datesListLastYear

def monthWord(month_num):
    if month_num == "01":
        return "January"
    elif month_num == "02":
        return "February"
    elif month_num == "03":
        return "March"
    elif month_num == "04":
        return "April"
    elif month_num == "05":
        return "May"
    elif month_num == "06":
        return "June"
    elif month_num == "07":
        return "July"
    elif month_num == "08":
        return "August"
    elif month_num == "09":
        return "September"
    elif month_num == "10":
        return "October"
    elif month_num == "11":
        return "November"
    elif month_num == "12":
        return "December"


pd.set_option("display.max_rows", None, "display.max_columns", None)


file = fd.askopenfilename(title='Open a file',initialdir='/C:/Users/patrick.coffey/OneDrive - Flanagan Flooring/Documents/')
#ask user for month and year
month = "02"
year = "2022"
Lyear = str(int(year)-1)
date, Ldate, YTD, LYTD = generate_dates(year,month)
print(YTD)
print("\n-------------------\n")
print(LYTD)
month_year1 = monthWord(month) + " " + year
month_year2 = monthWord(month) + " " + Lyear
try:#haven't fully accounted for all variances between the sheet names and headers yet but rest of code works well so far
    new = pd.read_excel(file,sheet_name="New Customer List")
    #query = "`Inv Date` == [\""+date+"\"]"
    #query2 = "`Inv Date` == [\""+Ldate+"\"]"
    #---------------------------------------
    #query3 = "`Inv Date` == [\"2022-02-01\"] or `Inv Date` == [\"2022-01-01\"]"
    #query4 = "`Inv Date` == [\"2021-02-01\"] or `Inv Date` == [\"2021-01-01\"]"
    #query3 = ""
    #for d in YTD:
    #    query3.append("`Inv Date` == [\"")
    #    query3.append(d)
    #    query3.append("\"] or ")
    #query3 = query3[:-4] #is this the right index to remove extra " or " string from end?
    #input_date
    #DateString + "== "
    D = "`Inv Date`"
    SV = "Sale Value"
    CN = "Customer Name"

except:
    try:
        new = pd.read_excel(file,sheet_name="Sheet1")
        #query = "Doc_Date == [\""+date+"\"]"
        #query2 = "Doc_Date == [\""+Ldate+"\"]"
        #-------------------------------------
        #query3 = "Doc_Date == [\"2022-02-01\"] or Doc_Date == [\"2022-01-01\"]"
        #query4 = "Doc_Date == [\"2021-02-01\"] or Doc_Date == [\"2021-01-01\"]"
        SV = "__Sale_Value"
        CN = "Customer_Name_________________"
        D = "Doc_Date"
    except:
        try:
            new = pd.read_excel(file,sheet_name="List")
            #query = "Doc_Date == [\""+date+"\"]"
            #query2 = "Doc_Date == [\""+Ldate+"\"]"
            #-------------------------------------
            #query3 = "Doc_Date == [\"2022-02-01\"] or Doc_Date == [\"2022-01-01\"]"
            #query4 = "Doc_Date == [\"2021-02-01\"] or Doc_Date == [\"2021-01-01\"]"
            SV = "__Sale_Value"
            CN = "Customer_Name_________________"
            D = "Doc_Date"
        except:
            print("Error - sheet not found")
query = D+" == [\""+date+"\"]"
query2 = D+" == [\""+Ldate+"\"]"
#---------------------------------------
#query3 = "`Inv Date` == [\"2022-02-01\"] or `Inv Date` == [\"2022-01-01\"]"
#query4 = "`Inv Date` == [\"2021-02-01\"] or `Inv Date` == [\"2021-01-01\"]"
query3 = ""
for d in YTD:
    query3+=D+" == [\""
    query3+=d
    query3+="\"] or "
query3 = query3[:-4] #is this the right index to remove extra " or " string from end?
print(query3,"Debug1")
#----------------------------------------
query4 = ""
for d in LYTD:
    query4+=D+" == [\""
    query4+=d
    query4+="\"] or "
query4 = query4[:-4] #is this the right index to remove extra " or " string from end?
print(query4,"Debug2")
#----------------------------------------------------------------------------------------------------------

piv22 = pd.pivot_table(new.query(query),index=["Item Type",],values=[SV])
piv21 = pd.pivot_table(new.query(query2),index=["Item Type",],values=[SV])

Item22 = piv22.rename(columns={SV:month_year1})
Item21 = piv21.rename(columns={SV:month_year2})
items_month = pd.merge(Item22,Item21,how="outer",on="Item Type").fillna(0)
print(items_month,"\n\n")

#----------------------------------------------------------------------------------------------------------

piv22 = pd.pivot_table(new.query(query),index=[CN,],values=[SV])
piv21 = pd.pivot_table(new.query(query2),index=[CN,],values=[SV])

Cust22 = piv22.rename(columns={SV:month_year1})
Cust21 = piv21.rename(columns={SV:month_year2})
cust_month = pd.merge(Cust22,Cust21,how="outer",on=CN).fillna(0)
print(cust_month,"\n\n")

#----------------------------------------------------------------------------------------------------------

piv22 = pd.pivot_table(new.query(query3),index=[CN,],values=[SV])
piv21 = pd.pivot_table(new.query(query4),index=[CN,],values=[SV])

YTDCust22 = piv22.rename(columns={SV:"2022"})
YTDCust21 = piv21.rename(columns={SV:"2021"})
cust_ytd = pd.merge(YTDCust22,YTDCust21,how="outer",on=CN).fillna(0)
print(cust_ytd)

#----------------------------------------------------------------------------------------------------------

writer = pd.ExcelWriter(fd.asksaveasfilename(title='Output filename:'))
items_month.to_excel(writer,'Items This Month')
cust_month.to_excel(writer,'Customer Summary this Month')
cust_ytd.to_excel(writer,'Customer Summary YTD')

writer.save()

print("Completed!")
