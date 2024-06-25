def calculate(amount):
    quarters = amount // 25
    amount -= quarters * 25

    dimes = amount // 10
    amount -= dimes * 10

    nickels = amount // 5
    amount -= nickels * 5

    pennies = amount // 1

    sumcoins = quarters + dimes + nickels + pennies

    return int(sumcoins)

while True:
    change = 37.5
    if change > 0:
        break
change = change * 100
coins = calculate(change)
print(f"{coins}")
