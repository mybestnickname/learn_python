import csv


if __name__ == '__main__':
    file_path = 'bus_stops.csv'
    street_dict = {}
    with open(file_path, 'r', encoding='windows-1251') as csvfile:
        streetreader = csv.reader(csvfile, delimiter=';')
        street_dict = {}
        for row in streetreader:
            if not street_dict.get(row[4], False):
                street_dict[row[4]] = 1
            else:
                street_dict[row[4]] += 1
    # удалим улицу 'проезд без названия'
    del street_dict['проезд без названия']
    max_key = max(street_dict, key=lambda k: street_dict[k])
    print(max_key)
    print('{} остановка'.format(street_dict[max_key]))
else:
    pass
