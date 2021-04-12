password = 'a123456'
i = 2
while True:
    user_input = input('Please input password')
    if user_input == password:
        print('Log in success!')
        break
    elif user_input != password and i > 0:
        print("Error, you have ", i, 'chance.')
        i += 1
    else:
        print('No chance!')
        break
