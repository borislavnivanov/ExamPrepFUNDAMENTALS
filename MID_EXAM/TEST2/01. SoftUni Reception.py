empl_efficiency_coef = []
for i in range(3):
    empl_efficiency_coef.append(int(input()))

number_of_stud = int(input())

hours = 0
answers = sum(empl_efficiency_coef)
while number_of_stud > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    number_of_stud -= answers

print(f'Time needed: {hours}h.')