import random
player_HP = 100
enemy_HP = 100
player_potions = 3


while True:
    while enemy_HP > 0 and player_HP > 0:
        print('==========BATTLE==========')
        print(f'Player HP: {player_HP}')
        print(f'Enemy HP: {enemy_HP}')
        print(f'Potions: {player_potions}')
        
        print('1. Attack')
        print('2. Heal')
        print('--------------------------')
        choice = input('Choose move:  ')
        if choice == '1':
            damage = random.randint(10, 25)
            enemy_HP -= damage

            enemy_damage = random.randint(5, 20)
            player_HP -= enemy_damage

            print(f'You dealt {damage} damage!')
            print(f'Enemy dealt {enemy_damage} damage!')
        elif choice == '2':
            if player_potions > 0:
                player_potions -= 1

                restore = random.randint(15, 30)
                player_HP += restore
                
                enemy_damage = random.randint(5, 20)
                player_HP -= enemy_damage
                print(f'Healed {restore} HP')
                print(f'Enemy dealt {enemy_damage} damage')
                if player_HP > 100:
                     player_HP = 100
            else:
                 print('Run out of potions')
                 enemy_damage = random.randint(5, 20)
                 player_HP -= enemy_damage
                 print(f'Enemy dealt {enemy_damage} damage')
        else:
             print('Invalid choice')
    if enemy_HP <= 0 and player_HP <= 0:
            print('Draw')
    elif player_HP <= 0:
            print('You lose!!!')
    elif enemy_HP <= 0:
            print('You win!!!')
    enter = input('Do you want to play again?(Y/N): ')
    enemy_HP = 100
    player_HP = 100
    player_potions = 3
    if enter.upper() != 'Y':
        print('Thank you for playing. Goodbye!')
        break
    






