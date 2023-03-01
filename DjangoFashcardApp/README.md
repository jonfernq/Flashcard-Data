## Multiple Choice Quiz App

Here is a recipe for a Coursera-like multiple choice quiz app in Django,
that displays a page of multiple choice questions using checkboxes.
When the user completes the quiz and hits submit, 
the quiz is corrected and wrong answers are highlighted in red,
with a total correct displayed at the bottom,
the multiple choice quiz is stored in a database table
and the user quiz score is stored in a separate database table. 

Here are some general steps you can follow to implement this app in Django:

0. **Setup:** [Setup Django Project and App.](https://github.com/jonfernq/Flashcard-Data/blob/main/DjangoFashcardApp/SetupDjangoProjectApp.md)

1. **Model:** [Define the models for the quiz and user quiz score tables in Django's ORM](https://github.com/jonfernq/Flashcard-Data/blob/main/DjangoFashcardApp/Models.md).

2. **Views:**[Create the views for the quiz page, submission page, and result page.](https://github.com/jonfernq/Flashcard-Data/blob/main/DjangoFashcardApp/Views.md) The quiz page should display the questions with checkboxes, the submission page should process the user's answers and calculate the score, and the result page should display the corrected quiz with wrong answers highlighted in red and the total score.

3. **URL Patterns:** [Define the URL patterns for the views.](https://github.com/jonfernq/Flashcard-Data/blob/main/DjangoFashcardApp/URLPatterns.md)

4. **Templates:** [Create the templates for the quiz, submission, and result pages.](https://github.com/jonfernq/Flashcard-Data/blob/main/DjangoFashcardApp/Templates.md)

5. **JavaScript:** [Write the JavaScript or jQuery code to highlight the wrong answers and calculate the score.](https://github.com/jonfernq/Flashcard-Data/blob/main/DjangoFashcardApp/JavaScript.md)

6. **Store Data:** [Implement the functionality to store the quiz and user quiz score data in the database.](https://github.com/jonfernq/Flashcard-Data/blob/main/DjangoFashcardApp/StoreData.md)

7. **Test App:** [Test the app and make any necessary adjustments.](https://github.com/jonfernq/Flashcard-Data/blob/main/DjangoFashcardApp/TestApp.md)

Additionally, an easy to deploy development environment can be set up:

8. [Docker Development Environment](https://github.com/jonfernq/Flashcard-Data/blob/main/DjangoFashcardApp/DockerDevEnvironment.md)

### Additional Details 

Here's a more detailed breakdown of the above steps:

1. Define the models for the quiz and user quiz score tables in Django's ORM:
You will need to define two models, one for the quiz questions and one for the user quiz scores. The quiz questions model should include fields for the question text, the answer options, and the correct answer. The user quiz scores model should include fields for the user's name or ID, the quiz questions answered, and the score.

2. Create the views for the quiz page, submission page, and result page:
The quiz page view should retrieve the questions from the database and display them with checkboxes. The submission page view should process the user's answers, compare them to the correct answers, and calculate the score. The result page view should retrieve the quiz questions and the user's answers from the database, highlight the wrong answers in red, and display the corrected quiz with the total score.

3. Define the URL patterns for the views:
You will need to define URL patterns that map to the quiz page, submission page, and result page views.

4. Create the templates for the quiz, submission, and result pages:
You will need to create HTML templates for each of the pages that use Django's templating language to display the dynamic content.

5. Write the JavaScript or jQuery code to highlight the wrong answers and calculate the score:
You can use JavaScript or jQuery to add the functionality to highlight the wrong answers and calculate the score on the client side.

6. Implement the functionality to store the quiz and user quiz score data in the database:
You will need to create a database table for the quiz questions and another table for the user quiz scores. When the user submits their answers, you can save their answers and the score in the user quiz score table.

7. Test the app and make any necessary adjustments:
Finally, you should test the app and make sure that everything is working as expected. You may need to make adjustments to the views, templates, or database models based on your testing results.

