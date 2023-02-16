## Academic Word List (AWL) 

The Academic Word List (AWL) is one of the first first formal word lists of academic vocabulary that university students should master: 

"The Academic Word List (AWL) is a word list of 570 English words which appear with great frequency in a broad range of academic texts. 
The target readership is English as a second or foreign language students intending to enter English-medium higher education, and teachers of such students. 
[It is] divided into ten sublists in decreasing order of frequency." (Source: [Wikipedia](https://en.wikipedia.org/wiki/Academic_Word_List)) 

Also note that: 

"The AWL excludes words from the [General Service List](https://en.wikipedia.org/wiki/General_Service_List) (the 2000 highest-frequency words in general texts); however, many words in the AWL are general vocabulary rather than restricted to an academic domain, such as area, approach, create, similar, and occur in Sublist One." 

Here are various collections of the words in the AWL along with useful descriptive information:

- [awl_sublists.csv](https://github.com/jonfernq/Flashcard-Data/blob/main/Academic-Word-List/awl_sublists.csv): The three columns of this CSV are: Headword, Sublist (mentioned above), and Related word forms. (Source: [EAP Foundation](https://www.eapfoundation.com/vocab/academic/awllists/)) 

- [awl_thai_english.csv](https://github.com/jonfernq/Flashcard-Data/blob/main/Academic-Word-List/awl_thai_english.csv): The four columns of this CSV are: English word, English example sentence for the word, Thai word, 
Thai example sentence for the word. (Source: [Main list of AWL items with Thai / English examples](http://www.sealang.net/thai/vocabulary/awl-2.htm) from [SEAlang Thai Vocabulary](http://sealang.net/thai/vocabulary/)). Note: The data validation program ([validate_csv_column_count.py](https://github.com/jonfernq/Flashcard-Data/blob/main/Academic-Word-List/validate_csv_column_count.py)) revealed that the screen-scraped data had several invalid rows. Some errors were corrected manually, other errors were corrected by making an extra English-Thai example sentence pair. These extra example sentences were made into additional rows by [split_long_rows.py](https://github.com/jonfernq/Flashcard-Data/blob/main/Academic-Word-List/split_long_rows.py)), so that each row consists of one Thai-English pair of words and one pair of example sentences.

- [awl_thai_english_blanks.csv](https://github.com/jonfernq/Flashcard-Data/blob/main/Academic-Word-List/awl_thai_english_blanks.csv): Thai-English Academic Word List (AWL) with the given word blanked out in the English and Thai example sentences. Uses three Python scripts: [blankout_sentences.py](https://github.com/jonfernq/Flashcard-Data/blob/main/Academic-Word-List/blankout_sentences.py) which uses [blankout_word_in_sentence.py](https://github.com/jonfernq/Flashcard-Data/blob/main/Academic-Word-List/blankout_word_in_sentence.py) based on [blanked_out_thai_words.py](https://github.com/jonfernq/Flashcard-Data/blob/main/Academic-Word-List/blanked_out_thai_words.py).

## Multiple Choice Questions

- [fcards2mcquestions.py](https://github.com/jonfernq/Flashcard-Data/blob/main/Academic-Word-List/fcards2mcquestions.py): Generate multiple choice questions from a set of flashcards (see [output](https://github.com/jonfernq/Flashcard-Data/blob/main/Academic-Word-List/output_mcquestions.txt)).

Specifications: Given a list of flashcards each with front and back, and n the number of options for each multiple choice question to be constructed, then from these flashcards construct multiple choice questions in the following manner. Each front of a flashcard is the stem of a multiple choice question, the n options for that question are selected randomly from the backs of all flashcards. 

