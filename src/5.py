import random

def get_random_integer(a, b):
    return random.randint(a, b)

def get_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    for i in range(length):
        result += random.choice(letters)
    return result

def get_random_boolean():
    return random.choice([True, False])

def get_random_tuple(length):
    return tuple(random.sample(range(10), length))

def get_random_list(length):
    return [random.randint(0, 10) for _ in range(length)]

def get_random_dictionary():
    dictionary = {}
    for i in range(5):
        key = random.randint(0, 10)
        value = random.randint(0, 10)
        dictionary[key] = value
    return dictionary

def get_random_set():
    return set(random.sample(range(10), 5))