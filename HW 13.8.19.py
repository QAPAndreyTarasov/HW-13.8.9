Tickets = int(input("При покупки от 4х билетов действует скидка 10% от стоимости всего заказа.\n"
                    "Введите сколько билетов желаете приобрести: "))

price = 0
for i in range(Tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        price = price + 0
    elif 18 <= age < 25:
        price = price + 990
    else:
        price = price + 1390
if Tickets > 3:
    price = price * 0.9

print("Сумма к оплате равна- " + str(round(price)) + " " "рублей")