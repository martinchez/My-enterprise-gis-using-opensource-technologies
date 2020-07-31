import psycopg2

#DB connection properties
conn = psycopg2.connect(dbname = 'postgres', host= 'localhost', port= 5432, user = 'mo',password= 'mo')
conn.autocommit = True
cur = conn.cursor()  ## open a cursor

acctid = repr(str(raw_input("Enter your Account ID: ")))

thesql = "SELECT  a.loc || ' ' || a.location as addr "\
         "FROM parcels2007 AS a, parcels2007 AS b " \
         "WHERE st_touches(a.geom, b.geom) AND b.parcelkey = " + acctid


#print thesql
cur.execute(thesql)
rows = cur.fetchall()
for row in rows:
    print "Your adjacent properties are:   ", row[0]
    
cur.close()

acctid = repr(str(raw_input("Hit return to end")))


