money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months_without_debt = 0
while spend < money_capital:
    if months_without_debt == 0:
        money_capital += salary
        money_capital -= spend
        months_without_debt += 1
    else:
        months_without_debt+= 1
        money_capital += salary
        money_capital -= spend
        spend *= (1 + increase)




# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", months_without_debt )