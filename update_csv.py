import csv

user = ['123','mark wood','35']
filepath = "./Output files/update.csv"

def update_csv(filepath,user):
    '''Updates csv file'''
    user_data = "\n" + ",".join(user)
    f = open(filepath,'a',encoding="UTF-8")
    f.write(user_data)
    print("Updated user in file")
    f.close()

update_csv(filepath,user)
user = ['544','Alexandra Philippe','24']
update_csv(filepath,user)