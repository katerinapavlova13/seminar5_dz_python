# 2. Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

from random import randint

quantity_candy = 150
#quantity_candy = int(input("Введите колличество конфет: "))

print("-------------------- CANDY GAME ----------------------")

print(f"На столе лежит {quantity_candy} конфет. Игроки по очереди берут с стола конфеты."
      "За один ход можно забрать не более чем 28 конфет."
      "Выйграет тот, кто заберет последнии конфеты!")

player_1 = input("Введите имя первого игрока: ")
player_2 = input("Введите имя второго игрока: ")

print("Монета решить кто ходит первый!")

stroke = randint(1, 2)
if stroke:
    print(f'Первый ходит: {player_1}')
else:
    print(f'Первый ходит: {player_2}')

def Input(name):
    move = int(input(f'{name}, сколько конфет возьмете?  '))
    while move < 1 or move > 28:
        move = int(input(f'{name}, вы взяли конфет больше позволеного! '
                         f'Попробуйте снова: '))
    return move

def Print(name, i, count, quantity_candy):
    print(f'{name}, взял {i}, теперь у него {count} конфет. На столе осталось {quantity_candy} конфеты.')

count1 = 0
count2 = 0

while quantity_candy > 28:
    if stroke:
        i = Input(player_1)
        count1 += i
        quantity_candy -= i
        stroke = False
        Print(player_1, i, count1, quantity_candy)
    else:
        i = Input(player_2)
        count2 += i
        quantity_candy -= i
        stroke = True
        Print(player_2, i, count2, quantity_candy)

if stroke:
    print(f'Выйграл {player_1}! Теперь все конфеты твои!')
else:
    print(f'Выйграл {player_2}! Теперь все конфеты твои!')




