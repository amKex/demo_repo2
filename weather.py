import requests

API_KEY = "a82c8523140ab35388acf9dfca2afb13"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input('Enter a city name? ')
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'

response = requests.get(request_url)
if response.status_code == 200:
	data = response.json()
	weather = data['weather'][0]['description']
	temp = round(data['main']['temp'] - 273.15, 2)

	print(f'weather:{weather}')
	print(f'Temprature: {temp} celsius')
else:
	print('an error occurred.')


