import os
from function import func

start_file = 'start.txt'
found_file = 'found.txt'
if not os.path.exists(start_file):
    open(start_file, 'a').close()


def read_start(file_name=start_file):
    with open(file_name, 'r') as f:
        start = f.read()
        try:
            n = int(start.strip())
        except:
            n = 1
        f.close()
    return n


def write_start(n, file_name=start_file):
    with open(file_name, 'w') as f:
        f.write(str(n))
        f.close()


def store_found(n, file_name=found_file):
    if not os.path.exists(found_file):
        open(found_file, 'a').close()
    with open(file_name, 'wa') as f:
        f.write(str(n))
        f.close()


def continuous_finding():
    start_number = read_start()
    n = start_number
    while True:
        if not func(n):
            store_found(n)
            print(f'Found {n}')
        if n % 1000 == 0:
            write_start(n)
            print(f'Currently, until {n} is good')
        if n % 100000 == 0:
            if not os.path.exists('log'):
                os.makedirs('log')
            write_start(n, f'log/Now-{n}.txt')
        n += 1


if __name__ == '__main__':
    continuous_finding()
