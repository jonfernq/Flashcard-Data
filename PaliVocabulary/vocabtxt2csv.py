import csv

# Define the split_string function as shown in the previous answer
import re
def split_string_last(string):
    """Split a string into two pieces with the delimiter being the last '.' in the string."""
    pattern = r'^(.*)\.(.*)$'
    match = re.match(pattern, string)
    if match:
        return match.group(1), match.group(2)
    else:
        return string, ''
        
def split_string_first(string):
    """Split a string into two pieces with the delimiter being the first '.' in the string."""
    pattern = r'^(.*?)\.(.*)$'  # regex pattern to match string with the first dot as delimiter
    match = re.match(pattern, string)  # match the pattern with the input string
    if match:  # if a match is found
        return match.group(1), match.group(2)  # return the two parts of the split string
    else:  # if no match is found
        return string, ''  # return the entire string as the first part and an empty string as the second part
        

# Open the input and output files
with open('input.txt', 'r', encoding='utf-8') as infile, open('pali_vocabulary.csv', 'w', newline='', encoding='utf-8') as outfile:

    # Create a CSV writer object with a tab delimiter
    writer = csv.writer(outfile, delimiter='\t')

    # Iterate over the lines of the input file
    for line in infile:

        # Strip any leading or trailing whitespace from the line
        line = line.strip()

        # Split the line at the last '.' using the split_string function
        #first_part, second_part = split_string_last(line)
        first_part, second_part = split_string_first(line)

        # Write the two parts as a row in the output CSV file
        writer.writerow([first_part, second_part])
