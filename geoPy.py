import requests
import json
import datetime as dt
import sys

# Klasa pozwalajaca drukowac kolorowy napis w konsoli
class bcolors:
	RED = '\033[31m'
	GREEN = '\033[32m'
	BLUE = '\033[34m'
	YELLOW = '\033[33m'
	WHITE = '\033[37m'

# Otwarcie pliku json z listą miast
file = open('cities.json', 'r')
# Otwarcie pliku modułem json
file2 = json.load(file)

# Główne instrukcje programu jako definicja funkcji
def forecast():
	cityID = ''
	
	#Uzytkownik podaje nazwe miasta
	try:
		choosenCity = str(input(bcolors.WHITE + "Podaj nazwe miasta: "))
	except KeyboardInterrupt:
		print("\nDo widzenia!")
		sys.exit(1)

	#Sprawdzenie czy podane miasto znajduje sie w pliku json
	for i in file2:
		if i['name'].lower() == choosenCity.lower():
			cityID = i['id']
			break
	if cityID == '':
		print('Nie znam takiego miasta :-(')
		sys.exit(1)
	print("Miasto: " + choosenCity)

	# Tworzenie requestu o prognozę pogody
	buildRequest = "http://api.openweathermap.org/data/2.5/forecast?id=" + str(cityID) + "&APPID=77d9c13c4dce7d76513fe552e4a1e191&lang=pl"
	r = requests.get(buildRequest)
	# Serwer zwraca prognoze na kolejne 5 dni (w formie json)
	weatherJSON = json.loads(r.text)
	# Pobieranie dzisiejszej daty
	date = dt.date.today()

	# Proste menu wyboru dnia (dzisiaj/jutro/pojutrze)
	try:
		flag = input(bcolors.WHITE + "Wybierz dzień: \nDzisiaj(d)\nJutro(j)\nPojutrze(p)\n-> ")
	except KeyboardInterrupt:
		print("\nDo widzenia!")
		sys.exit(1)
	

	# Ustawienie wybranej daty
	if flag == 'd':
		print("Pogoda na dzisiaj")
	elif flag == 'j':
		print("Pogoda na jutro")
		date += dt.timedelta(days=1)
	elif flag == 'p':
		print("Pogoda na pojutrze")
		date += dt.timedelta(days=2)
	else:
		print('Zły symbol\nDo widzenia!')
		sys.exit(1)
	#  Drukowanie prognozy na ekran 
	for item in weatherJSON['list']:
		if str(date) in item['dt_txt']: 
			print(bcolors.YELLOW + item['dt_txt'])
			print(bcolors.RED + '\t' + str(int(item['main']['temp_max']) - 273) + ' st. C')
			print(bcolors.GREEN + '\t' + str(int(item['main']['pressure'])) + 'hPa')
			print(bcolors.BLUE + '\t' + item['weather'][0]['description'] + '\n')
	print('\n')
	
print("Nie używaj polskich znaków\n\
Aby przerwać program wciśnij CTRL+C")

while(True):
	forecast()
