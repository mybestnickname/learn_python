name_dict = {
    'a': {'city': 'Moscow', 'temperature': 13.2, 'wind': 8},
    'b': {'city': 'Moscow', 'temperature': 13.2, 'wind': 8},
    'c': {'city': 'Moscow', 'temperature': 13.2, 'wind': 8},
    'd': {'city': 'Moscow', 'temperature': 13.2, 'wind': 8},
}
key_name = input()
if name_dict.get(key_name, False):
    print(name_dict[key_name])
else:
    print('wrong key.')
