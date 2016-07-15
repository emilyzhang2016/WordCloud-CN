#coding: utf-8

import mysql.connector
import pandas as pd

# Connect with the MySQL Server
cnx = mysql.connector.connect(user='Emily',password='123456', database='mysql_shiyan')

# Get one buffered cursors
curA = cnx.cursor(buffered=True)

# Define a SQL function
select_stmt = (
  "SELECT * FROM country;"
)

#user cursor to execute the SQLfunction
curA.execute(select_stmt)
#get the values from MySQL
data=curA.fetchall()
#commit change to MySQL
cnx.commit()
#must close the cursor after each time's usage
cnx.close()

#use DataFrame to store the data
frame=pd.DataFrame(data)


print data
print frame
#there are difference between print data and print frame  that's why we import pandas to save data