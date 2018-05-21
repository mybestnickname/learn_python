def string_comp(first_str, second_str):
    try:
        if first_str == second_str:
            return 1
        elif len(first_str) > len(second_str):
            return 2
        elif second_str == 'learn':
            return 3
    except TypeError:
        print('string_comp(str, str)')
