# validate_csv_column_count.py - 

# after screenscraping web page data
# checking if all rows have 4 columns
# some have 6 columns which means an additional 
# Thai-English example sentence pair,
# other entries were entered in a non-standard fashion 
# and had to be corrected manually. 

import csv, sys

def validate_csv_column_count(filename, correct_columns):
    incorrect_column_count = 0
    incorrect_columns = []
    total_column_count = 0

    with open(filename, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            column_count = len(row)
            total_column_count += column_count

            if column_count != correct_columns:
                incorrect_column_count += 1
                incorrect_columns.append(row)

    print("Total column count:", total_column_count)
    print("Incorrect column count:", incorrect_column_count)
    #print("Incorrect columns:", incorrect_columns)
    for column in incorrect_columns: 
        print('columns: ', str(len(column)), str(column), '\n') 
    

if __name__ == '__main__':
    #filename = sys.argv[1]
    #correct_columns = int(sys.argv[2])
    filename = "awl_thai_english.csv" 
    #filename = "output.csv" 
    correct_columns = 4
    validate_csv_column_count(filename, correct_columns)
    
    
