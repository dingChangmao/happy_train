import random
"""
学习了本代码以后买彩票妈妈再也不用担心我纠结了，那么来一发吗
"""
temp = [i+1 for i in range(35)]
random.shuffle(temp)

i = 0
list = []
while i<7:
    list.append(temp[i])
    i = i+1

list.sort()

print('\033[0;31;;1m')

print(*list[0:6], end="")

print('\033[0;34;;1m', end=" ")

print(list[-1])
