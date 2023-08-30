import requests
response = requests.get('https://api.weather.gov/alerts')
json_data = response.json()
for entry in json_data['features']:
        print (entry['properties']['headline'])
        response = requests.get('https://api.weather.gov/alerts')
json_data = response.json()
print (json_data['features'][3]['properties']['headline'])
