'''
уровень персонажа больше 100 и здороье больше 50
OR
броня больше 60 или здоровье больше 100
OR
больше 600 монет и больше 5 предметов в инвентаре
OR
больше 20 предметов в  инвентаре
'''

player = {"level": 50 ,"health": 80, "money": 700, "inventory": ["sword", "apple", 'arrow', 'bow', 'water', 'cola' ], "armor": 70}


if player["level"]>100 and player['health']>50 or player['armor']>60 and player['health']>100 or player['money']>600 and len(player['inventory'])>5 or player['inventory']>20:
    print('Вы допущены к уровню')
else:
    print("No access.")
