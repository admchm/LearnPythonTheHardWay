## Study Drill #3:
## Find out why you had to write out_file.close() in the code.

# Answer: I had to write out_file.close() in the code just to free resources from memory and to ensure that the
#         data was actually saved. It is also a good practice, because it makes the code more readable. I also
#         found on the Internet that properly closing the file after operations can help prevent access conflicts
#         and errors that might occur if multiple processes tried to use it simultaneously.