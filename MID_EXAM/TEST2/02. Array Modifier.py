def swap(lst: list, ind_1: int, ind_2: int) -> list:
    lst[ind_1], lst[ind_2] = lst[ind_2], lst[ind_1]
    return lst


def multiply(num_1: int, num_2: int) -> int:
    return num_1 * num_2


def decrease(lst: list) -> list:
    return list(x - 1 for x in lst)


number_lst = list(map(int, input().split()))

while True:
    com = input().split(' ')
    if com[0] == 'end':
        break
    elif com[0] == 'swap':
        number_lst = swap(number_lst, int(com[1]), int(com[2]))
    elif com[0] == 'multiply':
        number_lst[int(com[1])] = multiply(number_lst[int(com[1])], number_lst[int(com[2])])
    elif com[0] == 'decrease':
        number_lst = decrease(number_lst)

print(', '.join(str(x) for x in number_lst))