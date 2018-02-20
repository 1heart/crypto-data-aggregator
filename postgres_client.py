import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres', host='35.229.59.142', port='5432', password='hello')
cur = conn.cursor()
cur.execute("""SELECT * from data""")
rows = cur.fetchall()
for row in rows:
    print("   ", row)
