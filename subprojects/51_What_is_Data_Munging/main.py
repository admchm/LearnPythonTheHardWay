# https://github.com/jalan/pdftotext - instructions

# Your job is to download that PDF and extract the following data:
# - Reporting Period
# - Report Date
# - Production for Current Month, Prior Year, Cumulative to Date
# - Stocks on Hand End of Month for Current Month, Prior Year Current Month
# - Calculate the difference between Production and Stock on Hand 
#   End-of-Month to determine the actual sales that month.

import re
import pdftotext

def get_reporting_period(lines):
    for line in lines:
        if line.startswith("Reporting Period"):
            return line
        
def get_report_date(lines):
    for line in lines:
        if line.startswith("Report Date"):
            return line
        
def populate_columns(lines):
    current_month = []
    prior_year_current_month = []
    current_year_cumulative_to_date = []
    prior_year_cumulative_to_date = []
    
    numbers = re.compile(r"^[,\d\s]+$")

    i = 1
    for line in lines:
        line = numbers.match(line)
        
        first_column = 9
        second_column = 18
        third_column = 27
        fourth_column = 36
        
        if line != None:
            if i < first_column:
                current_month.append(line.string)
                
            if i < second_column and i > first_column:
                prior_year_current_month.append(line.string)
                
            if i < third_column and i > second_column:
                current_year_cumulative_to_date.append(line.string)
                
            if i < fourth_column and i > third_column:
                prior_year_cumulative_to_date.append(line.string)
                
            i += 1
    
file_name = "Statistical_Report_Beer_October_2021.pdf"
file = open(file_name, "rb")

pdf = pdftotext.PDF(file)

lines = "".join(pdf).split("\n")

reporting_period = get_reporting_period(lines)
print(reporting_period)

report_date = get_report_date(lines)
print(report_date)

populate_columns(lines)