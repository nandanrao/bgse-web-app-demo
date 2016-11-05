# Minimal Web App using Python & MySql

## General

I think this is a very simple template/boilerplate that will show you how you can create a simple web server, using languages and technologies you have already learned in class (Python, MySql). You will have all the power of python (including all data-sciency libraries), and you will have a development process that will be easy to collaborate, and the final deployment should be smooth and easy.

Read through the code and the comments!

### Fork and Clone

Fork this repo into a repo of your own! You can do this here on github, just press "fork" in the upper right hand corner.

After you have forked the repo, you will be directed to your very own version of the repo, under your usernmame. You should then git clone that repo to your local machine using something like the following command:

```
git clone https://github.com/<YOUR USERNAME>/bgse-web-app-demo.git
```

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
FLASK_PORT=
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
FLASK_APP="minimal.py" FLASK_DEBUG=1 flask run
```

Now open your browser to [http://localhost:5000/customers/anatr](http://localhost:5000)

The command we ran sets two environment variables (FLASK_APP and FLASK_DEBUG) and then runs the command line tool "flask". This gives you the benefit of automatically reloading the server when you change your code, which is very nice for development.


## Templating

Flask uses Jinja2 syntax for HTML templates. You can read more [here](http://flask.pocoo.org/docs/0.11/tutorial/templates/). Basic concept with an HTML template:

* You write everything that is "static" (the same for every user) in HTML (with CSS and Javascript), just like you would with a simple web page.
* In the HTML "templates" you include "placeholders" for dynamic content. In Jinja2, these looke like this: {{ name }}
* Some library will then "render" the template. You give it the variables (name), and it puts those variables into the placeholders ({{ name }}). It then returns a string of pure HTML.

Included in the code is a comment of how you can return pure JSON instead of HTML. Use this if you want to render the HTML in javascript in the browser.

## Data Science Shit

You now have an app which includes:

* A variable given to you by the user (customer id)
* A database where you can run any SQL query you can imagine
* A full Python runtime where you can do anything in Python with the above to elements!

You can import scipy, pandas, or any other python library you use for doing all your fancy data science, and use that to run functions, live, based on variables given to you by the user. It's easy!


## Deploying to a server

Running your app on your server should be simple and repeatable. If you are running your MySQL database on the same server, you will need to set that up first. Otherwise, the following steps should be all you need to do:

* git clone your repo onto your server
* create your .env file in the project root
* set the FLASK_PORT variable to 80

Now run:

```
python minimal.py
```

Make sure to setup your security group to expose port 80 (http) to the world. Your web app should now be available to everyone, just browse to the Public DNS of your server!
