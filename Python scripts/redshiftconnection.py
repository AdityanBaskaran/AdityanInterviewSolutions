import psycopg2
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
DATABASE = raw_input( "provide database name " )
USER = raw_input( "provide user name " )
PASSWORD = raw_input( "provide password.. " )
HOST = raw_input( "provide host url " )
PORT = raw_input( "provide PORT Number.. " )
createquery = raw_input("Enter the Create table query.. ")
querytoexec = raw_input("Enter the copy command ... ")
SCHEMA = "public"

connection_string = "redshift+psycopg2://%s:%s@%s:%s/%s" % (USER,PASSWORD,HOST,str(PORT),DATABASE)
engine = sa.create_engine(connection_string)
session = sessionmaker()
session.configure(bind=engine)
s = session()
SetPath = "SET search_path TO %s" % SCHEMA
s.execute(SetPath)

query1 = createquery
query2 = querytoexec
rr1 = s.execute(query1)
rr2 = s.execute(query2)
all_results =  rr2.fetchall()

def pretty(all_results):
   for row in all_results :
        print "row start >>>>>>>>>>>>>>>>>>>>"
        for r in row :
            print " ----" , r
        print "row end >>>>>>>>>>>>>>>>>>>>>>"


pretty(all_results)
s.close()
~
