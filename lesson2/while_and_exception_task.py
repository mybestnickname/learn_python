# import io
# import sys
# import traceback
# мой костыль для вывода кирилицы в atom
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

names_list = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
answers_dict = {'привет': 'И тебе привет',
                'как дела?': 'Лучше всех',
                'пока': 'Увидимся'
                }


def find_person(name):
    while len(names_list):
        if names_list.pop() == name:
            print("{} найден(а)".format(name))
            break
    else:
        print("{} не найден(а)".format(name))


def get_answer(question, answers):
    try:
        return answers[question.lower()]
    except KeyError:
        return 'Ответа не существует.'
    except (TypeError, AttributeError):
        return 'get_answer(str, dict)'


def ask_user():
    user_response = ''
    try:
        while user_response.lower() != 'хорошо':
            user_response = input('Как дела? ')
        user_response = input('Пообщаемся? ')
        if user_response.lower() in ['y', 'yes', 'да', 'д']:
            while 1:
                user_response = input('User input: ')
                if user_response.lower() == 'пока!':
                    print(get_answer('пока', answers_dict))
                    break
                print(get_answer(user_response, answers_dict))
        else:
            print(':(')
    except (EOFError, KeyboardInterrupt):
        # print(traceback.format_exc())
        print('Ушёл по английски!')


if __name__ == "__main__":
    find_person('Валера')
    ask_user()
