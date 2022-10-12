# 2. Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'

from random import randint

print("На столе лежит конфеты. Игроки по очереди берут конфеты."
      "За один ход нельзя взять больше 28 конфет."
      "Выйграет тот, кто заберет последнии конфеты!")
def Print(name, i, count, quantity_candy):
    print(f'Ходил {name}, взял {i}, теперь у него {count}. Осталось {quantity_candy} конфет')

player_1 = input("Введите имя первого игрока: ")
player_2 = input("Введите имя второго игрока: ")

stroke = randint(1, 2)
if stroke:
    print(f'Первый ходит {player_1}')
else:
    print(f'Первый ходит {player_2}')

quantity_candy = int(input("Введите колличество конфет: "))

def Input(name):
    move = int(input(f'{name}, сколько конфет возьмете? : '))
    while move < 1 or move > 28:
        move = int(input(f'{name}, вы взяли конфет больше позволеного!'))
    return move

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


