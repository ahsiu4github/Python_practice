import random
r = random.randint(1, 100)
#print(r)

while True:
    num = input('Guess number(1-100): ')
    num = int(num)
    if num < r:
        print('Higher')
    elif num > r:
        print('Lower')
    else:
        print('you got it')
        break
