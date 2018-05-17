def get_summ(one, two, delimeter=' '):
    return (str(one) + str(delimeter) + str(two)).upper()


if __name__ == "__main__":
    print(get_summ('first', 'second', delimeter='___'))
