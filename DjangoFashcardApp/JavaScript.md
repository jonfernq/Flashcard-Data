Commands and code to accomplish this sixth 'JavaScript' step for the Django quiz app:

6. Write the JavaScript code to highlight the wrong answers and calculate the score:

You can use JavaScript to add the functionality to highlight the wrong answers and calculate the score on the client side.
Here's an example of how you can write the JavaScript code to highlight wrong answers and calculate the score:

Add a script tag to the bottom of your result.html template to include your JavaScript code:

```html
{% extends "base.html" %}

{% block content %}
  <h1>Quiz Results</h1>
  <table>
    {% for question in questions %}
      <tr>
        <td>{{ question.question_text }}</td>
        {% for option in question.options.all %}
          <td><input type="checkbox" name="question{{ question.id }}" value="{{ option.id }}" {% if option.selected %}checked{% endif %} disabled>{{ option.option_text }}</td>
        {% endfor %}
      </tr>
    {% endfor %}
  </table>
  <h2>Your score: <span id="score"></span></h2>

  <script src="{% static 'js/quiz.js' %}"></script>
{% endblock %}
```

Create a new file called quiz.js in your static directory to hold your JavaScript code.

In quiz.js, add an event listener to the submit button that will calculate the score:

```javascript
document.querySelector('form').addEventListener('submit', function(e) {
  e.preventDefault();
  var score = calculateScore();
  document.querySelector('#score').textContent = score + '/' + questions.length;
});
```

Create a function called calculateScore that will loop through each question, compare the selected answer to the correct answer, and highlight the wrong answers:

```javascript
function calculateScore() {
  var score = 0;
  questions.forEach(function(question) {
    var selectedAnswers = document.querySelectorAll('[name="question' + question.id + '"]:checked');
    var correctAnswers = question.options.filter(function(option) {
      return option.correct;
    });
    var correct = selectedAnswers.length === correctAnswers.length && correctAnswers.every(function(option) {
      return Array.prototype.some.call(selectedAnswers, function(selected) {
        return selected.value == option.id;
      });
    });
    if (!correct) {
      selectedAnswers.forEach(function(selected) {
        selected.parentNode.classList.add('wrong');
      });
    } else {
      score++;
    }
  });
  return score;
}
```

Finally, add some CSS to your stylesheet to style the wrong answers:

```css
input[type=checkbox]:checked + label.wrong {
  color: red;
}
```

With these changes, your quiz should now highlight wrong answers and calculate the score on the result page.
