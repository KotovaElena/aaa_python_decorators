import sys


def redirect_output(filepath):
    def out_wrapper(function):
        def in_wrapper():
            tmp_stdout = sys.stdout
            f = open(filepath, "w")
            sys.stdout = f
            function()
            f.close()
            sys.stdout = tmp_stdout
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
