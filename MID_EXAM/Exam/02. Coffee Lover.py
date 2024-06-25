coffee_list = input().split(' ')
num_com = int(input())

for _ in range(num_com):
    com = input().split(' ')

    if com[0] == 'Include':
        coffee_list.append(com[1])
    elif com[0] == 'Reverse':
        coffee_list.reverse()
    elif com[0] == 'Remove':
        if int(int(com[2])) <= len(coffee_list):
            if com[1] == 'first':
                for i in range(int(com[2])):
                    coffee_list.pop(0)
            else:
                for i in range(int(com[2])):
                    del coffee_list[-1]
    elif com[0] == 'Prefer':
        if 0 <= int(com[1]) < len(coffee_list) and 0 <= int(com[2]) < len(coffee_list):
            coffee_list[int(com[1])], coffee_list[int(com[2])] = coffee_list[int(com[2])], coffee_list[int(com[1])]

print('Coffees:')
print(' '.join(coffee_list))
