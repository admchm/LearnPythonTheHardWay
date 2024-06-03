## Study Drill #4:
## Find out why we had to pass a 'w' as an extra parameter to open. Hint: open tries to be safe by 
## making you explicitly say you want to write a file.

# Answer:

# As I wrote in ex16.py:
# from search: python open site:"python.org"
# 'r' - open for reading (default)
# 'w' - open for writing, truncating the file first
# 'x' - open for exclusive creation, failing if the file already exists
# 'a' - open for writing, appending to the end of file if it exists
# 'b' - binary mode
# 't' - text mode (default)
# '+' - open for updating (reading and writing)

# We had to pass a 'w' as an extra parameter to open, because we needed to truncate the file first.