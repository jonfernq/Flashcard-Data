# blankout_word_in_sentence.py - 
# function that blanks out a word in an English sentence 
# if the first four characters match 

import re

def blankout_word_in_sentence(word, sentence):
    # Create a regular expression pattern that matches words that start with the first four letters of the input word
    pattern = re.compile(r'\b{}\w{{0,}}\b'.format(word[:4]))
    
    # Replace any matching words with underscores
    blanked_sentence = pattern.sub('_______', sentence)
    
    return blanked_sentence


# Test the function with different words and sentences
print('initiate', blankout_word_in_sentence('initiate', 'The company plans to initiate a new project soon.'))
# Output: 'initiate', 'The company plans to _______ a new project soon.'

print('injured', blankout_word_in_sentence('injured', 'The athlete was injured during the game.'))
# Output: 'injured', 'The athlete was _______ during the game.'

print('innovation', blankout_word_in_sentence('innovation', 'The company is known for its innovations in the tech industry.'))
# Output: 'innovation', 'The company is known for its _______ in the tech industry.'
