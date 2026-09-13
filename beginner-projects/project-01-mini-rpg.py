import random
player_health = 100
potions = 3
enemy_potions = 3
exp = 0

enemy_health = 80
while player_health > 0 and enemy_health > 0:
    print(f'Your HP: {player_health} \nEnemy HP: {enemy_health} \nPotions: {potions}')
    print('1. Attack \n2. Heavy Attack \n3. Heal ')
    choice = input('Enter Command(1-3): ')
    if choice == '1':
        damage = random.randint(10, 20)
        enemy_health -= damage
        print(f'you\'e dealt {damage}')
        enemy_damage = random.randint(5, 15)
        player_health -= enemy_damage
        print(f'kaloy dealt {enemy_damage} to you')
    elif choice == '2':
        generate = random.randint(1, 100)
        if generate <= 60:
            damage = random.randint(20, 35)
            enemy_health -= damage
            print(f'You\'ve dealt {damage} to kaloy')
            enemy_damage = random.randint(5, 15)
            player_health -= enemy_damage
            print(f'kaloy dealt {enemy_damage} to you')
        else:
            print('Attack miss \nDealt 0 damage')
            enemy_damage = random.randint(5, 15)
            player_health -= enemy_damage
            print(f'kaloy dealt {enemy_damage} to you')
    elif choice == '3':
        if potions > 0 and enemy_potions > 0:
            restore = random.randint(15, 30)
            player_health += restore
            potions -= 1
            if player_health > 100:
                player_health = 100
            restore_enemy_hp = random.randint(10,25)
            enemy_health += restore_enemy_hp
            enemy_potions -= 1
            if enemy_health > 100:
                enemy_health = 100
            print (f'Restore {restore} health, {potions} potions left')
        else:
            print('No potions to use')
    else:
        print('Invalid Choice')

    if enemy_health <= 0:
        print('You defeated kaloy')
        break

    if player_health <= 0:
        print('Your DEAD aahhhhh')
    elif player_health < 25:
        print('Warning Health Below 25 Use Potions now')
    else:
        print('Kaya pa')
    

