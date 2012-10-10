import requests

station_request = requests.get('http://w1.weather.gov/xml/current_obs/all_xml.zip')
print station_request.headers
with open('all_sites.zip', 'w') as f:
	f.write(station_request.content)


