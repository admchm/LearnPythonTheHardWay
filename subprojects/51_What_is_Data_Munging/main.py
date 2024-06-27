# I will call required functions here

# sample
# import modules I need
import pdftotext
import sys

# open the pdf
infile = open(sys.argv[1], "rb")

# convert it to text
pdf = pdftotext.PDF(infile)

lines = "".join(pdf).split("\n")

# find Reporting Period
for line in lines:
    if line.startswith("Reporting Period"):
        # print it
        print(line)
    else:
        print(line)