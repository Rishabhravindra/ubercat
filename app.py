# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for

# Get session token and connect with Uber Python API
import json
from getKeys import session
from uber_rides.client import UberRidesClient
client = UberRidesClient(session)

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case

dorms  = {"danHall":[39.131810, -84.512075,"Daniels Hall"],
		  "dabHall":[39.131858, -84.512654,"Dabney Hall"],
		  "morHall":[39.135247, -84.511780,"Morgens Hall"],
		  "upa":[39.128215, -84.514920, "University Park Apartments"]}
@app.route('/hello/', methods=['POST'])
def hello():
    startLong =request.form['startLong']
    startLat=request.form['startLat']
    numSeat = int(request.form['numSeat'])
    dorm = request.form['dorms']
    
    response = client.get_price_estimates(
    	start_latitude= startLat,
	    start_longitude=  startLong,
	    end_latitude= dorms[dorm][0],
	    end_longitude= dorms[dorm][1],
	    seat_count = numSeat
    )
    estimates = response.json.get('prices')
    cabType = estimates[0]['localized_display_name']
    return render_template('form_action.html',
     startLong=startLong,
     startLat=startLat,
     numSeat = numSeat,
     dorms = dorms[dorm][2],
     estimates = estimates,
     cabType = cabType)

# Run the app :)
if __name__ == '__main__':
  app.run( 
        host="localhost",
        port=int("80")
  )
