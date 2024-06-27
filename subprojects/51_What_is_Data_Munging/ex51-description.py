# When you're doing Data Munging you're actually doing something called 
# Extract, Transform, and Load or ETL. This exercise is about the 
# Extract stage where you find various media to extract data from. 
# Usually you'll receive the data in a nice format, like JSON or CSV 
# files. In the worst--and sometimes the most lucrative--cases the media 
# is not in any format you can use, and you have to manually extract 
# what you need.

# The Problem
# I'm your manager and I had an idea last night while I drove my Tesla 
# home. I walked into your team's office and mumbled, "US beer consumption 
# as a service for mobile." I walked out and your team immediately had a 
# meeting to implement this brilliant idea. When they finished, the senior 
# developer tasked you with finding out how much beer is manufactured in 
# the US every month, but you're only able to get the PDF data from the 
# Alcohol, Tobacco, and Firearms Department (ATF). The ATF has the data 
# in Excel (.xls) format but the senior developer tells you to use PDF 
# because, "we paid for a license to Adobe Acrobat in 2010."

# Your job is to download that PDF and extract the following data:
# - Reporting Period
# - Report Date
# - Production for Current Month, Prior Year, Cumulative to Date
# - Stocks on Hand End of Month for Current Month, Prior Year Current Month
# - Calculate the difference between Production and Stock on Hand 
#   End-of-Month to determine the actual sales that month.

# Steps to implement
# Create some kind of class for pdftotext to parse the pdf file
# Create another class for required data
# Call method from first class to get the data
# Fill the data an object from the second class