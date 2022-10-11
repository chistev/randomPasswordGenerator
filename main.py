import random

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
password_length = int

while True:
    try:
        password_length = int(input('What length of password would you like to generate: '))
        break
    except ValueError:
        print('invalid input')
        continue

print('\nyour generated password is: ')
for password in range(password_length):
    passwords = ''
    passwords += random.choice(characters)

    print(passwords, end='')  # end prints out the results of the loop on one line
