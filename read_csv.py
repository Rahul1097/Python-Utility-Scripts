import csv

filepath = "./Input files/sample.csv"

def read_csv(filepath):
    '''Reads data from csv file'''
    users = []
    with open(filepath,'r',encoding = 'utf-8') as csv_file:
        #reader = csv.reader(csv_file,delimiter = ',',quotechar='\'',quoting=csv.QUOTE_ALL)
        reader = csv.reader(csv_file,delimiter = ',')

        #skip the header row
        reader.__next__()
        for row in reader:
            users.append(row)
        return users

userlist = read_csv(filepath)
print(userlist)
    
