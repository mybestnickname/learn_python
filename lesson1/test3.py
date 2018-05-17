#import traceback

weather = {'city': 'Moscow', 'temperature': 20, 'wind': 'East'}
print(weather['city'])
weather['temperature'] = 10
print(weather['temperature'])
print(len(weather))

if weather.get('country', False):
    print('y')
else:
    print('no')

try:
    weather['country']
except KeyError:
    print('no')
    # print(traceback.format_exc())

weather['date'] = '27.05.2017'
weather1 = {'city': 'Moscow', 'temperature': 20,
            'wind': 'East', 'date': '28.05.2017'}
weather2 = {'city': 'Moscow', 'temperature': 20,
            'wind': 'East', 'date': '29.05.2017'}
weathers_lst = []
for weather_dict in [weather, weather1, weather2]:
    weathers_lst.append(weather_dict)

print(weathers_lst)
