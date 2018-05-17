grades_list = [
    {'school_class': '4a', 'scores': [3, 4, 4, 5, 2]},
    {'school_class': '4b', 'scores': [3, 5, 4, 2]},
    {'school_class': '4c', 'scores': [3, 3, 4, 5, 2]},
    {'school_class': '4d', 'scores': [3, 3, 3, 3, 3]},
    {'school_class': '4e', 'scores': [3, 4, 5, 5, 2]}
]

average_grades = {value['school_class']: sum(value['scores']) / len(value['scores'])
                  for value in grades_list}

school_average = sum(average_grades.values()) / len(average_grades)
# средний балл по всей школе.
print(school_average)
# средний балл по каждому классу.
for key, value in average_grades.items():
    print(key, value)
