elements = input().strip().split(' ')
moves = 0

while len(elements) > 0:
    com = input().split(' ')
    if com[0] == 'end':
        break
    moves += 1
    el_1, el_2 = int(com[0]), int(com[1])
    if not 0 <= el_1 < len(elements) or not 0 <= el_2 < len(elements) or el_1 == el_2:
        mid = len(elements) // 2
        a = f'-{moves}a'
        elements.insert(mid, a)
        elements.insert(mid, a)
        print('Invalid input! Adding additional elements to the board')
        continue

    if elements[el_1] == elements[el_2]:
        print(f'Congrats! You have found matching elements - {elements[el_1]}!')
        elements.pop(max(el_2, el_1))
        elements.pop(min(el_2, el_1))

    elif elements[el_1] != elements[el_2]:
        print('Try again!')

if len(elements) == 0:
    print(f'You have won in {moves} turns!')
else:
    print(f'Sorry you lose :(\n'
          f'{" ".join(str(x) for x in elements)}')
