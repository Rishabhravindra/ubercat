# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/hello/', methods=['POST'])
def hello():
    startLong=request.form['startLong']
    startLat=request.form['startLat']
    numSeat = request.form['numSeat']
    dorms = request.form['dorms']
    return render_template('form_action.html',
     startLong=startLong,
     startLat=startLat,
     numSeat = numSeat,
     dorms = dorms)

# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="localhost",
        port=int("80")
  )
