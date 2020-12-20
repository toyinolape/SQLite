# SQLite
SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. SQLite is the most used database engine in the world. 
SQLite is built into all mobile phones and most computers and comes bundled inside countless other applications that people use every day.

#### [SQLite_testdata:](httpsgithub.com/Josiah-Jovido/SQLite/blob/master/SQLite_testdata/SQLite_notebook_1.ipynb)
In this repo i worked with the car data prediction dataset obtained from kaggle, i used both jupyter notebook and VScode-[testdata.py](https://github.com/Josiah-Jovido/SQLite/blob/master/SQLite_testdata/testdata.py) for analyzing my data. All the steps all stated in detail in the corresponding notebook and python script.
I began by splitting my dataset into train and test sets, then i exported the test set out as a csv file, this was the main dataset i worked with for my analysis. I then imported SQLite library, connected my database, created a table and inserted the test.csv data. Then i queried the data for needed information.

#### [SQLite_studentdata:](https://github.com/Josiah-Jovido/SQLite/blob/master/SQLite_studentdata/database.py)
In this repo i worked with just VScode. i created three python scripts, the database.py, [data_app.py](https://github.com/Josiah-Jovido/SQLite/blob/master/SQLite_studentdata/data_app.py) and [callfunction.py](https://github.com/Josiah-Jovido/SQLite/blob/master/SQLite_studentdata/callfunction.py). database.py contains codes for the the student database i created using SQLite library, data_app.py contains codes for the functions i created to store different SQLite arguments for querying database, while the callfunction.py contains codes for calling the arguments on data_app.

# Building API
API stands for application programming interface. This is a concept in software technology that essentially refers to how multiple applications can interact with and obtain data from one another. APIs operate on an agreement of inputs and outputs.
**Application:** These can be apps that you use on your smartphone or a software program that you use.
**Programming:** Developers use APIs to write software.
**Interface:** How you interact with the application.

### How API's Work
To use an analogy here, we’ll compare this to ordering a drink at a bar. When you step up to the bar, you’re given a menu with several drinks listed. To look at this like an API, there’s an existing convention you can follow (i.e., the menu) to state your order and obtain a drink.

The menu as it’s presented to you is the interface. All the drinks listed on the menu are what the bartender has agreed to serve. When you ask for a certain drink on the menu, you receive it. But if you ask for something off the menu, such as a vodka martini instead of a gin martini, the bartender can’t provide it because it’s not something they agreed to serve.

Let’s say you want that gin martini delivered to your home. You call a delivery service and you order a martini that appears on the menu. When you order it, someone will tell the bartender your order, the bartender will make the martini and then someone will deliver it to your home. This is an example of an additional service (delivery) built on an “API” (the menu).

To relate this back to software, an API can help one application retrieve specific types of data from another. If the API doesn’t support certain types of data, it won’t be able to facilitate the retrieval of that “off-menu” data.
![Image](https://media.sproutsocial.com/uploads/2015/04/API_defined3-02.png)

#### Flask: 
In this repo i created a flask application ([app.py](https://github.com/Josiah-Jovido/SQLite/blob/master/SQLite_studentdata/flask/app.py), [index.html](https://github.com/Josiah-Jovido/SQLite/blob/master/SQLite_studentdata/flask/templates/index.html)) using vscode, this was just a simple application that shows how to build basic API's. The built API was then connected to Postman.

### Flappy App:
From the profitability report released by the Finance department of xyz shipping company, it was observed that a lot of expenditure is being spent on safety equipments for passengers. 
The management therefore wants a suitable cost cutting strategy to resolve this crisis and balance the financial sheet. A memo has been sent to the Data analysis department to resolve this problem using Machine Learning. The management needs a user web interface where one can easily predict the survival rate of passengers according to their Age, Sex, and Embarked status. We are required to use Data manipulation, Machine learning, API and web development to tackle this task. 

#### Methodology:
* Build the model
* Build API
* Build web page 
* Fit model into web page 
* Test on Postman 
* Get result from the web interface


