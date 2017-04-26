# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for

# Get session token and connect with Uber Python API
import json

#import google maps API's python wrapper to convert address to co-ordinates (geocoding)
import googlemaps

#get keys from the Uber and Google Maps developer console
from getKeys import session, gMapsKey

#create clients to interact with the online servers
from uber_rides.client import UberRidesClient
uberClient = UberRidesClient(session)
gmapsClient = googlemaps.Client(gMapsKey);


# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('form_submit.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is
# accepting: POST requests in this case
# print(geocode_result[0]["geometry"]["location"]["lat"])


#Create python dictionary to store dorm co-ordinates and full names
dorms  = {"danHall":[39.131810, -84.512075, "Daniels Hall"],
		  "dabHall":[39.131858, -84.512654, "Dabney Hall"],
		  "morHall":[39.135247, -84.511780, "Morgens Hall"],
          "sciHall":[39.134303, -84.512053, "Scioto Hall"],
		  "upa":[39.128215, -84.514920, "University Park Apartments"],
          "sidHall":[39.128981, -84.517728, "Siddall Hall"],
          "calHall":[39.128537, -84.516699, "Calhoun Hall"],
          "strHall":[39.131342, -84.522076, "Stratford Heights"],
          "turHall":[39.132313, -84.511764, "Turner Hall"]
          }
@app.route('/hello/', methods=['POST'])
def hello():
    #get data from the submitted form
    dorm = request.form['dorms']
    startLoc = request.form['startLoc'];
    geocode_result = gmapsClient.geocode(startLoc)

    response = uberClient.get_price_estimates(
    	start_latitude= geocode_result[0]["geometry"]["location"]["lat"],
	    start_longitude=  geocode_result[0]["geometry"]["location"]["lng"],
	    end_latitude= dorms[dorm][0],
	    end_longitude= dorms[dorm][1]    )

    estimates = response.json.get('prices')



    return render_template('form_action.html',
     startLoc=startLoc,
     dorms = dorms[dorm][2],
     estimates = estimates)

# Run the app :)
if __name__ == '__main__':
  app.run(
        host="localhost",
        port=int("5000")
  )
