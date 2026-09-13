score = 0
while True:
    print('=======QUESTION GAME=======')
    print('What does CPU stand for?')
    print('A. Central Processing Unit')
    print('B. Computer Processing Utility')
    print('C. Central Program Unit')
    print('D. Computer Personal Unit')
    answer1 = input('Enter Answer:  ').upper()
    if answer1 == 'A':
        score += 1
        print('Correct!')
    else:
        print('Wrong!')
    print('Which of these is used to store data permanently?')
    print('A. RAM')
    print('B. CPU')
    print('C. SSD')
    print('D. Cache')
    answer2 = input('Enter Answer: ').upper()
    if answer2 == 'C':
        score += 1
        print('Correct!')
    else:
        print('Wrong!')
    print('What does HTML stand for?')
    print('A. HyperText Markup Language')
    print('B. HighText Machine Language')
    print('C. Hyperlink Text Management Language')
    print('D. Home Tool Markup Language')
    answer3 = input('Enter Answer:  ').upper()
    if answer3 == 'A':
        score += 1
        print('------------------------------------------------')
        print('Correct!')
    else:
        print('------------------------------------------------')
        print('Wrong!')
    print('Which protocol is connection-oriented and reliable?')
    print('A. UDP')
    print('B. HTTP')
    print('C. TCP')
    print('D. FTP')
    answer4 = input('Enter Answer: ').upper()
    if answer4 == 'C':
        score += 1
        print('------------------------------------------------')
        print('Correct!')
    else:
        print('------------------------------------------------')
        print('Wrong!')

    print('Which programming language is commonly used for web page interactivity?')
    print('A. JavaScript')
    print('B. SQL')
    print('C. HTML')
    print('D. CSS')    
    answer5 = input('Enter Answer: ').upper()
    if answer5 == 'A':
        score += 1
        print('------------------------------------------------')
        print('Correct!')
    else:
        print('------------------------------------------------')
        print('Wrong!')

    print('==========SCORE==========')
    if score == 5:
        print('Excellent')
    elif score == 4:
        print('Very Good!')
    elif score == 3:
        print('Good!')
    elif score == 2:
        print('Needs improvements!')
    else:
        print('Keep practicing')
    print(f'Score: {score}/5')
    enter = input('Do you want to continue?(Y/N):  ')
    score = 0
    if enter.upper() != 'Y':
        print('Thank you for Playing. Goodbye!')
        break


