import csv
import psycopg2
import json
import sys

csvfile = open('2018_05_31_grouped_dme_1654_0001.csv', 'r')

reader = csv.DictReader( csvfile)



conn = psycopg2.connect(database="OTCDemo", user = "gloinc", password = "glodom2009", host = "172.21.120.247", port = "5432")

print ("Opened database successfully")

cur = conn.cursor()
cur2 = conn.cursor()
cur3 = conn.cursor()


for row in reader:
    X = row.get('CURHIC_UNEQ')
    query = "Select id,nname from patient_view_new where insurance1 = '"+row.get('CURHIC_UNEQ')+"' OR insurance2 = '"+row.get('CURHIC_UNEQ')+"'"
    cur.execute(query)
    result = cur.fetchall()
    for ans in result:
        print("Insurance id ",X)

        m = ans[1]
        n = json.dumps(m)
        o = json.loads(n)

        name = o[0]['given'][0]+" "+o[0]['family']
        print("Patient id = ",ans[0])
        print("Patient Name : ",name)
        query2 = "select episodeid from episodebypatientdao where patientid='"+ans[0]+"'"
        cur2.execute(query2)
        result2 = cur2.fetchall()
        for episodeids in result2:
            for episodeid in episodeids:
                # print("Episode id : ", episodeid)
                query3 = "select targetprice,surgery_date from episodeofcare_view where id = '"+episodeid+"'"
                cur3.execute(query3)
                result3 = cur3.fetchall()
                # print("Target Price : ",result3[0][0])
                # print("Surgery Date : ",result3[0][1])


                keylist = list()
                for i in row.keys():
                    keylist.append(i)

                valuelist = list()
                for i in row.values():
                    valuelist.append(i)

                j=0
                jsondata = {}
                for key in keylist:
                    jsondata[key]=valuelist[j]
                    j=j+1

                jsondata['PATIENT_ID']=ans[0]
                jsondata['PATIENT_NAME'] = name
                jsondata['PATIENT_EPISODE_ID'] = episodeid
                jsondata['TARGET_PRICE'] = result3[0][0]
                jsondata['SURGERY_DATE'] = result3[0][1]

                print(jsondata)
                # print("")




