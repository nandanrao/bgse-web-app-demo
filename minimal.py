from flask import Flask, request, render_template, make_response
import mysql.connector
import json

# We create the Flask app. The template_folder defaults to "templates" already,
# but I put it here to be explicit:
app = Flask("Minmal App", template_folder = "templates")

# This is how we connect using the python mysql connector:
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

    # we get the first result of a query.
    customer = cursor.fetchone()

    # if we cannot find a customer, we return a 404 status, which means
    # we failed to find the resource. Error handling can help make
    # your development experience smoother, that way you know what's going
    # wrong!
    if not customer:
        return make_response("Sorry we could not find that customer", 404)


    # if we find a customer, we create a dictionary from the MySql Row.
    # This simply allows us to access the name via 'ContactName' instead
    # of needing to know the order of the columns. It also allows us to turn
    # the dictionary into JSON if we would rather send that:
    customer_dict = dict(zip(cursor.column_names, customer))

    # we know longer need our database curser, so we close it.
    cursor.close()

    # let's render this into html!
    return render_template('./mypage.html', name = customer_dict['ContactName'])

    # We could instead return JSON if we wanted and let the CLIENT do the rendering!
    # return json.dumps(customer_dict)


# we run the Flask app. By default, Flask creates a server and listens on
# port 5000. We could change that if we needed by passing another port as
# a parameter to the "run" command:
if __name__ == "__main__":
    app.run()
