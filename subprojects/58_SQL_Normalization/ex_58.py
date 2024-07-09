# Creating Tables in SQL

# CREATE TABLE IF NOT EXISTS rate
#   id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#   date DATE, currency TEXT, rate FLOAT;

# DROP TABLE IF EXISTS table_name;

# Implementing 2NF
# DROP TABLE IF EXISTS currency;

# CREATE TABLE currency (id INTEGER PRIMARY KEY
#   AUTOINCREMENT NOT NULL, currency TEXT);

# ALTER TABLE rate ADD COLUMN currency_id INTEGER;

# INSERT INTO currency (currency) SELECT currency FROM rate GROUP BY
# currency;

# UPDATE rate SET currency_id = currency.id FROM currency WHERE
# rate.currency = currency.currency;

# ALTER TABLE rate DROP COLUMN currency;

# sqlite> .schema rate
# sqlite> .schema currency
# sqlite> select * from rate;
# sqlite> select * from currency;

# Querying 2NF Data
# SELECT * FROM rate, currency WHERE
#   rate.currency_id=currency.id
#   AND currency.currency='USD'
#   AND date(rate.date) > date('2023-01-01');

# sqlite> SELECT count(*) from rate, currency
#    WHERE currency.currency='USD' AND
#    date(rate.date) > date('2023-01-01');

# 7544

# sqlite> SELECT count(*) from rate, currency WHERE
#    rate.currency_id=currency.id AND
#    currency.currency='USD' AND
#    date(rate.date) > date('2023-01-01');

# 184

# Querying with Joins