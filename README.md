# Angelica's little blog

This is a microblog built as full-stack web app coded on Python, Flask, SQL.

The live version lives here - https://angelicas-flask-microblog.herokuapp.com/ ✨

## Motivation

I worked on this project to continue to learn full-stack software web development with Python.

I chose this particular project because it uses the skills I need to build my personal projects, including relational database design with one to one, one to many and many to many relationships.

## Features

- User authentication
- Profile avatars
- Follow other users
- Email support
- Pagination and page navigation
- Asynchronous functions and multi-threading
- Translations

## Technologies

- Flask
- Postgres
- werkzeug and hashlib for password security
- jwt.io for password reset tokens
- Babel

## Set up and run App

**Create a virtual environment**

`<python3 -m venv env>`

**Activate your virtual environment**

`<source env/bin/activate>`

**Install the required dependencies**

`<pip3 install -r requirements.txt>`

**To run the app**

`<flask run>`

## To add translations,

create a repository for each language you would like by running the command

`<pybabel init -i messages.pot -d translations -l language-abreviation>`

and replace "language-abbreviation" with the 2 syllable abbreviation.

This will create the language file in the translations folder.

To use translated texts use the command

`<pybabel compile>`

to compile the translations

To test this change was successful, change the language setting on our browser or force the language selector function to always return by changing it to

`<@babel.localeselector/ def get_locale(): /return 'language'>`

## Credits

To build this project, I used both **"Learning Flask Framework"** by Matt Copperwaite and Charles Leifer, published by Packt on Nov 2015 and **"The Flask Mega-Tutorial"** from Miguel Grinberg https://blog.miguelgrinberg.com/

Both are great resources, and it is not necessary to use both. Still, the goal of this project was to learn the technologies, I need for other projects, and I found using both resources incredibly helpful, particularly the chapters regarding databases.

For translations the Flask documentation was essential
https://pythonhosted.org/Flask-Babel/

to create transaltions you need to create a repository for each by running the command

`<pybabel init -i messages.pot -d translations -l language-abreviation>`

and replace "language-abreviation" with the 2 sylable abreviation.
This will create the language file in the translaiton folder
To use translatesd texts use comamnd

pybabel compile

to compile the translations

To test this change was successful, change the language setting on our browser or force the langage selector function to always return by chaging it to

`<@babel.localeselector def get_locale(): return 'language'>`
