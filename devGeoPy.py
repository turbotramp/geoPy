import requests
import json
import datetime as dt
import sys

class bcolors:
	RED = '\033[31m'
	GREEN = '\033[32m'
	BLUE = '\033[34m'
	YELLOW = '\033[33m'
	WHITE = '\033[37m'

apiKey = '77d9c13c4dce7d76513fe552e4a1e191'

file = open('cities.json', 'r')
file2 = json.load(file)
def forecast(): 
	try:
		choosenCity = str(input(bcolors.WHITE + "Podaj nazwe miasta: "))
	except KeyboardInterrupt:
		print("\nDo widzenia!")
		sys.exit(1)

	for i in file2:
		if i['name'].lower() == choosenCity.lower():
			cityID = i['id']
			break
	print("Miasto: " + choosenCity)

	buildRequest = "http://api.openweathermap.org/data/2.5/forecast?id=" + str(cityID) + "&APPID=77d9c13c4dce7d76513fe552e4a1e191&lang=pl"
	r = requests.get(buildRequest)
	weatherJSON = json.loads(r.text)

	date = dt.date.today()
	try:
		flag = input(bcolors.WHITE + "Wybierz dzień: \nDzisiaj(d)\nJutro(j)\nPojutrze(p)\n-> ")
	except KeyboardInterrupt:
		print("\nDo widzenia!")
		sys.exit(1)
	if flag == 'd':
		print("Pogoda na dzisiaj")
	elif flag == 'j':
		print("Pogoda na jutro")
		date += dt.timedelta(days=1)
	elif flag == 'p':
		print("Pogoda na pojutrze")
		date += dt.timedelta(days=2)

	for item in weatherJSON['list']:
		if str(date) in item['dt_txt']: 
			print(bcolors.YELLOW + item['dt_txt'])
			print(bcolors.RED + '\t' + str(int(item['main']['temp_max']) - 273) + ' st. C')
			print(bcolors.GREEN + '\t' + str(int(item['main']['pressure'])) + 'hPa')
			print(bcolors.BLUE + '\t' + item['weather'][0]['description'] + '\n')
	print('\n')
	
print("Nie używaj polskich znaków.")
print("Aby przerwać program wciśnij CTRL+C")

while(True):
	forecast()
