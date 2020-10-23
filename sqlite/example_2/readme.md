# SQLite Example-2: VED

This example reads a file of Vehicle Energy Dataset (VED), A Large-scale
Dataset for Vehicle Energy Consumption Research

The Vehicle Energy Dataset (VED), contains energy data collected from 383
personal cars in Ann Arbor, Michigan, USA. This open dataset
captures GPS trajectories of vehicles along with their time-
series data of fuel, energy, speed, and auxiliary power usage.


The paper can be download from [here](https://arxiv.org/abs/1905.02081).


# Dataset Description

The dataset can be downloaded from [here](https://github.com/gsoh/VED/tree/master/Data).
It contains 54 csv files and two xlsx files.

The structure of **VED_Static_Data_ICE&HEV.xlsx** is:
- VehId
- Vehicle Type	
- Vehicle Class
- Engine Configuration & Displacement
- Transmission	
- Drive Wheels	
- Generalized_Weight

The structure of **VED_Static_Data_PHEV&HEV.xlsx** is:
- VehId
- Vehicle Type	
- Vehicle Class
- Engine Configuration & Displacement
- Transmission	
- Drive Wheels	
- Generalized_Weight


The structure of 54 csv files is:
- DayNum
- VehId
- Trip
- Timestamp(ms)
- Latitude[deg]
- Longitude[deg]
- Vehicle Speed[km/h]
- MAF[g/sec]
- Engine RPM[RPM]
- Absolute Load[%]
- OAT[DegC]
- Fuel Rate[L/hr]
- Air Conditioning Power[kW]
- Air Conditioning Power[Watts]
- Heater Power[Watts]
- HV Battery Current[A]
- HV Battery SOC[%]
- HV Battery Voltage[V]
- Short Term Fuel Trim Bank 1[%]
- Short Term Fuel Trim Bank 2[%]
- Long Term Fuel Trim Bank 1[%]
- Long Term Fuel Trim Bank 2[%]


# Problem Definition
Here we want to do an API that allow us to:
- plot the travels of each vehicle 
- discover vehicle concentrations
 
using the information provide by datasets.

The information from 54 cvs occupies 3.4 GB. To handle this information, a datatase was
built to store into a table this information. A second table stores the information from
the two xlsx files. The database will not be commit in github due to each own size. 

# Folders Structure
- databases: loclation where is stored the database
- datasets: location where is stored the files with data
- datasets/files_csv: location where is stored the csv files
- datasets/files_xlsx: location where is stored the xlsx files
- first_part: where is showed how is build a databse, table and insert values in table, 
              with a jupyter notebook to help you do data exploration    

## First Part
The first part of this example is a demonstrative part that shows
how we can build a database and create a table to store the information of only one
 csv file. 
 
Thus run 
        
        /first_part/main.py 
        
to create a dabase and insert values 
into a table. It uses **VED_171101_week.csv file**, but you can select what file you want.
After run the command  you will see a new file */first_part/databases/ved.db* which is the
database with the table created with the information that is in the csv file. 
The file *first_part/queries.db* allows us to execute queries.  

After this process a jupyter notebook can be used to explore the 
You can find a jupyter notebook example in the folder */notebook*

**Folder Structure**
- create tables: create tables if not exists
- database:
- insert_into_tables: define table structure to insert values
- main: create a table, read a file, insert values from file into table
- queries_db: to define functions to run sql SELECT queries
- read_files: read a file and store information in a list of tuples. 
The data of each row is stored in a tuple.
- utils: create/connect with database, define functions to run critical queries (i.e DROP) 

## Second Part
In the second part is showed how to store information from multiple files into a database
using SQLite. The main objective is create conditions to work with this huge dataset.
The databse with all information occupies 2.1 GB face out 3.2G. 

**Folder Structure**
- build_tables: read data from files and insert data into tables
- create_tables: create tables if not exists
- insert_into_tables: define table structure to insert values
- read_multiple_xlxs: all process only for xlsx files
- main: execute all process with only one function
- utils: create/connect to database and drop table. Here you can define other functions
that helps you to work with this dataset.


# **References**

[SQLite commands](https://www.sqlite.org/cli.html).

[Tutorial](https://www.youtube.com/watch?v=byHcYRpMgI4&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&start_radio=1&ab_channel=freeCodeCamp.org)




 