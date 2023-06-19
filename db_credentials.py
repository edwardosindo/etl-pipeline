datawarehouse_name = ''

# sql-server (target db, datawarehouse)
datewarehouse_db_config = {
    'Trusted_Connection': 'yes',
    'TrustServerCertificate': 'yes',
    'driver': '{ODBC Driver 18 for SQL Server}',
    'server': '',
    'database': '{}'.format(),
    'autocommit': True,   
}

# sql-server (source db)
sqlserver_db_config = [
    {
        'Trusted_Connection': 'yes',
        'driver': '{ODBC Driver 17 for SQL Server}',
        'server': '',
        'database': '',
        'autocommit': True,
    }
]

# # mysql (source db)
# mysql_db_config = [
#     {
#         'user': 'your_user_1',
#         'password': 'your_password_1',
#         'host': 'db_connection_string_1',
#         'database': 'db_1',
#     },
#     {
#         'user': 'your_user_2',
#         'password': 'your_password_2',
#         'host': 'db_connection_string_2',
#         'database': 'db_2',
#     },
# ]