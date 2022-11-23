import sys
from datetime import datetime

original_write = sys.stdout.write


def my_write(string_text):
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if string_text != '\n':
        return original_write(f'[{current_datetime}]: {string_text} \n')


if __name__ == '__main__':
    print('1, 2, 3')
    sys.stdout.write = my_write
    print('1, 2, 3')
    sys.stdout.write = original_write
    print('1, 2, 3')
