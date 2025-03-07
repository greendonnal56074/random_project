import random

def get_random_number(max_value):
    return random.randint(1, max_value)

def get_random_color():
    colors = ['red', 'blue', 'green', 'yellow']
    return random.choice(colors)

def get_random_boolean():
    return bool(random.getrandbits(1))

def get_random_string():
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(10))

def get_random_list(max_size, max_value):
    return [random.randint(1, max_value) for i in range(max_size)]
