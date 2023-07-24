pose = []
for number in range(0, 5):
    user = int(input(f'Digite {number+1}º numero: '))
    pose.append(user)    

print(f'Esta é a sua lista {pose}')
print(f'O maior numero foi {max(pose)} ele está na posição {pose.index(max(pose))+1}')
print(f'O menor numero foi {min(pose)} ele está na posição {pose.index(min(pose))+1}')