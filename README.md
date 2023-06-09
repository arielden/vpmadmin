
# vpmadmin
> model admin site

## Table of Contents
* [Setup](#setup)
* [Things to do](#things-to-do)
* [Contact](#contact)
* [Reference information](#reference)
<!-- * [License](#license) -->


## Setup
- I made a virtual env (venv) contained in the project directory.

Create the venv and activate it:
```
python3 -m venv venv
. venv/bin/activate

``` 
- For deactivate the virtual env (just enter the following command)
```
deactivate
```
- To use code runner with the venv created, add the following lines to "settings" (into the .code-workspace file)
```
		"code-runner.executorMap": {
			"python": ". ./venv/bin/activate && python -u",
		}
```

- Installing necessary packages:
```
pip install django
pip install django-extensions
pip install django-crispy-forms
pip install crispy-bootstrap5
```

## Django Usefull Commands
- Startproject, startapp and database migrations.
```
django-admin startproject [project name] .
python manage.py startapp [app name]
python manage.py makemigrations [app name]
python manage.py migrate
python manage.py runserver

```
- SuperUser
```
python manage.py createsuperuser
```


## Shell
- Some usefull queries.

lets say:
```
t = ToDoList.objects
```

Filtering elements...
```
t.filter(name__startwith="you_search")
t.filter(id=2)
```
Deleting objects.
```
deleted_object = t.get(id=1)
deleted_object.delete()
```

Adding elements.
```
t1 = ToDoList(name="first list")
t1.save()

```
More adding...
```
t = ToDoList.objects.get(id=2)
t.item_set.all()
t.item_set.create(text="Third item", complete=False)
t.item_set.create(text="Fourth item", complete=True)
```


## Using django shell
- To activate and start using the shell
```
python manage.py shell
```
- usefull test commands.
```
from [app_name].models import [Class names]
from main.models import ToDoList, Item

```

<!-- Relevant information about the project setup -->


## Things to do

To do:
-
-
-

## Contact
Created by [@arieldenaro](https://github.com/arielden) - feel free to contact me!

## Reference

* https://www.youtube.com/watch?v=sm1mokevMWk&t=9694s
* https://www.youtube.com/watch?v=e1IyzVyrLSU

<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->