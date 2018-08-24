import sys
import urllib.request
import json

# Variables with API endpoint and key
endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = # Client requires personal key

origin = input('From: ').replace(' ', '+')
destination = input('To: ').replace(' ', '+')

# Building request
nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
request = endpoint + nav_request
response = urllib.request.urlopen(request).read()

# Decoding response
directions = json.loads(response.decode('utf -8'))

# Check number of viable routes, if any
routes = directions['routes']
routes_count = len(routes)
if routes_count < 1:
	sys.exit("No route found")
else: 
	start_address = routes[0]['legs'][0]['start_address']
	end_address = routes[0]['legs'][0]['end_address']

	print ("We're going from: '%s' to '%s'." % (start_address, end_address))

# Displaying relevant info about routes using response
for count in range(0, routes_count):
	summary = routes[count]['summary']
	distance = routes[count]['legs'][0]['distance']['text']
	time = routes[count]['legs'][0]['duration']['text']

	print ("Route %s Summary: %s" % (count + 1, summary))
	print ("Distance: %s" % distance)
	print ("Duration: %s" % time)