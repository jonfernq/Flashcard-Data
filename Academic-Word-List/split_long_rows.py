# split_long_rows.py - 
# this splits the long rows with extra example sentences found
# during data validation

import csv

def process_csv_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as csv_input_file, open(output_file, 'w', newline='', encoding='utf-8') as csv_output_file:
        csv_reader = csv.reader(csv_input_file)
        csv_writer = csv.writer(csv_output_file)

        for row in csv_reader:
            if len(row) == 6:
                original_row = [row[0], row[1], row[2], row[3]]
                csv_writer.writerow(original_row)
                new_row = [row[0], row[1], row[4], row[5]]
                csv_writer.writerow(new_row)
            else:
                csv_writer.writerow(row)

if __name__ == '__main__':
    input_file = 'awl_thai_english.csv'
    output_file = 'output.csv'
    process_csv_file(input_file, output_file)
