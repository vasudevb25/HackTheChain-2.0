import mysql.connector as ms
from JTL_Decr_V3_FA import *
sql=ms.connect(user="root",host="localhost",password="Arduino1")
c=sql.cursor()
c.execute("Use amazon")
