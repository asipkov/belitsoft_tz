list_symbol = ['a', 'b', 'c', 'c', 'a']


def first_duplicate():
    duplicate = []
    while True:
        for index, el in enumerate(list_symbol[:-1]):
            if el == list_symbol[index + 1]:
                duplicate.append(el)
            if duplicate:
                break
            else:
                continue
        return duplicate


result = first_duplicate()
print(result)
