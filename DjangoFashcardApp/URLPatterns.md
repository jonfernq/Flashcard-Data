## URL Patterns

Commands and code to accomplish this fourth 'URL patterns' step for the Django quiz app:

4. Define the URL patterns for the views:

You will need to define URL patterns that map to the quiz page, submission page, and result page views.
Sure, here's an example of how you could define the URL patterns for the views:

In your Django app's urls.py file, import the views and define the URL patterns like this:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('quiz/', views.quiz, name='quiz'),
    path('submission/', views.submission, name='submission'),
    path('result/', views.result, name='result'),
]
```

In this example, we've defined three URL patterns:

- /quiz/ maps to the quiz view, which displays the quiz questions.
- /submission/ maps to the submission view, which processes the user's answers.
- /result/ maps to the result view, which displays the corrected quiz with the total score.

Note that the name parameter gives each URL pattern a unique name, which we can use to reference the views in other parts of our Django app (e.g. in templates using the {% url %} tag).
