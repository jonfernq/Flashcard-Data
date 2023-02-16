# blankout_sentences.py - 
# takes the words and sentences in the Thai AWL: awl_thai_english.csv
# and creates new columns in the CSV file with Thai and English sentences 
# with the given word blanked out, for use in flashcards and multiple choice quizzes 

import csv
import re

def blankout_word_in_sentence(word, sentence):
    # Create a regular expression pattern that matches words that start with the first four letters of the input word
    pattern = re.compile(r'\b{}\w{{0,}}\b'.format(word[:4]))
    
    # Replace any matching words with underscores
    blanked_sentence = pattern.sub('_______', sentence)
    
    return blanked_sentence

def blankout_thai_word_in_sentence(word, sentence):
    pattern = r'{}'.format(word)
    regex = re.compile(pattern, re.UNICODE)
    return regex.sub('_______', sentence)
    

# Define regular expressions for extracting the English word and blanking out the sentence
word_regex = re.compile(r'^([^,]+)')
blank_regex = re.compile(r'(\b{}\b)')

def add_blanked_out_english(row):
        # Extract the English word from the ENGLISH WORD column
        english_word_match = word_regex.search(row['ENGLISH WORD'])
        if english_word_match:
            extracted_word = english_word_match.group(1)
        else:
            extracted_word = ''

        # Blank out the matching word in the ENGLISH SENTENCE column
        if extracted_word:
            #blanked_sentence = blank_regex.sub('_______', row['ENGLISH SENTENCE'].format(extracted_word))
            blanked_sentence = blankout_word_in_sentence(extracted_word, row['ENGLISH SENTENCE'])
        else:
            blanked_sentence = ''

        # Add the extracted word and blanked out sentence as new columns
        row['EXTRACTED WORD'] = extracted_word
        row['BLANKED SENTENCE'] = blanked_sentence
        return row 


def add_blanked_out_thai(row):
        extracted_word = row['THAI WORD']
        
        # Blank out the matching word in the THAI SENTENCE column
        if extracted_word:
            blanked_sentence = blankout_thai_word_in_sentence(extracted_word, row['THAI SENTENCE'])
        else:
            blanked_sentence = ''

        # Add the extracted word and blanked out sentence as new columns
        row['EXTRACTED THAI WORD'] = extracted_word
        row['BLANKED THAI SENTENCE'] = blanked_sentence
        return row 


# Open the input and output CSV files
with open('awl_thai_english.csv', 'r', encoding='utf-8') as csv_input, open('output4.csv', 'w', newline='', encoding='utf-8') as csv_output:
    # Create CSV reader and writer objects
    reader = csv.DictReader(csv_input)
    fieldnames = reader.fieldnames + ['EXTRACTED WORD', 'BLANKED SENTENCE','EXTRACTED THAI WORD', 'BLANKED THAI SENTENCE'] 
    writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
    writer.writeheader()

    # Loop through each row of the input file
    for row in reader:
        row = add_blanked_out_english(row)  
        row = add_blanked_out_thai(row) 
        # Write the row to the output file
        writer.writerow(row)

