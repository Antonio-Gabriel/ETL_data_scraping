# ETL (Extract, Transform, Load)

ETL is a much-needed approach for those who want to export data from one location to another or different environments.

ETLs are systems that have the ability to read different file formats and data types and transport them from one environment to another.

ETl serves to consolidate data from different sources and deliver it to a new environment. In addition, it can be used when a company switches from old to new systems.

An ETL also helps bring together all the data in a business, contributing to decision making.

## ETL Processes

- Extraction
- Transformation (or Cleaning)
- Data Load (or Delivery)

ETL are components that fit into the data pipeline.

An architectural example of ETL's in practice.

<img src="https://www.altexsoft.com/media/2021/03/the-etl-workflow.png" alt="etl architecture image">

This is a project where I will be developing an ETL for data scraping with `python`.

## Start

To start this project first you need to run `db.sql` file in your mysql server and after if you have credentials in your mysql admin alter the database connector instance on:

[Database Connector File](src/infra/database_connector.py)

```py
class DatabaseConnector:
    connection = None

    @classmethod
    def connect(cls):
        """mysql driver connector"""
        db_connection = mysql.connect(
            host="localhost",
            port=3306,
            database="pipeline_db",
            user="root",
            passwd=""
        )

        cls.connection = db_connection

```
if not after run run `db.sql` file you only need to run the command bellow:

```bash
python3 -m venv venv
. venv/bin/activate # ubuntu
. venv/scripts/activate # windows
pip3 install -r requirements.txt
python3 run.py

# output
Inserted rows: #########1
Inserted rows: #########2
Inserted rows: #########3
Inserted rows: #########4
Inserted rows: #########5
Inserted rows: #########6
Inserted rows: #########7
Inserted rows: #########8
Inserted rows: #########9
Inserted rows: ########10
Inserted rows: ########11
Inserted rows: ########12
Inserted rows: ########13
Inserted rows: ########14
Inserted rows: ########15
Inserted rows: ########16
Inserted rows: ########17
Inserted rows: ########18
Inserted rows: ########19
Inserted rows: ########20
Inserted rows: ########21
Inserted rows: ########22
Inserted rows: ########23
Inserted rows: ########24
Inserted rows: ########25
Inserted rows: ########26
Inserted rows: ########27
Inserted rows: ########28
Inserted rows: ########29
```