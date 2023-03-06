## Models

The first step in creating the Django quiz app:

Define the models for the quiz and user quiz score tables in Django's ORM:
 
Define two models, one for the quiz questions and one for the user quiz scores. 

Put the code below for the two models.py inside 'models.py' in the Django application folder.

The quiz questions model should include fields for the question text, the answer options, and the correct answer. 

The user quiz scores model should include fields for the user's name or ID, the quiz questions answered, and the score.

Here's an implementation of the two models in Django:

```python
from django.db import models

class QuizQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    answer_options = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=50)
    
    def __str__(self):
        return self.question_text

class UserQuizScore(models.Model):
    user_id = models.CharField(max_length=50)
    quiz_question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    selected_answer = models.CharField(max_length=50)
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return f'{self.user_id} - {self.quiz_question.question_text}'
```

In this implementation, the QuizQuestion model has fields for the question text, answer options, and correct answer. The UserQuizScore model has fields for the user's ID, the quiz question they answered, the selected answer, and the score they received for that question.

Note that the UserQuizScore model has a foreign key relationship to the QuizQuestion model, which means that each UserQuizScore object is associated with a specific QuizQuestion object.

Once you've defined these models in your Django app, you'll need to run the following commands to create the corresponding database tables:

```
python manage.py makemigrations
python manage.py migrate
```

This will create the necessary database tables based on the models you've defined.

Finally, you can test your new Django app by running the development server with the following command:

```
python manage.py runserver
```
You should be able to visit the app in your web browser at http://localhost:8000/.
