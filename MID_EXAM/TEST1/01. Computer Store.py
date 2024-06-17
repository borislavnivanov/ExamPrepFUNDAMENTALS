customer_stat = ''
total = 0.00

while True:
    com = input()
    if com == "special" or com == "regular":
        customer_stat = com
        break

    price = float(com)
    if price < 0:
        print('Invalid price!')
        continue
    else:
        total += price


tax = (total * 1.2) - total

final_price = tax + total

if customer_stat == 'special':
    final_price *= 0.90

if final_price != 0:
    print("Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total:.2f}$\n"
          f"Taxes: {tax:.2f}$\n"
          "-----------\n"
          f"Total price: {final_price:.2f}$")
else:
    print('Invalid order!')