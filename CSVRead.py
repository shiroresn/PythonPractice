#EPISODE_ID, CURHIC_UNEQ, BENE_SK, CLAIMNO, LINEITEM, LINE_STD_ALLOWED, LINE_ALLOWED, FROM_DT, THRU_DT, PMT_AMT, SUP_NPI, TAX_NUM, EXPNSDT1, EXPNSDT2, HCPCS_CD, LPRPDAMT]
#Index: []


import csv
import json

csvfile = open('2018_05_31_grouped_dme_1654_0001.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("EPISODE_ID", "CURHIC_UNEQ", "BENE_SK", "CLAIMNO", "LINEITEM", "LINE_STD_ALLOWED", "LINE_ALLOWED", "FROM_DT", "THRU_DT", "PMT_AMT", "SUP_NPI", "TAX_NUM", "EXPNSDT1", "EXPNSDT2", "HCPCS_CD", "LPRPDAMT")
reader = csv.DictReader( csvfile, fieldnames)




for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')