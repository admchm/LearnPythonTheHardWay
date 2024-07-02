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
    first_col = []
    second_col = []
    third_col = []
    fourth_col = []
    
    numbers = re.compile(r"^[,\d\s]+$")

    i = 1
    for line in lines:
        line = numbers.match(line)
        
        first_column_last_element = 9
        second_column_last_element = 18
        third_column_last_element = 27
        fourth_column_last_element = 36
        
        if line != None:
            if i < first_column_last_element:
                first_col.append(line.string)
                
            if i < second_column_last_element and i > first_column_last_element:
                second_col.append(line.string)
                
            if i < third_column_last_element and i > second_column_last_element:
                third_col.append(line.string)
                
            if i < fourth_column_last_element and i > third_column_last_element:
                fourth_col.append(line.string)
                
            i += 1
    
    return first_col, second_col, third_col, fourth_col

def get_production(first_col, second_col, third_col, fourth_col):
    return first_col[0], second_col[0], third_col[0], fourth_col[0]
    
file_name = "Statistical_Report_Beer_October_2021.pdf"
file = open(file_name, "rb")

pdf = pdftotext.PDF(file)

lines = "".join(pdf).split("\n")

current_month, prior_year_current_month, current_year_cumulative_to_date, prior_year_cumulative_to_date = populate_columns(lines)

print("\n#################### ANSWERS #################### ")
print(f"# - Reporting Period: {get_reporting_period(lines)}")
print(f"# - Report Date: {get_report_date(lines)}")
print(f"# - Production for Current Month, Prior Year, Cumulative to Date:")
print(get_production(current_month, prior_year_current_month, current_year_cumulative_to_date, prior_year_cumulative_to_date))
# - Stocks on Hand End of Month for Current Month, Prior Year Current Month
# - Calculate the difference between Production and Stock on Hand 
# - End-of-Month to determine the actual sales that month.



