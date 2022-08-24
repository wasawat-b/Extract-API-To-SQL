#drop table
fin_table_drop = "DROP TABLE IF EXISTS finance_statement_list"
his_table_drop = "DROP TABLE IF EXISTS historical_dividend"
delist_table_drop = "DROP TABLE IF EXISTS delisted_companies"


#create table
fin_table_create = "CREATE TABLE IF NOT EXISTS finance_statement_list (symbol VARCHAR NOT NULL);"

his_table_create = """
CREATE TABLE IF NOT EXISTS historical_dividend (
symbol VARCHAR NOT NULL,
date TIMESTAMP NOT NULL,
label VARCHAR NOT NULL,
adjDividend INT NOT NULL,
dividend INT NOT NULL,
recordDate TIMESTAMP NOT NULL,
paymentDate TIMESTAMP NOT NULL,
declarationDate TIMESTAMP NOT NULL);
"""

delist_table_create = """
CREATE TABLE IF NOT EXISTS delisted_companies (
symbol VARCHAR NOT NULL,
companyName VARCHAR,
exchange VARCHAR,
ipoDate TIMESTAMP,
delistedDate TIMESTAMP);
"""


#insert table
fin_table_insert = "INSERT INTO finance_statement_list (symbol) VALUES (%s);"
his_table_insert = "INSERT INTO historical_dividend (symbol, historical) VALUES (%s, %s);"
delist_table_insert = "INSERT INTO delisted_companies (symbol, companyName, exchange, ipoDate, delistedDate) VALUES (%s, %s, %s, %s, %s);"


#Query lists
create_table_queries = [fin_table_create, his_table_create, delist_table_create]
drop_table_queries = [fin_table_drop, his_table_drop, delist_table_drop]