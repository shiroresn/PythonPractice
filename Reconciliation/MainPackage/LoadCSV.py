


import csv
import json
import psycopg2


csvfile = open('dm_1652_0001.csv', 'r')

reader = csv.DictReader( csvfile)



conn = psycopg2.connect(database="OTCProdRecon", user = "gloinc", password = "glodom2009", host = "172.21.120.247", port = "5432")

print ("Opened database successfully")

cur = conn.cursor()
#
# query = "select * from patient_view_new"
# cur.execute(query)
# result = cur.fetchall()
# print(result)

# cur.execute('''CREATE TABLE COMPA''')

for row in reader:
    X = row.get('CURHIC_UNEQ')
    query = "Select nname from patient_view_new where insurance1 = '5T21HX4EH17'"#"+row.get('CURHIC_UNEQ')+"' OR insurance2 = '"+row.get('MBI_ID')+"'"
    cur.execute(query)
    result = cur.fetchall()
    print(result)
    print(X)

