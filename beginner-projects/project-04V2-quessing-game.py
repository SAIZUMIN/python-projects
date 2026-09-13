import random
attempt = 0

number = 7
while True:
    guess = int(input('Enter guess number(1-100): '))
    attempt += 1
    if guess < number:
        print('--------------------------------------------')
        print('Guess To LOW!')
        print(f'Attempts : {attempt}')  
    elif guess > number:
        print('--------------------------------------------')
        print('Guess to HIGH!')
        print(f'Attempts : {attempt}')  

    if guess == number:
        print('CORRECT!!!')
        attempt = 0
        number = random.randint(1,100)
        enter = input('Do you want to play again(Y/N): ')
        if enter.upper() != 'Y':
            print('Thank you! for playing.')
            break
    elif guess != number and attempt >=7:
        attempt = 0
        print('Run out of attempts')
        print(f'Number: {number}')
        number = random.randint(1,100)
        enter = input('Do you want to play again(Y/N): ')
        if enter.upper() != 'Y':
            print('Thank you! for playing.')
            break
   

