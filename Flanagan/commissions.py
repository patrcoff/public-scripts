import pandas as pd
from tkinter import filedialog as fd

pd.set_option("display.max_rows", None, "display.max_columns", None)


file = fd.askopenfilename(title='Open a file',initialdir='/C:/Users/patrick.coffey/OneDrive - Flanagan Flooring/Documents/')
month_year1 = "Feb 2022"
month_year2 = "Feb 2021"
try:#haven't fully accounted for all variances between the sheet names and headers yet but rest of code works well so far
    new = pd.read_excel(file,sheet_name="New Customer List")
    query = "`Inv Date` == [\"2022-02-01\"]"
    query2 = "`Inv Date` == [\"2021-02-01\"]"
    #---------------------------------------
    query3 = "`Inv Date` == [\"2022-02-01\"] or `Inv Date` == [\"2022-01-01\"]"
    query4 = "`Inv Date` == [\"2021-02-01\"] or `Inv Date` == [\"2021-01-01\"]"
    SV = "Sale Value"
    CN = "Customer Name"
    
except:
    try:
        new = pd.read_excel(file,sheet_name="Sheet1")
        query = "Doc_Date == [\"2022-02-01\"]"
        query2 = "Doc_Date == [\"2021-02-01\"]"
        #-------------------------------------
        query3 = "Doc_Date == [\"2022-02-01\"] or Doc_Date == [\"2022-01-01\"]"
        query4 = "Doc_Date == [\"2021-02-01\"] or Doc_Date == [\"2021-01-01\"]"
        SV = "__Sale_Value"
        CN = "Customer_Name_________________"
    except:
        try:
            new = pd.read_excel(file,sheet_name="List")
            query = "Doc_Date == [\"2022-02-01\"]"
            query2 = "Doc_Date == [\"2021-02-01\"]"
            #-------------------------------------
            query3 = "Doc_Date == [\"2022-02-01\"] or Doc_Date == [\"2022-01-01\"]"
            query4 = "Doc_Date == [\"2021-02-01\"] or Doc_Date == [\"2021-01-01\"]"
            SV = "__Sale_Value"
            CN = "Customer_Name_________________"
        except:
            print("Error - sheet not found")

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


                                                                      
