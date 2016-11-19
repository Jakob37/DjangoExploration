# Overview

Initially tracing the following tutorial:
https://docs.djangoproject.com/en/1.10/intro/tutorial02/

## Central parts

Some central concepts seems to be:

### URL forwarding

* Pattern matching for deciding where to go
* Performed both for site and for specific applications on site

### Views

* Seems to enable relating multiple HTML pages to single application

### Models

* Databases on conceptual level. Used by Django to both automate SQL database creation, and providing Python inteface to the databases.

## Useful commands

### Migration commands

```
# Migrate polls app after updating models
python manage.py makemigrations polls

# Show SQL migration procedure (in SQL code)
python manage.py sqlmigrate polls 0001

# Apply non-applied database migrations, creating needed tables
python manage.py migrate
```

### Procedure for changing models

* Change models (in `models.py`)
* Run `python manage.py makemigrations` to create migrations for changes
* Run `python manage.py migrate` to apply changes to database

### Interactively work with models

Run `python manage.py shell`. Then, we are ready to add stuff manually to our databases.

```
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()  # Save object to databse
>>> q.id  # Get object ID
>>> Question.objects.all()  # List all objects in Question database (?)
>>> q.question_text  # Access fields
```
