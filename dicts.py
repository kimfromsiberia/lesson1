weather = {"city": "Москва", "temperature": "20"}
print(weather)
print(weather['city'])
weather['temperature'] = str(int(weather['temperature']) - 5)
print(weather)
print(weather.get('country', 'Россия'))
weather['date'] = '27.05.2019'
print(len(weather))