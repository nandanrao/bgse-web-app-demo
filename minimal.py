from flask import Flask, request, render_template, make_response
from dotenv import load_dotenv
import mysql.connector
import json
import os

# We create the Flask app. The template_folder defaults to "templates" already,
# but I put it here to be explicit. The same goes for "static", where we put all
# our static assets (css, images, etc.):
app = Flask(__name__, template_folder = 'templates', static_folder='static')

# This loads the .env file which holds our environment variables! You will need to
# create this file on every machine you want to run the app!
load_dotenv('./.env')

# This is how we connect using the python mysql connector. Note that this
# relies entirely on environment variables. If those environment variables are
# not properly set, this will throw an exception!
cnx = mysql.connector.connect(
    user = os.environ['MYSQL_USERNAME'],
    password = os.environ['MYSQL_PASSWORD'],
    host = os.environ['MYSQL_HOST'],
    database = os.environ['MYSQL_DB']
)


# Here we declare how we want to handle all HTTPP requests to the "home" path:
@app.route('/')
def home():

    # create cursor and execute query
    cursor = cnx.cursor()
    cursor.execute('SELECT ContactName, CustomerID FROM customers LIMIT 20')

    # mysql interface, returns a list of tuples (each item in the list is a row,
    # which is a tuple with the column values). In other worse:
    # [ (Laurence Lebihan, BONAP), (Maria Anders, ALKFI), ...]
    rows = cursor.fetchall()

    # Let's transform the tuples into python dictionaries so we can easily
    # access them by name later in our templates. We will just use the same
    # column names from the database (retrieved with column_names) as keys:
    # [ {'CustomerID': 'ALFKI', 'ContactName': 'Maria Anders'}, ...]
    customers = [dict(zip(cursor.column_names, customer)) for customer in rows]

    # we know longer need our database curser, so we close it.
    cursor.close()

    # render with a list of "customer" dictionaries to use in our template:
    return render_template('home.html', customers = customers)


# Flask gives us a variable, within get_customer function
# called "customer_id", that contains a string which is
# passed in this part of the PATH in a GET request.
@app.route('/customers/<customer_id>')
def get_customer(customer_id):

    # opens cursor for use in this query
    cursor = cnx.cursor()

    # %s is for string interpolation, the mysql library will pass
    # the second parameter of execute as variables into this string
    query = ('SELECT * FROM customers WHERE CustomerID = %(id)s')
    cursor.execute(query, { 'id': customer_id })

    # we get the first result of a query.
    customer = cursor.fetchone()

    # if we cannot find a customer, we return a 404 status, which means
    # we failed to find the resource. Error handling can help make
    # your development experience smoother, that way you know what's going
    # wrong!
    if not customer:
        return make_response('Sorry we could not find that customer', 404)


    # if we find a customer, we create a dictionary from the MySql Row.
    # This simply allows us to access the name via 'ContactName' instead
    # of needing to know the order of the columns. It also allows us to turn
    # the dictionary into JSON if we would rather send that:
    customer_dict = dict(zip(cursor.column_names, customer))
    cursor.close()

    # let's render this into html!
    return render_template('customer.html', name = customer_dict['ContactName'])

    # We could instead return JSON if we wanted and let the CLIENT do the rendering!
    # return json.dumps(customer_dict)


# This runs the flask app when 'python minimal.py' is run. By default,
# we listen on port 5000, if no FLASK_PORT environment variable is set:
if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 5000
    app.run(port = port)
