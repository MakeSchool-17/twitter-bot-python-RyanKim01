table = ['a', 1, 'b', 2, 'c', 3]


def get(key, array):
    value = None
    for index, item in enumerate(array):
        if item == key:
            value = array[index + 1]
            break
    return value


print(get('b', table))
print(hash("age") % 23)
