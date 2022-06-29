import csv

header = ['Serial Number','Company Name','Description','Leave']
data = [['9788190000000','TALES OF SHIVA','mark',0],
        ['9780100000000','1Q84 THE COMPLETE TRILOGY','Mark',0],
        ['9780200000000','MY KUMAN','Mark',0],
        ['9780010000000','THE GOD OF SMAAL THINGS','4TH HARPER COLLINS',2]
        ]
filepath = "./Output files/csv_output.csv"


def create_csv(header,data,path):
    '''Creates csv file'''

    if len(data) > 0:
        with open(path,'w',encoding='UTF-8',newline='') as csv_file:
            writer = csv.writer(csv_file,delimiter=',')
            writer.writerow(header)
            for line in data:
                writer.writerow(line)
        print("Created csv file with {} users".format(len(data)))
    else:
        print("File not created")

create_csv(header,data,filepath)