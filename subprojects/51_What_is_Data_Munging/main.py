# https://github.com/jalan/pdftotext - instructions

# Your job is to download that PDF and extract the following data:
# - Reporting Period
# - Report Date
# - Production for Current Month, Prior Year, Cumulative to Date
# - Stocks on Hand End of Month for Current Month, Prior Year Current Month
# - Calculate the difference between Production and Stock on Hand 
#   End-of-Month to determine the actual sales that month.

import pdftotext

def get_reporting_period(lines):
    for line in lines:
        if line.startswith("Reporting Period"):
            return line
    
file_name = "Statistical_Report_Beer_October_2021.pdf"
file = open(file_name, "rb")

pdf = pdftotext.PDF(file)

lines = "".join(pdf).split("\n")

reporting_period = get_reporting_period(lines)
print(reporting_period)

# i = 0
# for line in lines:
#     i += 1
#     print(f"#{i}: {line}")
    


