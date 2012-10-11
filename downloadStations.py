import requests
from subprocess import call
import os
import xml.etree.ElementTree as ET
import json


sites = {}
call(["rm",'-r', "all_sites"])
os.makedirs('all_sites')

station_request = requests.get('http://w1.weather.gov/xml/current_obs/all_xml.zip')
print station_request.headers
with open('all_sites/all_sites.zip', 'w') as f:
	f.write(station_request.content)
call(["unzip", "all_sites/all_sites.zip", '-d', 'all_sites'])

fileCounter = 0
for file in os.listdir("all_sites"):
	if file.endswith(".xml"):
		site = ET.parse("all_sites/" + file)
		location  =''
		lat = ''
		long = ''
		wind  = ''

		if site.find('location') is not None and site.find('location').text is not None:
			location = site.find('location').text  
		if site.find('latitude') is not None:
			lat = site.find('latitude').text 
		if site.find('latitude') is not None:
			long = site.find('longitude').text 
		if site.find('wind_degrees') is not None:
			wind = site.find('wind_degrees').text 
		else:
			print "wind direction not found !!"
			

		sites[os.path.splitext(file)[0]] = {"loc": location, 'lat':lat , 'lng':long , 'wind': wind}
		#sites.update({'site': {"location": location, 'lat':lat , 'long':long }})
		fileCounter += 1

with open("static/all_sites.json", "wb") as f:
	json.dump(sites,f) 
