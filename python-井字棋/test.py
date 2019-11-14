import random

list = [[0 for i in range(3)] for j in range(3)]
count = 1
for i in range(3):
    for j in range(3):
        list[i][j] = count
        count = count + 1
for i in range(3):
    print("—————---")
    print("|",list[i][0],"|",list[i][1],"|",list[i][2],"|")
print("—————---")
cp = random.randint(1, 9)
print(cp)