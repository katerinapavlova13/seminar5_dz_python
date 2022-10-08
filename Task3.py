# 3. Создайте программу для игры в 'Крестики-нолики'.

position = []
for i in range(1,10):
    position.append(i)

sign = "O"

moves = []
def printField(position):
    print(f"{position[0]:^5}|{position[1]:^5}|{position[2]:^5}")
    print("-----------------")
    print(f"{position[3]:^5}|{position[4]:^5}|{position[5]:^5}")
    print("-----------------")
    print(f"{position[6]:^5}|{position[7]:^5}|{position[8]:^5}")

while True:

    while True:
        printField(position)
        index = int(input(f"\n\nХод {'игрока' if sign == 'X' else 'противника'}: "))
        if index in moves:
            print("Эта клетка уже занята")
        else:
            if sign == "O":
                sign = "X"
            else:
                sign = "O"
            moves.append(index)
            position[index - 1] = sign
            break