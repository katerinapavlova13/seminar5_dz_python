# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

path = "text.txt"

dataTxt = " "
with open(path, "r", encoding="UTF-8") as file:
    dataTxt = file.read()
dataTxt = dataTxt.split()
print(dataTxt)

findTxt = input("Введите текст для проверки: ")

resultTxt = []

for word in dataTxt:
    if findTxt not in word:
        resultTxt.append(word)
print(resultTxt)