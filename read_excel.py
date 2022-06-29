import pandas as pd
import openpyxl

filepath = './Input files/sample_data.xlsx'

def read_excel_data(data_file):
    '''Reads data from excel file all tabs seperately and stores in dict of lists'''
    sheets = ['Userlist1','Userlist2']
    excel_data = {}
    i=0
    while i<len(sheets):
        sheet = pd.read_excel(data_file,sheets[i])
        df = pd.DataFrame(sheet)
        list1 = df.values.tolist()
        excel_data[sheets[i]] = list1
        i += 1

    return excel_data

data = read_excel_data(filepath)
print(data)

