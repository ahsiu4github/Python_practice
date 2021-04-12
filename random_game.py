import random
r = random.randint(1, 100)
print(r)
count = 0

while True:
    num = input('Guess number(1-100): ')
    num = int(num)
    count += 1
    if num < r:
        print('Higher')
    elif num > r:
        print('Lower')
    else:
        print('you got it')
        print('This is your ', count, ' try')
        break
    print('This is your ', count, ' try')
