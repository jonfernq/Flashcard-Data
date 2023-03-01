## Store Data 

Commands and code to accomplish this seventh 'store data' step for the Django quiz app:

7. Implement the functionality to store the quiz and user quiz score data in the database:

You will need to create a database table for the quiz questions and another table for the user quiz scores. When the user submits their answers, you can save their answers and the score in the user quiz score table.
Sure! Here's an example of how you can implement the functionality to store the quiz and user quiz score data in the database:

Define the models for the quiz and user quiz score tables in Django's ORM as described in step 1:

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    correct_answer = models.ForeignKey('Option', related_name='correct_for', on_delete=models.CASCADE)

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    option_text = models.CharField(max_length=200)
    selected = models.BooleanField(default=False)
    correct = models.BooleanField(default=False)

class UserQuizScore(models.Model):
    user = models.CharField(max_length=200)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
```

Update the views for the quiz page, submission page, and result page to save the user's answers and score to the database:

```python
from django.shortcuts import render, redirect
from .models import Question, Option, UserQuizScore

def quiz(request):
    questions = Question.objects.all()
    return render(request, 'quiz.html', {'questions': questions})

def submit(request):
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('question'):
                question_id = int(key[len('question'):])
                option_id = int(value)
                option = Option.objects.get(pk=option_id)
                option.selected = True
                option.save()
        return redirect('result')

def result(request):
    questions = Question.objects.all()
    score = 0
    for question in questions:
        selected_options = question.options.filter(selected=True)
        correct_options = question.correct_answer
        if selected_options.count() == correct_options.count() and selected_options.filter(correct=True).count() == correct_options.count():
            score += 1
        for option in question.options.all():
            if option.selected and not option.correct:
                UserQuizScore.objects.create(user=request.POST.get('user'), question=question, score=0)
                break
            elif not option.selected and option.correct:
                UserQuizScore.objects.create(user=request.POST.get('user'), question=question, score=0)
                break
            else:
                UserQuizScore.objects.create(user=request.POST.get('user'), question=question, score=1)
    return render(request, 'result.html', {'questions': questions, 'score': score})
```

In the submit view, we loop through each POST parameter to find the selected option for each question. We then update the selected field of the corresponding Option object and save it to the database.

In the result view, we calculate the score as in step 6. We then loop through each question and each option to check whether the option was selected and whether it was correct. We create a new UserQuizScore object for each option, with a score of 1 if it was correct and 0 if it was incorrect. We also store the user's name or ID in the user field.

With these changes, your Django quiz app should now be able to store quiz and user quiz score data in the database.
