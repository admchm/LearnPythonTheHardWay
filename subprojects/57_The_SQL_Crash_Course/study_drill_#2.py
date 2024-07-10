## Study Drill #1: 
# The study drill for this exercise is simple to describe,
# but possibly difficult for you to do:
#
# Use Python to repeat all of the SQL shown in this exercise.
#
# To accomplish this goal you'll need the code from the
# Python sqlite3 documentation which describes in great detail
# how to use the module. You also know how to study documentation
# like this after Exercise 55 so leverage your skills when
# studying this library.
#
# One thing you must do when solving this is use placeholder values
# in your SQL as described in "How to use placeholders to bind values
# in SQL queries." If the link doesn't go directly to that section
# then scroll all the way down to the bottom or search for the word
# "placeholders."


# Answer:
import sqlite3
import pandas as pd

# Connecting to SQLite database
conn = sqlite3.connect('euro.sqlite3')
cursor = conn.cursor()

# Loading CSV data into the database
df = pd.read_csv('fixed.csv')
df.to_sql('euro', conn, if_exists='replace', index=False)

# Counting the rows in the table
cursor.execute('SELECT count(*) FROM euro')
print(cursor.fetchone()[0])  # Should print 6331

# Printing available rows (schema)
cursor.execute('PRAGMA table_info(euro)')
print(cursor.fetchall())

# Backing up the database
conn.backup(sqlite3.connect('euro_backup.sqlite3'))

# Recovering the database
# Use a file copy operation outside of this script:
# cp euro_backup.sqlite3 euro.sqlite3

# Getting help (example: SQLite3 help URL)
help_url = 'https://www.sqlite.org/cli.html'

# Create, Read, Update, Delete

# SELECT
query = """
SELECT date, PLN
FROM euro
WHERE date(date) > date('2023-01-01')
"""
for row in cursor.execute(query):
    print(row)

# INSERT
insert_query = """
INSERT INTO euro (date, PLN) VALUES (date('now'), 4.260)
"""
cursor.execute(insert_query)

insert_query = """
INSERT INTO euro (date, PLN) VALUES (date('now', '+1 day'), 4.1)
"""
cursor.execute(insert_query)
conn.commit()

# Getting the data for a specific day
query = """
SELECT * FROM euro WHERE date(date) > date('now', '-1 day')
"""
for row in cursor.execute(query):
    print(row)

# UPDATE
update_query = """
UPDATE euro
SET USD=100, date='2048-01-01'
WHERE date(date) > date('2023-01-01') AND USD=1.0808
"""
cursor.execute(update_query)
conn.commit()

# DELETE and Transactions
delete_query = """
DELETE FROM euro WHERE USD=1.1215
"""
cursor.execute(delete_query)
conn.commit()

# Transactions
cursor.execute('BEGIN TRANSACTION')
cursor.execute('DELETE FROM euro')
cursor.execute('ROLLBACK TRANSACTION')

cursor.execute('SELECT count(*) FROM euro')
print(cursor.fetchone()[0])  # Should print 6331

# Commented out because no transaction is active
# cursor.execute('COMMIT')

# Math, Aggregates, and GROUP BY
query = """
SELECT count(date) AS count_dates,
       date(date, 'start of month') AS month_start,
       avg(USD) AS avg_usd,
       min(USD) AS min_usd,
       max(USD) AS max_usd
FROM euro
GROUP BY date(date, 'start of month')
"""
for row in cursor.execute(query):
    print(row)

# ORDER BY
query = """
SELECT date, PLN FROM euro
ORDER BY PLN
"""
for row in cursor.execute(query):
    print(row)

# Closing the connection
conn.close()
