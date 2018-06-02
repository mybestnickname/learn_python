buser_info = {'first_name': '',
             'second_name': ''}
first_name = input('input first_name')
second_name = input('input second_name')
while not (first_name and second_name):
    first_name = input('input first_name: ')
    second_name = input('input second_name: ')
else:
    user_info['first_name'] = first_name
    user_info['second_name'] = second_name

print(user_info)
