### Setup Django Project and App 

Before defining the models, you'll need to set up a new Django project and app. Here are the general steps you can follow:

Install Django using pip:

```
pip install Django
```

Create a new Django project:

```
django-admin startproject myproject
```

This will create a new directory called myproject that contains the basic structure of a Django project.

Create a new Django app within the project:

```bash
cd myproject
python manage.py startapp myapp
```

This will create a new directory called myapp that contains the basic structure of a Django app.

Add the new app to the project's list of installed apps by adding the following line to the INSTALLED_APPS list in the myproject/settings.py file:

```python
'myapp',
```

Define the models for the quiz and user quiz score tables in Django's ORM, as described in the previous answer.

Run the following commands to create the necessary database tables based on the models you've defined:

```
python manage.py makemigrations
python manage.py migrate
```

Finally, you can test your new Django app by running the development server with the following command:

```
python manage.py runserver
```

You should be able to visit the app in your web browser at http://localhost:8000/.

Of course, there are many more steps involved in building a complete Django app, but these should get you started with a basic project and app structure.
