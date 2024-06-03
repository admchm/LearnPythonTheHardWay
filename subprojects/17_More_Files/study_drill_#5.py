## Study Drill #5:
## Try converting this code to a ex17.py script you can run from Terminal/PowerShell again. If you're getting tired 
## of Jupyter's text editor then check out one of the editors mentioned in Exercise 0: Getting Started. You can also 
## try any of the editors mentioned in Exercise 0: Getting Started or found on the Complete Setup Page.

#python3 study_drill_#5.py

from_file = "test.txt"
to_file = "new_test.txt"

print(f"Copying from {from_file} to {to_file}.")

in_file = open(from_file)
indata = in_file.read()

print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print(f"Allright, all done for study drill #1.")

out_file.close()
in_file.close()