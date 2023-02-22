import csv

# Bodhi Bodhi. 2020. Reading the Buddha's Discourses in Pāli : A Practical Guide to the Language of the Ancient Buddhist Canon. Somerville MA: Wisdom Publications.

# Open the CSV file for reading and create a CSV reader object
with open('decks_assigned.csv', 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)

    # Save the headings
    headings = next(reader)

    # Create a dictionary to hold the lines for each deck
    decks = {}

    # Iterate over the lines
    for line in reader:
        deck_assigned = line[-1]

        # Check if this deck has been created yet
        if deck_assigned not in decks:
            # Create a new deck
            decks[deck_assigned] = [headings]

        # Add this line to the deck
        decks[deck_assigned].append(line)

# Iterate over the decks and write them out to separate CSV files
for deck_num, deck_lines in decks.items():
    # Create the file name
    file_name = 'BodhiBodhi2020vocab_deck' + deck_num + '.csv'

    # Open the file for writing and create a CSV writer object
    with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)

        # Write the lines to the file
        writer.writerows(deck_lines)
