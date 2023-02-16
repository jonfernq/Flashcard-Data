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


