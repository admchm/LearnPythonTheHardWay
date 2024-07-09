import csv 
from pathlib import Path

input_file = "eurofxref-hist.csv"
output_file = Path("eurofxref-hist-fixed.csv")

if not output_file.exists():
    output_file.touch()
else:
    print("File already exists")

with open(input_file, mode='r', newline='') as infile, \
    open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            # removing last column
            new_row = row[:-1]
            
            writer.writerow(new_row)
        
print(f"A CSV file that was modified has been saved as {output_file}")