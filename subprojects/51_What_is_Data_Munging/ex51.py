# https://github.com/jalan/pdftotext - instructions

# Your job is to download that PDF and extract the following data:
# - Reporting Period
# - Report Date
# - Production for Current Month, Prior Year, Cumulative to Date
# - Stocks on Hand End of Month for Current Month, Prior Year Current Month
# - Calculate the difference between Production and Stock on Hand 
# - End-of-Month to determine the actual sales that month.

import re
import pdftotext
from decimal import Decimal

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
        fourth_column_last_element = 37
        
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

def get_stocks_on_hand_for_two_columns(lines):
    numbers = re.compile(r"^[,\d\s]+$")
    stocks = []
    temp = []
    
    for line in lines:
        line = numbers.match(line)
        
        if line != None:
            temp.append(line.string)
            
    stocks = temp[-3:] # getting last three elements
    stocks.pop() # removing '\x0c'
    
    return stocks[0], stocks[1]

def diff_prod_and_stock_on_hand_curr_month(production, stocks_on_hand):
    prod_current_month = production[0].replace(',', '')
    stocks_current_month = stocks_on_hand[0].replace(',', '')
    
    return Decimal(prod_current_month) - Decimal(stocks_current_month)
    
def diff_prod_and_stock_on_hand_prior_year(production, stocks_on_hand):
    prod_prior_year_current_month = production[1].replace(',', '')
    stocks_prior_year_current_month = stocks_on_hand[1].replace(',', '')
    
    return Decimal(prod_prior_year_current_month) - Decimal(stocks_prior_year_current_month)

def calculate_actual_sales_stocks(stocks_ond_hand):
    stocks_current_month = stocks_on_hand[0].replace(',', '')
    stocks_prior_year_current_month = stocks_on_hand[1].replace(',', '')
    
    return Decimal(stocks_current_month) - Decimal(stocks_prior_year_current_month)

# filenames that could be used for testing:
# "Statistical_Report_Beer_October_2021.pdf"
# "Statistical_Report_Beer_November_2021.pdf"
# "Statistical_Report_Beer_December_2021_revised.pdf"

file_name = "Statistical_Report_Beer_October_2021.pdf"
file = open(file_name, "rb")

pdf = pdftotext.PDF(file)

lines = "".join(pdf).split("\n")

current_month, prior_year_current_month, current_year_cumulative_to_date, prior_year_cumulative_to_date = populate_columns(lines)
production = get_production(current_month, prior_year_current_month, current_year_cumulative_to_date, prior_year_cumulative_to_date)
stocks_on_hand = get_stocks_on_hand_for_two_columns(lines)

print("\n#################### ANSWERS #################### ")
print(f"# - Reporting Period: {get_reporting_period(lines)}")
print(f"# - Report Date: {get_report_date(lines)}")
print(f"# - Production for Current Month, Prior Year, Cumulative to Date {production}")
print(f"# - Stocks on Hand End of Month for Current Month, Prior Year Current Month: {get_stocks_on_hand_for_two_columns(lines)}")
print(f"# - Calculate the difference between Production and Stock on Hand:")
print(diff_prod_and_stock_on_hand_curr_month(production, stocks_on_hand))
print(diff_prod_and_stock_on_hand_prior_year(production, stocks_on_hand))
print(f"# - End-of-Month to determine the actual sales that month:")
print(calculate_actual_sales_stocks(stocks_on_hand))