# Import dependency
import sqlite3
import csv

# Connect to testdata
conn = sqlite3.connect('testdata.db')

# Create a cursor
c = conn.cursor()

#c.execute("DROP TABLE testdata")
#print('done')

# Create testdata Table
# c.execute("""CREATE TABLE testdata(
#                                    car_ID integer,
#                                   symboling integer,
#                                    CarName text,
#                                    fueltype text,
#                                   aspiration text,
#                                   doornumber text,
#                                   carbody text,
#                                   drivewheel text,
#                                   enginelocation text,
#                                   wheelbase float,
#                                   carlength float,
#                                   carwidth float,
#                                   carheight float,
#                                   curbweight integer,
#                                   enginetype text,
#                                   cylindernumber text,
#                                   enginesize integer,
#                                   fuelsystem text,
#                                   boreratio float,
#                                   stroke float,
#                                   compress float,
#                                   horsepower integer,
#                                   peakrpm integer,
#                                   citympg integer,
#                                   highwaympg integer
#                                    )""")

# file = open("test3.csv")
# test = csv.reader(file)
# c.executemany("INSERT INTO  testdata VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?)", test)

c.execute('SELECT * FROM testdata')
print(c.fetchmany(6))
# Insert testdata into Table
#c.execute("INSERT testdata FROM '/mnt/c/Users/HP/Documents/SQLite/testdata.npy' WITH (rowterminator='\n', fieldterminator=',')")
#print('command executed successfully...')

# Commit command
conn.commit()

# Close the connection
conn.close()
