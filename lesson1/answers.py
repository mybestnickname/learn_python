def get_answer(question, answers):
    # проверка типов
    try:
        return answers[question.lower()]
    except KeyError:
        return 'Ответа не существует.'
    except (TypeError, AttributeError):
        return 'get_answer(str, dict)'


answers_dict = {'привет': 'И тебе привет',
                'как дела?': 'Лучше всех',
                'пока': 'Увидимся'
                }
