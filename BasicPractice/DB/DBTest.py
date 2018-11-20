import psycopg2

conn = psycopg2.connect(database="testdb", user = "gloinc", password = "glodom2009", host = "172.21.120.247", port = "5432")

print ("Opened database successfully")

cur = conn.cursor()
cur.execute('''CREATE TABLE COMPA''')