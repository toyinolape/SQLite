# SQLite
SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world. 
SQLite is built into all mobile phones and most computers and comes bundled inside countless other applications that people use every day.

#### SQLite_testdata:
In this repo i worked with the car data prediction dataset obtained from kaggle, i used both jupyter notebook and VScode for analyzing my data. All the steps all stated in detail in the corresponding notebook and python script.
I began by splitting my dataset into train and test sets, then i exported the test set out as a csv file, this was the main dataset i worked with for my analysis. I then imported SQLite library, connected my database, created a table and inserted the test.csv data. Then i queried the data for needed information.

#### SQLite_studentdata:
In this repo i worked with just VScode. i created three python scripts, the database.py, data_app.py and callfunction.py. database.py contains codes for the the student database i created using SQLite library, data_app.py contains codes for the functions i created to store different SQLite arguments for querying database, while the callfunction.py contains codes for calling the arguments on data_app.
