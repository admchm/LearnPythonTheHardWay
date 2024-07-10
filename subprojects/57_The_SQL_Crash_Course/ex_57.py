# commands:

# Loading a csv data file into sqlite3:
# sqlite3 euro.sqlite3

# sqlite> .import --csv "fixed.csv" euro
# sqlite> select count(*) from euro;
# 6331
# sqlite>

# Printing available rows:
# sqlite> .schema euro

# Backing Up Your Database:
# sqlite3 euro.sqlite3 ".backup euro_backup.sqlite3"
# for calling this command the sqlite3 shouldn't be running

# Recovering db:
#cp euro_backup.sqlite3 euro.sqlite3


# Create, Read, Update, Delete

#SELECT
# SELECT date, USD
#   FROM euro
#   WHERE date(date) > date('2023-01-01');


#INSERT
# INSERT INTO euro (date, USD)
#   VALUES (date('now'), 1.090);

# INSERT INTO euro (date, USD)
#   VALUES (date('now', '+1 day'), 1.087);


# SELECT * FROM euro WHERE date(date) > date('now', '-1 day');

# 2023-09-21|1.09||||||||||||||||||
# 2023-09-22|1.087||||||||||||||||||

#UPDATE
# UPDATE euro
#   SET USD=100, date='2048-01-01'
#   WHERE
#   date(date) > date('2023-01-01')
#     AND USD=1.0808;


#DELETE and Transactions
# DELETE FROM euro WHERE USD=1.1215;


# SELECT count(*) FROM euro;

# BEGIN TRANSACTION;

# DELETE FROM euro;

# ROLLBACK TRANSACTION;

# SELECT count(*) FROM euro;

# Math, Aggregates, and GROUP BY
#SELECT date, USD from euro GROUP BY date;

# SELECT count(date),
#     date, avg(USD),
#     min(USD), max(USD)
#   FROM euro
#   GROUP BY
#     date(date, "start of month");