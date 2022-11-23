import sys
from functools import wraps


def redirect_output(filepath):
    def out_wrapper(function):
        @wraps(function)
        def in_wrapper(*args, **kwargs):
            tmp_stdout = sys.stdout
            with open(filepath, "w") as f:
                sys.stdout = f
                result = function(*args, **kwargs)
            sys.stdout = tmp_stdout
            return result
        return in_wrapper
    return out_wrapper


@redirect_output('function_output.txt')
def calculate():
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    calculate()
