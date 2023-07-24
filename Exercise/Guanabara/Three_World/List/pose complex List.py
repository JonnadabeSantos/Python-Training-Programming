pose = []
for number in range(0, 5):
    user = int(input(f'Digite {number+1}º numero: '))
    pose.append(user)    

print(f'Esta é a sua lista {pose}')
# print(f'O maior numero foi {max(pose)} ele está na posição {pose.index(max(pose))+1}')
# print(f'O menor numero foi {min(pose)} ele está na posição {pose.index(min(pose))+1}')
print(f'\nO maior numero foi {max(pose)} e esta na posição ', end='')
for p, x in enumerate(pose):
    if x == max(pose):
        print(f'{p+1}', end='...')

print(f'\nO menor numero foi {min(pose)} e esta na posição ', end='')
for p, y in enumerate(pose):
    if y == min(pose):
        print(f'{p+1}', end='...')