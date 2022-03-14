

def calc(numbers: str)-> None:
    numbers = list(map(int, numbers.split(' ')))
    print(numbers[0] + (numbers[3] - numbers[1])* numbers[2])
    #print(int(numbers[0]) + )

def calc2(*num) -> None:
    print(int(num[0] + (num[3] - num[1]) * num[2]))

def generate_numbers():
    with open('test_numbers', 'w') as f:
        f.write('100 10 12 15\n')
        f.write('100 10 12 1')
        f.close()

if __name__ == '__main__':
    generate_numbers()
    with open('test_numbers', 'r') as f:
        for line in f.read():
            print(line)
            calc(line)
        f.close()
    #calc2(100 10 12 15)

