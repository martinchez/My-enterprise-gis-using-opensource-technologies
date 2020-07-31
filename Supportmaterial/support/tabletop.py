import psycopg2

#DB connection properties
conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'mo',password= 'mo')
conn.autocommit = True
cur = conn.cursor()  ## open a cursor

acctid = repr(str(raw_input("Enter your Account ID: ")))

thesql = "SELECT min(st_distance(floodzone.geom,parcels2007.geom)) as dist " \
         "FROM floodzone, parcels2007 WHERE parcels2007.parcelkey = " + acctid + " AND " \
         "floodzone.zone = 'AE' "

#print thesql
cur.execute(thesql)
rows = cur.fetchall()
for row in rows:
    print "Distance to the closest AE flood zone is:   ", row[0]
    
cur.close()

acctid = repr(str(raw_input("Hit return to end")))


