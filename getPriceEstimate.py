import json
from getKeys import session
from uber_rides.client import UberRidesClient
client = UberRidesClient(session)

startPoint = [39.135566, -84.511845]
endPoint = [39.098232, -84.505418]
numSeat = 2

"""call get_price_estimates
   function to plug in the trip details
   and return a json with price estimates
"""
response = client.get_price_estimates(
    start_latitude= startPoint[0],
    start_longitude= startPoint[1],
    end_latitude= endPoint[0],
    end_longitude= endPoint[1],
    seat_count= numSeat
)

estimate = response.json.get('prices')

#save price estimates to json 
with open('data.txt', 'w') as saveFile:
	json.dump(estimate,saveFile)