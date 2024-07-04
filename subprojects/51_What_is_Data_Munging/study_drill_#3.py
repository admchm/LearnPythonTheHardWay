## Study Drill #3: 
## One thing all data munging tools needs is a "exception log." An 
## exception log reports what parts of what inputs have badly formed
## data while possibly saving the actual data for later inspection. 
## You need this because you don't want one bad PDF destroying the 
## entire ETL process, but you do need to go back and fix the problem 
## to re-run it. Make an exception logging system for your tool.

# Answer: 

# Here's an exception log for the provided script and PDF content:

### Exception Log

#### PDF Parsing:
#- **Issue:** 
# Failure in parsing the PDF could occur if the `pdftotext` library 
# isn't correctly set up or if it cannot handle the PDF's encoding or format.
#- **Solution:** 
# Ensure that `pdftotext` is installed and correctly configured. 
# Verify the PDF version and encoding to ensure compatibility.

#### Data Extraction Functions:
#- **Issue:** Functions `get_reporting_period` and `get_report_date` might return 
# `None` if no matching line starts with the expected strings due to formatting issues
# in the PDF.
#- **Solution:** Implement more robust search patterns or preprocess lines to remove
# unexpected formatting.

#### Data Extraction from Lines:
#- **Issue:** 
# The function `populate_columns` attempts to parse numbers using regular 
# expressions but applies it directly to the lines without checking if the match is 
# successful, potentially leading to `AttributeError` when accessing `.string` on `None`.
#- **Solution:** 
# Add a check to ensure `line` is not `None` before accessing `line.string`.

#### Column Data Parsing:
#- **Issue:** 
# Misinterpretation of column boundaries could result in incorrect data being extracted or 
# columns not containing the expected number of entries, leading to index errors.
#- **Solution:** 
# Validate the expected number of entries per column after parsing and adjust boundaries as 
# needed.

#### Production and Stocks Parsing:
#- **Issue:** 
# Incorrect handling of commas in numbers could lead to `InvalidOperation` errors when converting
# to `Decimal`.
#- **Solution:** 
# Ensure all strings representing numbers are correctly formatted by removing commas before 
# conversion to `Decimal`.

#### Reporting Outputs:
#- **Issue:** If any of the key data points (production, stocks on hand) are not found or parsed 
# correctly, the subsequent calculations and outputs will fail.
#- **Solution:** Include error handling and default values for each step of data extraction and 
# calculations to gracefully handle missing or malformed data.

#### File Handling:
#- **Issue:** 
# Hardcoding the filename could result in a `FileNotFoundError` if the file is not 
# present in the expected location.
#- **Solution:** 
# Implement a check to confirm the file exists before attempting to open it, and 
# potentially provide a user input option to specify the file path.

### Recommendations for Future Debugging:
#- Implement detailed logging at each step of the data processing pipeline to capture the state 
# of variables and outcomes of operations, especially before and after parsing sections of the PDF.
#- Consider wrapping critical operations in try-except blocks to capture and log exceptions while 
# allowing the program to continue running or fail gracefully.
#- Enhance regex patterns to be more flexible in handling variations in formatting within the PDF 
# documents.

# Updated code:
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

import logging
import functools

def safe_execute(func):
    @functools.wraps(func) # it is needed, because earlier functions with @safe_execute decorator
                           # that were throwing exceptions was treated as None instead of returning
                           # a callable function. 
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__} with args {args}, kwargs {kwargs}: {str(e)}")
            return None  # Explicitly return None on error to signal failure
    return wrapper

@safe_execute
def open_pdf(file_path):
    file = open(file_path, "rb")

    pdf = pdftotext.PDF(file)
    return pdf

@safe_execute
def get_reporting_period(lines):
    for line in lines:
        if line.startswith("Reporting Period"):
            return line
        
@safe_execute
def get_report_date(lines):
    for line in lines:
    
        if line.startswith("REVISED"):
            line = line[8:]
        
        if line.startswith("Report Date"):
            return line

@safe_execute
def populate_columns(lines):
    numbers = re.compile(r"^[,\d\s]+$")
    first_col, second_col, third_col, fourth_col = [], [], [], []
    
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

@safe_execute
def get_production(first_col, second_col, third_col, fourth_col):
    return first_col[0], second_col[0], third_col[0], fourth_col[0]

@safe_execute
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

@safe_execute
def diff_prod_and_stock_on_hand_curr_month(production, stocks_on_hand):
    prod_current_month = production[0].replace(',', '')
    stocks_current_month = stocks_on_hand[0].replace(',', '')
    
    return Decimal(prod_current_month) - Decimal(stocks_current_month)
    
@safe_execute
def diff_prod_and_stock_on_hand_prior_year(production, stocks_on_hand):
    prod_prior_year_current_month = production[1].replace(',', '')
    stocks_prior_year_current_month = stocks_on_hand[1].replace(',', '')
    
    return Decimal(prod_prior_year_current_month) - Decimal(stocks_prior_year_current_month)

@safe_execute
def calculate_actual_sales_stocks(stocks_ond_hand):
    stocks_current_month = stocks_on_hand[0].replace(',', '')
    stocks_prior_year_current_month = stocks_on_hand[1].replace(',', '')
    
    return Decimal(stocks_current_month) - Decimal(stocks_prior_year_current_month)

logging.basicConfig(filename='exception_log.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.info('Starting the PDF data extraction process.')

# filenames that could be used for testing:
# "Statistical_Report_Beer_October_2021.pdf"
# "Statistical_Report_Beer_November_2021.pdf"
# "Statistical_Report_Beer_December_2021_revised.pdf"

file_path = "Statistical_Report_Beer_December_2021_revised.pdf"

if __name__ == "__main__":
    logging.info("Script started")
    try:
        # Load and process the PDF
        pdf = open_pdf(file_path)
        # Additional processing and function calls
    except Exception as e:
        logging.error(f"Fatal error in main execution block: {str(e)}")
    finally:
        logging.info("Script ended")

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
