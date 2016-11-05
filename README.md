# Minimal Web App using Python & MySql

## General

Read through the code and the comments!

## Setting up your database / environment variables

### Background
Take a look at minimal.py, you will see where it connects to MySQL. Similar to connecting via Workbench, you need to tell the (python) mysql client WHERE to connect, WHAT database to use, and WHICH usernames/passwords to use to connect.

Because this could be different on your local machine, on your server, and on your teammates machine, we put this information into what are called "environment variables". These are global variables running in the UNIX process, that any application can access.

We use a pattern popularized by the application-hosting company Heroku, and put environment variables in a file called ".env". This file is kept our of source control (.gitignore), and must be created on every machine where the app will run.

### Create your environment variables:

Create a file called .env in the root of the project:

```
touch .env
```

Open your .env file, copy and paste the following text:

```
MYSQL_USERNAME=
MYSQL_PASSWORD=
MYSQL_HOST=
MYSQL_DB=ecommerce
```

Now fill in the four variables with connection information needed for your MySQL database. You can leave a field blank if you want it to revert to the "default". For example, if you want it to connect to a MySql instance on the same machine as the Python app is running, you can leave MYSQL_HOST blank:

```
MYSQL_HOST=
```

And it will default to connecting via "localhost".


## Running the App

Make sure you have [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) installed globally on your computer. If you do not, run:

```
pip install virtualenv
```

Create a virtual environment for this project. Make sure you are in the root directory of the project. Then run the following command:

```
virtualenv venv
```

This creates a virtual environment, called "venv", in this project. Now activate the environment with:

```
source venv/bin/activate
```

Your CLI should now be prefixed with (venv) to show that you are using the virtualenv. Now all "pip" commands will install libraries "locally", meaning only in this virtual environment. This keeps all your projects separate, and ensures that whatever runs on your computer will also run on a server!

Now install the libraries required for this app. These are canonically listed in the "requirements.txt" file.

```
pip install -r requirements.txt
```

Now that you have all the python libraries installed, you can run the app by typing:

```
python minimal.py
```

Now open your browser to [http://localhost:5000/customers/anatr](http://localhost:5000/customers/anatr)

## Templating

Flask uses Jinja2 syntax for HTML templates. You can read more [here](http://flask.pocoo.org/docs/0.11/tutorial/templates/). Basic concept with an HTML template: you write everything that you know ahead of time in HTML, then include "placeholders" for dynamic content. The server then "renders" the template, which just fills in the dynamic content based on variables it recieves in code, and then it creates a string of pure HTML.

Included in the code is a comment of how you can return pure JSON instead of HTML. Use this if you want to render the HTML in javascript in the browser.
