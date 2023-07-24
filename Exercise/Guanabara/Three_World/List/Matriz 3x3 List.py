temp = []
l1 = []
l2 = []
l3 = []

for Number in range(0,3):
    temp.append(int(input(f'Digite o [{Number}, 0]: ')))
    l1.append(temp[:])
    temp.clear()

for Number in range(0,3):
    temp.append(int(input(f'Digite o [{Number}, 1]: ')))
    l2.append(temp[:])
    temp.clear()

for Number in range(0,3):
    temp.append(int(input(f'Digite o [{Number}, 2]: ')))
    l3.append(temp[:])
    temp.clear()

print(l1)
print(l2)
print(l3)