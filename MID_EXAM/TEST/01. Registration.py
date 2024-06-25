def letters(lst: list, com: str) -> list:
    if com == 'Lower':
        final_list = [str(x).lower() for x in lst]
    else:
        final_list = [str(x).upper() for x in lst]
    print(''.join(final_list))
    return final_list


def reverse(lst: list, start_ind: int, end_ind: int) -> None:
    if 0 < start_ind < len(lst) and 0 < end_ind < len(lst):
        print(''.join(lst[end_ind:start_ind - 1:-1]))


def substring(lst: list, sub_string: str) -> list:
    text = ''.join(lst)
    if sub_string not in text:
        print(f'The username {text} doesn\'t contain {sub_string}.')
    else:
        new_text = text.replace(sub_string, '', 1)
        print(new_text)
        return [x for x in new_text]


def replace(lst: list, char: str) -> list:
    new_lst = [x if x != char else '-' for x in lst]
    print(''.join(new_lst))
    return new_lst


def is_valid(lst: list, char: str) -> None:
    if char not in str(lst):
        print(f'{char} must be contained in your username.')
    else:
        print('Valid username.')


input_list = [x for x in input()]

while True:
    command = input().split()
    if command[0] == 'Registration':
        break
    elif command[0] == 'Letters':
        input_list = letters(input_list, command[1])
    elif command[0] == 'Reverse':
        reverse(input_list, int(command[1]), int(command[2]))
    elif command[0] == 'Substring':
        input_list = substring(input_list, command[1])
    elif command[0] == 'Replace':
        input_list = replace(input_list, command[1])
    elif command[0] == 'IsValid':
        is_valid(input_list, command[1])
