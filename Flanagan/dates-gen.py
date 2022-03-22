#we want to generate the list of months of this YTD and last YTD in format 2022-04-01

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
    return datesListThisYear,datesListLastYear


month = "04" #user selected month of april
year = 2022 #user selected year of 2022
print(generate_dates(year,month))
