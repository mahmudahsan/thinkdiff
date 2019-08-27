### Django Commands

### New Directory
```
mkdir demo
cd demo
```

### VirtualEnv and PIP

```
pipenv install django
pipenv shell # activate virtual environment
```

### Project and App

```
django-admin startproject name_project .
python manage.py startapp app_name
```

### Database
```
python manage.py migrate # First Time
```

### Modification of Model ORM

```
python manage.py makemigrations app_name 
python manage.py migrate app_name 
```

### Super User Create for Admin

```
python manage.py createsuperuser
```

### Common Ref:
1. [Builtin Template](https://docs.djangoproject.com/en/2.0/ref/templates/builtins/#std:templatetag-block)

### Django Rest Framework
```
pipenv install djangorestframework
```

### Within Installed App Write

```
'rest_framework'
```

### In Pipenv Updating Python
```
pipenv install --python 3.7
```