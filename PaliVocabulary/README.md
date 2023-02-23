## Pali Vocabulary Flashcards

Reformatting word lists into flashcard CSV files.

From one recent book: 

- [Input](https://github.com/jonfernq/Flashcard-Data/blob/main/PaliVocabulary/input.txt) 
- One of many output files: [BodhiBodhi2020vocab_deck10.csv](https://github.com/jonfernq/Flashcard-Data/blob/main/PaliVocabulary/BodhiBodhi2020vocab_deck10.csv) 

The problem is create small-sized decks of flashcards that are not in alphabetical order to be uploaded to flashcard app such as Quizlet or Cram.com (or the apps in this repository).

First, starting with a raw vocabulary list scraped from its original source, it is reformatted into a CSV flashcard file with two columns 'front' and 'back'. ([vocabtxt2csv.py](https://github.com/jonfernq/Flashcard-Data/blob/main/PaliVocabulary/vocabtxt2csv.py))

Then the random mixing out of alphabetical order step occurs. 

Originally, the strategy of [random grouping](https://github.com/jonfernq/Flashcard-Data/blob/main/PaliVocabulary/random_grouping.py) was used.

An easier approach, however, was discovered, namely assigning a sequential number to each flashcard and then randomly mixing the flashcard numbers up, assigning each flashcard number to a new flashcard ([mapping_dictionary.py](https://github.com/jonfernq/Flashcard-Data/blob/main/PaliVocabulary/mapping_dictionary.py)).

Then, two additional simple steps completed the process, namely sorting on this new random line assignment and then sequentially renumbering the flashcards in this new sequence [assign_deck_sequentially.py](https://github.com/jonfernq/Flashcard-Data/blob/main/PaliVocabulary/assign_deck_sequentially.py). Then, there is iteration through the flashcards writing out flashcards in the same deck to a common csv deck file with a meaningful filename that can be used by the flashcard app/viewer.

The intial [input](https://github.com/jonfernq/Flashcard-Data/blob/main/PaliVocabulary/input.txt) is transformed into several csv files of flashcards similar to [BodhiBodhi2020vocab_deck10.csv](https://github.com/jonfernq/Flashcard-Data/blob/main/PaliVocabulary/BodhiBodhi2020vocab_deck10.csv). 






