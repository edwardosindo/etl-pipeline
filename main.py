'''
   This code in this file is responsible for iterating through credentials to connect with the database and perform the required ETL Using Python operations. 
'''

# Variables
import pyodbc

from db_credentials import datewarehouse_db_config, sqlserver_db_config
from sql_queries import sqlserver_queries

# Methods
from etl import etl_process

def main():
    print('Starting etl')
    
    # Establish connection for target database (sql-server)
    target_cnx = pyodbc.connect(**datewarehouse_db_config)
    
    # Loop through credentials
    
    # sql-server
    for config in sqlserver_db_config:
        try: 
            print("loading db: " + config['database'])
            etl_process(sqlserver_queries, target_cnx, config, 'sqlserver')
            print("This is done")
        except Exception as error:
            print(error)
            print("etl for {} has error".format(config['database']))
            print('error message: {}'.format(error))
            continue
        
    target_cnx.close()
    
if __name__ == "__main__":
    main()
        
    