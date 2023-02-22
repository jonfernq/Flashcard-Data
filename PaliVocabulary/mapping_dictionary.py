import csv
import random


# Open the CSV file for reading and create a CSV reader object
with open('pali_vocabulary2.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)

    # Save the headings
    headings = next(reader)

    # Read the rows into a list
    rows = list(reader)

# Save the length of the list
length_list = len(rows)

# Iterate over the list and add two items to the beginning of each row
for i, row in enumerate(rows):
    line_number = i + 1
    new_line_number = random.randint(0, length_list - 1)
    rows[i] = [line_number, new_line_number] + row

# Open a new CSV file for writing and create a CSV writer object
with open('random_line_numbers.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    # Write the two headings to the output file
    writer.writerow(['Line Number', 'New Line Number'] + headings)

    # Write the modified rows to the output file
    writer.writerows(rows)
