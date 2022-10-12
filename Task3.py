# 3. Создайте программу для игры в 'Крестики-нолики'.

position = list(range(1, 10))

winner_coord = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
                (1, 4, 7), (2, 5, 8), (3, 6, 9),
                (1, 5, 9), (3, 5, 7)]

def draw_board():
    print("-------------")
    for i in range(3):
        print("|", position[0 + i * 3], "|", position[1 + i * 3], "|", position[2 + i * 3], "|")
        print("-------------")

def take_input(playar):
    while True:
        value = input(f"\n\nХод {'1 игрока' if playar == 'X' else '2 игрока'}: ")
        # value = input("Куда поставить " + playar + ' ?')
        if not (value in '1223456789'):
            print("Такой клетки нет на поле. Попробуйте снова.")
            continue
        value = int(value)
        if str(position[value - 1]) in 'XO':
            print("Эта клетка уже занята!")
            continue
        position[value - 1] = playar
        break

def check_win():
    for j in winner_coord:
        if (position[j[0] - 1]) == (position[j[1] - 1]) == (position[j[2] - 1]):
            return position[j[1] - 1]
    else:
        return False
def main():
    count = 0
    while True:
        draw_board()
        if count % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        if count > 3:
            wins = check_win()
            if wins:
                draw_board()
                print(wins, "Выйграл!")
                break
        count += 1
        if count > 8:
            draw_board()
            print("У вас ничья!!")
            break

main()
