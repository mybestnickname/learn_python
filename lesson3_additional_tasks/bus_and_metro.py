import csv
from decimal import Decimal
from math import cos, asin, sqrt, radians, sin

from metro import dict_creater


def distance(lat1, lon1, lat2, lon2):
    """
    Функция считающая расстояние между координатами по формуле хаверсина
    погрешность abs(1%) - из-за того, что в эксельке даны координаты по WSG84
    а считаю для сферы
    """
    # переводим в радианы
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # считаем по haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def coord_checker(coord_list, street_lat, street_lon):
    """
    Функции на вход подаётся список словарей координат выходов из метро
    и координаты остановки.
    Если находится такая точка из списка координат выходов из метро,
    что расстояние до остановки меньше 0.5км, то возвращаем True.
    Иначе False
    """
    for coord in coord_list:
        metro_lat = coord['latitude']
        metro_lon = coord['longitude']
        if distance(lat1=street_lat, lon1=street_lon, lat2=metro_lat, lon2=metro_lon) <= 0.5:
            return True
    else:
        return False


if __name__ == '__main__':
    # на линуксе перед заливкой в гит убрать
    metro_dict = dict_creater('metro.xlsx')
    # на линуксе перед заливкой в гит убрать
    with open('bus_stops.csv', 'r', encoding='windows-1251') as csvfile:
        # пропустим первую строчку
        headers = next(csvfile)
        streetreader = csv.reader(csvfile, delimiter=';')
        # составляем словарь - счётчик остановок
        # {'метро':[{коорд. метро},[{коорд остановок рядом},...]]}
        stops_counter_dict = {}
        # проходим по всем остановкам
        for row_index, row in enumerate(streetreader):
            street_lon = Decimal(row[2])
            street_lat = Decimal(row[3])
            print(row_index, street_lon, street_lat)
            # проходим по выходам из метро и ищем рядом с ними остановку
            for station_name, value in metro_dict.items():
                coord_list = value[0]
                # если остановка оказалась рядом со станцией, то отметим это
                if coord_checker(coord_list, street_lat, street_lon):
                    if not stops_counter_dict.get(station_name, False):
                        stops_counter_dict[station_name] = (
                            coord_list, [{'lat': street_lat, 'lon': street_lon}])
                    else:
                        stops_counter_dict[station_name][1].append(
                            {'lat': street_lat, 'lon': street_lon})
                    break
                else:
                    continue
        # подсчитаем, у какой станции больше всех остановок и выведем их
        max_key = max(stops_counter_dict, key=lambda k: len(
            stops_counter_dict[k][1]))
        print(max_key)
        print('{} остановок'.format(len(stops_counter_dict[max_key][1])))
        print('Их координаты:')
        for geo_dict in stops_counter_dict[max_key][1]:
            print('lon:{} lat:{}'.format(geo_dict['lon'], geo_dict['lat']))
        # проверить можно вбивая координаты в гугл-мапс :)
        # рядом с ю-з действительно очень много остановок))

else:
    pass
