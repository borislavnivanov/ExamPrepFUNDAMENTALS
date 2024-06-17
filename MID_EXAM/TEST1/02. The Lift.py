CAR_MAX_VALUE = 4

people_waiting = int(input())
car_status = [int(x) for x in input().split(' ')]

for i in range(len(car_status)):
    if people_waiting > 0:
        if car_status[i] < CAR_MAX_VALUE:
            if people_waiting - (CAR_MAX_VALUE - car_status[i]) > 0:
                people_waiting -= CAR_MAX_VALUE - car_status[i]
                car_status[i] += CAR_MAX_VALUE - car_status[i]
            else:
                car_status[i] += people_waiting
                people_waiting = 0

if people_waiting == 0 and sum(car_status) < len(car_status) * CAR_MAX_VALUE:
    print('The lift has empty spots!')
elif people_waiting > 0 and sum(car_status) == len(car_status) * CAR_MAX_VALUE:
    print(f'There isn\'t enough space! {people_waiting} people in a queue!')
print(' '.join(str(x) for x in car_status))