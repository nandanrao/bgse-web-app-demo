# Minimal Web App using Python & MySql

## General

Read through the code and the comments!


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
