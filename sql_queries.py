# Example queries for Extracting data from db platform
sqlserver_extract = (''' SELECT CurrencyKey, DateKey, AverageRate, EndOfDayRate, Date
FROM     dbo.FactCurrencyRate
                     ''')

sqlserver_insert = ('''
                    INSERT INTO [dbo].[FactCurrencyRate_etl] ([CurrencyKey],[DateKey],[AverageRate],[EndOfDayRate],[Date]) 
                    VALUES(?, ?, ?, ?, ?)
                    ''')
                    # VALUES (<CurrencyKey, int,>,<DateKey, int,>,<AverageRate, float,>,<EndOfDayRate, float,>,<Date, datetime,>)

# Exporting queries
class SqlQuery:
    def __init__(self, extract_query, load_query) -> None:
        self.extract_query = extract_query
        self.load_query = load_query
        
# create instances for SqlQuery class
sqlserver_query = SqlQuery(sqlserver_extract, sqlserver_insert)

# store as list for iteration
sqlserver_queries = [sqlserver_query]