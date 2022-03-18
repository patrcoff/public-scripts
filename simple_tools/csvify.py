#simple script to convert tab delimited .asc file to csv
import csv, sys


#delimfile = csv.reader('./QV.OEINVHEAD.asc', dialect=csv.excel_tab)
#with open('output.csv'
#outputfile = csv.writer('./output.csv','w',quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, lineterminator='\n')
#for row in delimfile:
    #outputfile.writerow(row)
#    print(row)

rows = []
with open('./QV.OEINVHEAD.asc','rt') as f:
    csv_reader = csv.reader(f, delimiter='\t')
    for row in csv_reader:
        rows.append(row)
        #print(row)
#for row in rows:
#    print(row)

with open('output.csv','w') as f:
    writer = csv.writer(f,quotechar='"', delimiter=',',quoting=csv.QUOTE_ALL, lineterminator='\n')
    for row in rows:
        writer.writerow(row)

        
print("Done!")
