import random
import json
import re
import time
import sys
import os


name = 'Default'
money = int(100)
Cashback = int(0)
credit_status = int(0)
game_over = int(1)
win = int(0)

with open('player.json', 'r', encoding='utf-8') as x:
    save = json.load(x)  # Создание, либо загрузка сохранения
    name = save["name"]

savedata = ("savedata\\"+name+".json")

with open(savedata, 'r', encoding='utf-8') as x:
    save = json.load(x)                                                                                             # Создание, либо загрузка сохранения
    money = save["client_cash"]
    Cashback = save["client_cashback"]
    credit_status = save["credit_status"]


while game_over != 0:
    while 0 < money < 2001:
        if credit_status == int(1) and money >= int(1400):
            print("Пришло время возвращать долги. 1300$ списаны с твоего счета. Приятно было с вами работать.")
            credit_status = 0
            money = money - int(1300)
        print(name, "У вас на счету -", money, "Введите число от 1 до 10, что бы играть:")
        x = input()
        y = int(random.randint(1, 10))
        print(y)
        if not re.findall(r'\D', x):
            if int(x) == y:
                print('Вы выиграли 100$')
                money = money + int(100)
                Cashback = int(0)
            else:
                print('Как жаль, но вы проиграли 10$')
                money = money - int(10)
                Cashback = Cashback + int(1)
                if Cashback == int(8):
                    money = money + int(10)
                    print("Не отчаивайтесь, вот вам 10$, что бы отыграться! Вперед!")
                    Cashback = int(0)
            print("Продолжаем играть? y/n")
            get_out = str(input())
            if get_out == 'y' or get_out == 'Y':
                print("Отлично!")
            elif get_out == 'n' or get_out == 'N':
                with open(savedata, 'w', encoding='utf-8') as outfile:
                    json.dump({
                        "client_cash": money,
                        "client_cashback": Cashback,
                        "credit_status": credit_status,
                    }, outfile)
                print("Всегда будем вам рады в 'Азино'!")
                sys.exit(0)
            else:
                print('Неверный формат данных')
        else:
            print('Неверный формат данных')
    if money <= int(0):
        print("Вы банкрот! Хотите ли вы взять кредит в 'АзиноИнвестБанке' и отыграться? Нажмите y, что бы согласится!")
        credit = str(input())
        if credit == 'y' or credit == 'Y':
            if credit_status == 0:
                print("Вы взяли кредит на 300$. Вы должны банку вернуть 1300$ до конца дня!")
                money = int(300)
                credit_status = int(1)
            else:
                print("Вы и так должны банку 1300$! оглядывайтесь по сторонам, когда будете идти домой!")
                time.sleep(2)
                print("Вы банкрот! Убирайтесь с казино!")
                game_over = int(0)
        else:
            print("Вы банкрот! Убирайтесь с казино!")
            game_over = int(0)
    elif money > int(2000):
        print("Вы слишком много выиграли! Убирайтесь с казино!")
        win = int(1)
        game_over = int(0)
time.sleep(2)
if win == int(1):
    print("Вас выгнали с казино, но выплатили ваш выиграш. Возможно, это лучшее развитие событий в Азино...")
    sys.exit(0)
elif credit_status == 0:
    print("Вы проиграли все свои деньги, но хотя бы не влезли в долги.")
    print("Возможно, это не худшее развитие событий в Азино...")
    sys.exit(0)
elif credit_status == 1:
    print("Когда вас выгнали из Азино с долгом в 1300$")
    print("Вы и подумать не могли, что уже сейчас вашу семью вывозят на рабский труд в Мексику.")
    print("Вас почему то трогать не стали, Правда деньги вы все равно должны вернуть. ")
    print("Возможно, это худшее развитие событий в Азино...")
