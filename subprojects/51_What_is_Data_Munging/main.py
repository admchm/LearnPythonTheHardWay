# https://github.com/jalan/pdftotext - instructions

import pdftotext

file_name = "Statistical_Report_Beer_October_2021.pdf"
file = open(file_name, "rb")

pdf = pdftotext.PDF(file)

lines = "".join(pdf).split("\n")

i = 0
for line in lines:
    i += 1
    print(f"#{i}: {line}")

# find Reporting Period
# for line in lines:
#     if line.startswith("Reporting Period"):
#         # print it
#         print(line)
#     else:
#         print(line)