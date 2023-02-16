# fcards2mcquestions.py - 
# generate multiple choice questions from a set of flashcards 

import random

def create_multiple_choice_questions(flashcards, n):
    questions = []
    for card in flashcards:
        # Use the front of the card as the stem of the question
        stem = card[0]
        # Choose n-1 random options from the backs of all the other cards
        options = random.sample([c[1] for c in flashcards if c != card], n-1)
        # Add the correct answer (the back of the current card) to the list of options
        options.append(card[1])
        # Shuffle the options to avoid bias towards the correct answer being in a particular position
        random.shuffle(options)
        # Combine the stem and options into a single string and add to the list of questions
        question = f"{stem}\n\n" + "\n".join([f"{i+1}. {o}" for i, o in enumerate(options)])
        questions.append(question)
    return questions

flashcards = [    ("What is the capital of France?", "Paris"),    ("What is the largest planet in the solar system?", "Jupiter"),    ("What is the highest mountain in the world?", "Mount Everest"),    ("What is the chemical symbol for gold?", "Au"),    ("What is the largest country in the world by land area?", "Russia"),]
n = 4
questions = create_multiple_choice_questions(flashcards, n)
for i, question in enumerate(questions):
    print(f"Question {i+1}:")
    print(question)
    print()
