# CRUD-CAR-APP
CRUD App to access rental car database
There are two versions of same rental car database app.

Firse version SpeedyCarHire.py is with Microsoft SQL database
There are three files:

1.RustyCarHire.py  This file has source code for CRUD car database access APP

2.moduleSQLserverconfig.py This file has details of the SQL server database. By creating this additional file, we are not exposing 
database details in the source code. 
We are just importing this file/module in source code file to use it.

3.SpeedyHire.sql This is sql script file which has script to create database with which create app will be interacting
  Run this script in DBMS/database software.


Second verion of app Serialized_SpeedyCarHire_Version.py is nmplementing all the CRUD applications' functionality by storing data in programmer-defined JSON files without using a relational database.
There are two files:
1. Serialized_SpeedyCarHire_Version.py. This file has source code for app.
2. datafile3.json . This file is to store data (instead of SQL database we are usig JSON file)





