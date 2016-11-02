from flask import Flask, request, render_template_string
import mysql.connector
import json

app = Flask(__name__)
cnx = mysql.connector.connect(user='root', database='ecommerce')

# Flask gives us a variable, within get_customer function
# called "customer_id", that contains a string which is
# passed in this part of the PATH in a GET request.
@app.route("/customers/<customer_id>", methods = ['GET'])
def get_customer(customer_id):

    # opens cursor for use in this query
    cursor = cnx.cursor()

    # %s is for string interpolation, the mysql library will pass
    # the second parameter of execute as variables into this string
    query = ('select * from customers WHERE CustomerID = %(id)s')
    cursor.execute(query, { 'id': customer_id })

    # we get the first result of a query, and close the cursor
    customer = cursor.fetchone()
    customer_dict = dict(zip(cursor.column_names, customer))
    cursor.close()

    # let's render this into html!
    return render_template_string('<p> hello {{ name }}!</p>', name = customer_dict['ContactName'])
    # We could instead return JSON if we wanted and let the CLIENT do the rendering!
    # return json.dumps(customer)


if __name__ == "__main__":
    app.run()
