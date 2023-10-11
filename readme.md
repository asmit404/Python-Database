# Overview
This is a very simple command-line database management system made in python using prettytable and in-built libraries. It can store names, email addresses and phone numbers in a database and display them in a table. It can also search through the database using name, email or phone number. This application was made as a part of my school project.

## Functions
The application includes three main functions:
* Add Data
* Display Data
* Search Data

## In Depth Explanation
### Add Data Function
This function allows the user to add data to the database. The user can add a name, email address and phone number. The data is stored as a dictionary in a JSON file which is used as a database.

### Display Data Function
This function allows the user to display the data in the database in a table. The table is made using the prettytable library. The table includes the name, email address and phone number of the person.

### Search Data Function
This function allows the user to search for data in the database. The user can search for data using name, email address or phone number. The function will then display the data in a table. The table is made using the prettytable library. The table includes the name, email address and phone number of the person.

## Usage
### Install Dependencies
```bash 
pip install -r requirements.txt
```

### Run the program
```bash
python app.py
```
