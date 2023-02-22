import csv

# Open the CSV file for reading and create a CSV reader object
with open('random_line_numbers.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)

    # Save the headings
    headings = next(reader)

    # Read the rows into a list
    rows = list(reader)

# Sort the rows by "New Line Number"
rows_sorted = sorted(rows, key=lambda row: int(row[1]))

# Add a new column "Deck Assigned" to the headings
headings.append("Deck Assigned")

# Assign each successive 20 lines to a new deck
num_decks = len(rows) // 20 + 1
for i, row in enumerate(rows_sorted):
    deck_assigned = (i // 20) % num_decks + 1
    rows_sorted[i].append(deck_assigned)

# Open a new CSV file for writing and create a CSV writer object
with open('decks_assigned.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    # Write the headings to the output file
    writer.writerow(headings)

    # Write the modified rows to the output file
    writer.writerows(rows_sorted)
