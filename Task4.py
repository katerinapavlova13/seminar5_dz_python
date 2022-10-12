# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

from collections import Counter

path = "task4_enc.txt"
path2 = 'task4_dec.txt'

dataTxt = ' '
dataTxt2 = ' '

with open(path, "r") as file:
    dataTxt = file.read()
    dataTxt = dataTxt.split()

with open(path2, "r") as file:
    dataTxt2 = file.read()
    dataTxt2 = dataTxt2.split()

def encode_rle(dataTxt):
    encoding = ''
    prev_char = ''
    count = 1
    if not dataTxt:
        return ''
    for char in dataTxt:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
        return encoding

print(dataTxt)
res_enc = encode_rle(dataTxt)
print(res_enc)

def decode_rle(dataTxt2):
    decode = ''
    count = ''
    for check in dataTxt2:
        if check.isdigit():
            count += check
        else:
            decode += check * int(count)
            count = ''
    return decode


print(dataTxt2)
res_dec = decode_rle(dataTxt2)
print(res_dec)

with open('Task4_res.txt', 'w') as f:
    f.write(res_enc + '\n')
    f.write(res_dec + '\n')


