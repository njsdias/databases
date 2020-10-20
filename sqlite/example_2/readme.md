# SQLite Example-2: VED

This example reads a file of Vehicle Energy Dataset (VED), A Large-scale
Dataset for Vehicle Energy Consumption Research

The Vehicle Energy Dataset (VED), contains energy data collected from 383
personal cars in Ann Arbor, Michigan, USA. This open dataset
captures GPS trajectories of vehicles along with their time-
series data of fuel, energy, speed, and auxiliary power usage.

The dataset can be downloaded from [here](https://github.com/gsoh/VED/tree/master/Data).
The paper can be download from [here](https://arxiv.org/abs/1905.02081).


The first part of this example has the objective to read only one file
from VED repository and store the information in a database using SQLite.

The databases will not be commit in github due to each own size. 
Thus run first */first_part/databse.py* to create a dabase and insert values 
into a table. You will see a new file */first_part/ved.db* which is the
database with the table created stored with the information. 
The file *first_part/queries.db* allows us to execute queries.  


The second part is read all content files stored in VED repository.
The main objective is handling a huge dataset using memory.

 