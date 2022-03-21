import csv,sys
import pandas as pd
from tkinter import filedialog as fd

def selectFile():
    filetypes = (
        ('ASC', '*.asc'),
        ('csv files', '*.csv')
    )
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/192.168.100.97/c$/Reflex/qlikview/Flanagan/data/4_PowerBI',
        filetypes=filetypes)
    return filename



file = selectFile()

df = pd.read_csv(file,sep='\t')
print(df)

print(df.corr(method ='pearson'))
