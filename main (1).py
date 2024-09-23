import random 

name = input("Введите имя: ")
HERO = {
    "name": name
}

CHRS_HERO = {
    "Сила": random.randint(15, 45),
    "Выносливость": random.randint(15, 45)
}

CHRS_ENEMY = {
    "Сила": random.randint(15, 45),
    "Выносливость": random.randint(15, 45)
}

MODEL_HERO = "Z"
MODEL_ENEMY = "V"

HERO["Хар-ки"] = CHRS_HERO
HERO["Модель"] = MODEL_HERO

MAP = ["0", "0", "0", "0", "0",]
HERO['Position'] = [0][0]
i = 0
MAP[i] = MODEL_HERO

MAP = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

max_enemys = 3
enemys = 0
hero_counter = 0
for y in range(len(MAP)):
    for x in range(5):
        spawn = random.randint(1, 10)
        if spawn in [6, 8]:
            if enemys <= max_enemys-1 and y != 0:
                MAP[y][x] = MODEL_ENEMY
                enemys+=1

MAP[0][2] = MODEL_HERO  
HERO['Position'] = [0,2]
for i in MAP:
    print(''.join(str(i)))
                
            
        

# while MAP.index(MODEL_HERO) < len(MAP) - 1:
#     tmp = i
#     i = MAP.index(MODEL_HERO) + 1
#     MAP[i] = MODEL_HERO
#     MAP[tmp] = "0"
#     print(MAP)
    
# input("Нажмите Enter для продолжения..")

# while MAP.index(MODEL_HERO) > 0:
#     tmp = i
#     i = MAP.index(MODEL_HERO) - 1
#     MAP[i] = MODEL_HERO
#     MAP[tmp] = "0"
#     print(MAP)

HERO['Базовая З'] = 100

inventory = {
    "Броня": 25,
    "Зелье здоровья": 1
}

HERO["И"] = inventory
HERO["Базовый урон"] = 15
HERO["Урон"] = HERO['Базовый урон'] + CHRS_HERO["Сила"] // 3
HERO['З'] = HERO['Базовая З'] + CHRS_HERO['Выносливость'] // 3 + inventory['Броня'] // 5

ENEMY = {
    "Базовая З": 100
}
ENEMY['Базовый урон'] = 10
ENEMY["Урон"] = ENEMY['Базовый урон'] + CHRS_ENEMY["Сила"] // 3
ENEMY['З'] = ENEMY['Базовая З'] + CHRS_ENEMY['Выносливость'] // 3


while True:
    # # while MAP.index(MODEL_HERO) < len(MAP) - 3:
    # #     input("Нажмите Enter для продолжения..")
    # #     tmp = i
    # #     i = MAP.index(MODEL_HERO) + 1
    # #     MAP[i] = MODEL_HERO
    # #     MAP[tmp] = "0"
    # #     print(MAP)
    
    # # while MAP.index(MODEL_ENEMY) > 3:
    # #     input("Нажмите Enter для продолжения..")
    # #     tmp = a
    # #     a = MAP.index(MODEL_ENEMY) - 1
    # #     MAP[a] = MODEL_ENEMY
    # #     MAP[tmp] = "0"
    # #     print(MAP)
    # input("Нажмите Enter для продолжения..")
    # #print(MAP)
    # if MAP.index(MODEL_HERO) == 2:
    #     if MAP.index(MODEL_ENEMY) == 3:
    #         if random.randint(1, 6) in [1, 3, 6]:
    #             ENEMY["З"] = ENEMY["З"] - HERO["Урон"]
    #             print('Вы нанесли', HERO["Урон"], "урона")
    #             HERO['З'] = HERO['З'] - ENEMY['Урон']
    #             print('Вам нанесли', ENEMY["Урон"])
    #             print('У вас осталось', HERO["З"])
    #             if HERO['З'] <= 0:
    #                 print('Вы проиграли')
    #                 break
    #             elif ENEMY['З'] <= 0:
    #                 print('Вы выйграли')
    #                 break
    #         elif random.randint(1, 20) in [20]:
    #             ENEMY["З"] = ENEMY["З"] - HERO["Урон"]*2
    #             if HERO['З'] <= 0:
    #                 print('Вы проиграли')
    #                 break
    #             elif ENEMY['З'] <= 0:
    #                 print('Вы выйграли')
    #                 break
    #         else:
    #             print("Вы промахнулись")
    #             HERO['З'] = HERO['З'] - ENEMY['Урон']
    #             print('Вам нанесли', ENEMY["Урон"])
    #             print('У вас осталось', HERO["З"])
    #             if HERO['З'] <= 0:
    #                 print('Вы проиграли')
    #                 break
    #             elif ENEMY['З'] <= 0:
    #                 print('Вы выйграли')
    #                 break
    move = int(input('--> Ваш ход (1 - влево, 2 - вправо, 3 - вниз, 4 = вверх)'))
    
    
    if move == 1:
        if HERO['Position'][1] > 0:
            MAP[HERO['Position'][0]][HERO['Position'][1]] = 0
            MAP[HERO['Position'][0]][HERO['Position'][1]-1] = MODEL_HERO
            HERO['Position'] = [HERO["Position"][0], HERO['Position'][1]-1]
        else:
            print('СТЕНА!')
    if move == 2:
        if HERO['Position'][1] < 4:
            MAP[HERO['Position'][0]][HERO['Position'][1]] = 0
            MAP[HERO['Position'][0]][HERO['Position'][1]] = MODEL_HERO
            HERO['Position'] = [HERO["Position"][0], HERO['Position'][1]+1]
        else:
            print('СТЕНА!')
    if move == 3:
        if HERO['Position'][0] < 4:
            MAP[HERO['Position'][0]][HERO['Position'][1]] = 0
            MAP[HERO['Position'][0]+1][HERO['Position'][1]] = MODEL_HERO
            HERO['Position'] = [HERO["Position"][0]+1, HERO['Position'][1]]
        else:
            print('СТЕНА!')
    if move == 4:
        if HERO['Position'][0] > 0:
            MAP[HERO['Position'][0]][HERO['Position'][1]] = 0
            MAP[HERO['Position'][0]-1][HERO['Position'][1]] = MODEL_HERO
            HERO['Position'] = [HERO["Position"][0]-1, HERO['Position'][1]]
        else:
            print('СТЕНА!')
    for i in MAP:
        print(''.join(str(i)))














