experience_needed = float(input())
battles = int(input())

gained_experience = 0.0
battles_fought = 0

for i in range(1, battles + 1):
    exp = float(input())

    if i % 15 == 0:
        gained_experience += exp * 1.05
    elif i % 5 == 0:
        gained_experience += exp * 0.90
    elif i % 3 == 0:
        gained_experience += exp * 1.15
    else:
        gained_experience += exp

    battles_fought += 1

    if gained_experience >= experience_needed:
        break

if gained_experience >= experience_needed:
    print(f'Player successfully collected his needed experience for {battles_fought} battles.')
else:
    print(f'Player was not able to collect the needed experience, {experience_needed - gained_experience:.2f} more needed.')
