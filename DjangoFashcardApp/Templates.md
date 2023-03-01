## Templates

Commands and code to accomplish this fifth 'templates' step for the Django quiz app:

5. Create the templates for the quiz, submission, and result pages:

You will need to create HTML templates for each of the pages that use Django's templating language to display the dynamic content.
Here's an example of how you could create the templates for the quiz, submission, and result pages:

- 1. Create a new directory called templates in your Django app's root directory if it doesn't exist already.
- 2. Inside the templates directory, create another directory called quiz.
- 3. Inside the quiz directory, create three new HTML templates: quiz.html, submission.html, and result.html.

Here's an example quiz.html template:

```html
{% extends 'base.html' %}

{% block content %}
  <form action="{% url 'submission' %}" method="post">
    {% csrf_token %}
    {% for question in questions %}
      <p>{{ question.question_text }}</p>
      {% for option in question.answer_options %}
        <label>
          <input type="checkbox" name="{{ question.id }}" value="{{ option }}">
          {{ option }}
        </label>
      {% endfor %}
    {% endfor %}
    <button type="submit">Submit</button>
  </form>
{% endblock %}
```
Here's an example submission.html template:

```html
{% extends 'base.html' %}

{% block content %}
  <h1>Result</h1>
  <p>You scored {{ score }} out of {{ total_questions }} correct.</p>
  <a href="{% url 'quiz' %}">Try again</a>
{% endblock %}
```
Here's an example result.html template:
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Result</h1>
  {% for question, answer in zip(questions, answers) %}
    <p>{{ question.question_text }}</p>
    {% for option in question.answer_options %}
      {% if option == answer %}
        <p style="color:green">{{ option }}</p>
      {% elif option == question.correct_answer %}
        <p style="color:green">{{ option }}</p>
      {% else %}
        <p style="color:red">{{ option }}</p>
      {% endif %}
    {% endfor %}
  {% endfor %}
  <p>You scored {{ score }} out of {{ total_questions }} correct.</p>
  <a href="{% url 'quiz' %}">Try again</a>
{% endblock %}
```
Note that each template extends a base.html template, which defines the overall structure of the page (e.g. header, footer, etc.). You'll need to create this base.html template in the templates directory as well. Here's an example base.html template:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{% block title %}Quiz App{% endblock %}</title>
</head>
<body>
  <nav>
    <ul>
      <li><a href="{% url 'quiz' %}">Quiz</a></li>
    </ul>
  </nav>
  {% block content %}{% endblock %}
</body>
</html>
```
This base.html template defines the overall structure of the page and includes a navigation bar with a link to the quiz page. Each template that extends base.html can override the title and content blocks with its own content.

