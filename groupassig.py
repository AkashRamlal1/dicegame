import random

HPplayer = 20
HPmonster = 20
playerDamage = 0
monsterDamage = 0
dice = 0

def rules():
    print('welkom bij monster dice het spel is simpel het monster en de hebben 20 hp\n. als je een 1 of 2 rolt met de dobbelsteen ontvangt het monster schade\n. als je een 3 of 4 rolt ontvang je 2 schade. als je een 5 of 6 rolt krijgt het monster kritieke schade en verliest het 4 hp ')

def diceroll():
    global dice
    dice = random.randint(1, 6)

  

def TheFight(monster,player):
    global dice,playerDamage,monsterDamage
    rules()

    while monster > 0 or player > 0:
        print('het monster heeft nog ',monster," hp")
        print(" de speler heeft ",player," hp")
        action = input(' wil je aanvallen of wil je stoppen ')


        if action == "aanvallen":
            diceroll()
            print("gerold: ", dice)

            if dice == 1 or dice == 2:
                print('je aanval deed 2 dmg')
                playerDamage = 2
                monster = monster - playerDamage 
            elif dice == 3 or dice == 4:
                print(' oei je hebt aanval heeft het monster niet geraakt je verliest 3 hp')
                monsterDamage = 3
                player =  player - monsterDamage

            elif dice == 5 or dice  == 6:
                print('je hebt een kritieke schade aan het monster toegebracht het monster verliest 4 hp')
                playerDamage = 4
                monster = monster - playerDamage

        elif action == "stop":
            break
    if player <= 0: 
        print("Game over, that sucks ")
    elif monster <= 0:
        print("gefeliciteerd koop een taart en vier het ")




        
TheFight(HPmonster,HPplayer)