# ALS-Data-Engineer-Exercises
ALS-Data Engineer Exercises
#Download Anaconda Naviagator Application- Python Distribution Package
#Link to Download - 
https://docs.anaconda.com/anaconda/navigator/#:~:text=Anaconda%20Navigator%20is%20a%20desktop,in%20a%20local%20Anaconda%20Repository.

Anaconda Naviagator contains all the Python libraries and the editor IDE - No additional installation of packages required
Libraries to import in the python program - pandas and datetime

if libraries pandas and datetime is not present or gives an error then re-install the packages again. See Below- How to install

# pip install pandas
# pip install DateTime

# Dataset - download the Data Sets in the working directory
cons.csv: https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons.csv

cons_email.csv:
    https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email.csv
    Boolean columns (including is_primary) in all of these datasets are 1/0 numeric values. 1 means True, 0 means False.
    The records that hold the primary email address are extracted from the given data set. 
   
cons_email_chapter_subscription.csv: 
    https://als-hiring.s3.amazonaws.com/fake_data/2020-07-01_17%3A11%3A00/cons_email_chapter_subscription.csv
    The records with chapter_id = 1 is extracted. 
     
# Output CSV files
1) people.csv

Holds the data schema of:
email(Primary email address), code (Source code), is_unsub(email address unsubscripted),
created_dt(Person created datetime), updated_dt (Person updated datetime)

2) acquisition_facts

Holds the aggregates stats about when people in the dataset were acquired

# Programming logic: 

Python with pandas packages were used to develop the programming code. 
The Data Files are in csv format downloaded from the specified sites.
The names of the Data files are: cons.csv, cons_email.csv, and cons_email_chapter_subcription.csv.

From each of the Data sets, the number of rows and columns were printed. 

From the Data Set, cons_email.csv, the records that have the column is_primary=1 is loaded into the Data Frame 
and the required columns are considered.

From the Data Set, cons_email_chapter_subscription_id.csv the records that have the column is_chapter_id=1 is 
loaded into the Data Frame and the required columns are considered.

The Data Sets are merged, we begin with merging in_cons_email and cons_email_chapter_subscription using cons_email_id
as connector between both the data sets. A left join is considered as we need the email addresses even if it is 
not present in_cons_email_chapter_subscription table. 

Review the meta_data.xlsx file as the connectors between the tables are highlighted and the assumption pertaining to the 
output file 'people.csv' is documented. 

To calculate the aggregate stats, about when people in the data set were acquired, the number of constituents acquired were aggregated 
by year as I failed to understand what is the criteria that must be incorporated in arriving at the conclusion. 









