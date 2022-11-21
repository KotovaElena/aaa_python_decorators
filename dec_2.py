import sys
from datetime import datetime

original_write = sys.stdout.write


def my_write(string_text):
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if string_text != '\n':
        return original_write(f'[{current_datetime}]: {string_text} \n')


def timed_output(function):
    def wrapper(*args, **kwargs):
        sys.stdout.write = my_write
        function(*args, **kwargs)
        sys.stdout.write = original_write
    return wrapper


@timed_output
def print_greeting(name):
    print(f'Hello, {name}!')


if __name__ == '__main__':
    print_greeting("Nikita")
