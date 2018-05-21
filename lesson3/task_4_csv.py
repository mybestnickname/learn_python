import os
import sys
import io
import csv

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

file_path = os.path.join(sys.path[0], 'export.csv')

list_of_answer_dicts = [
    {'question': 'привет', 'response': 'И тебе привет'},
    {'question': 'как дела?', 'response': 'Лучше всех'},
    {'question': 'пока', 'response': 'Увидимся'}
]

with open(file_path, 'w', encoding='utf-8') as f:
    fields = ['question', 'response']
    writer = csv.DictWriter(f, fields, delimiter=';')
    writer.writeheader()
    for chat_line in list_of_answer_dicts:
        writer.writerow(chat_line)
