import random
import time
import sys
import json
import os.path

money = int(100)

print("Представьтесь, пожалуйста!")
name = str(input())

savedata = ("savedata\\"+name+".json")                                                                                  #Проверка на наличие сохранения
save_not_null = os.path.isfile(savedata)


if save_not_null is True:
    with open(savedata, 'r', encoding='utf-8') as x:
        save = json.load(x)                                                                                             # Создание, либо загрузка сохранения
        money = save['cash']
elif save_not_null is False:
    with open(savedata, 'w', encoding='utf-8') as outfile:
        json.dump({
            "cash": money,
        }, outfile)


with open('enemy.json', 'r', encoding='utf-8') as f:                                                                    #Загрузка оппонентов
    text = json.load(f)
enemy = random.randint(0,8)
enemy_name = text[enemy]['name']
enemy_cash = text[enemy]['cash']

print("Добро пожаловать в 'Кости'! Имя вашего соперника:", enemy_name)
time.sleep(1)
print("Правила просты - вы, и ваш оппонент кидаете кости по очереди.")
print("После каждого броска вы выбираете, у кого из вас сумма костей будет больше.")
print("Угадали - ваша ставка удваивается.")
end_game = 0
your_turn = 1


while end_game == 0:

    if 10 > money:
        print("Вы банкрот! Отныне 'Кости' не для вас!")
        end_game = 1
        break

    if your_turn == 1:
        print(name, "Какую ставку вы хотите сделать? у вас на счету сейчас -", str(money)+"$. У оппонента -", enemy_cash)
        rate = int(input())
        if rate > money or rate < 10:
            print("Вы не можете столько поставить, сделайте ставку меньше!")
            continue
        if rate > enemy_cash or rate < 10:
            print(enemy_name,"не может столько поставить, Он выбывает из игры, вам будет подобран новый соперник")
            enemy_status = 0
            while enemy_status == 0:
                new_enemy = random.randint(0, 8)
                if new_enemy != enemy:
                    enemy_name = text[new_enemy]['name']
                    enemy_cash = text[new_enemy]['cash']
                    enemy_status = 1
                    print("Ваш новый оппонент:", enemy_name)
                else:
                    new_enemy = random.randint(0, 8)
                continue
        print("Вы бросаете кости...")
        time.sleep(2)
        you_one = random.randint(1,6)
        you_two = random.randint(1,6)
        you_bones = you_one + you_two
        print("Выпало:", you_one,"и", you_two)
        time.sleep(1)
        print("Сумма ваших костей:", you_bones)
        loop = int(0)
        while loop == int(0):
            print("Если вы считаете, что ваша сумма будет больше, нажмите +, если меньше, то нажмите -")
            balance = str(input())
            if balance == str('+'):
                range = int(1)
                loop = int(1)
            elif balance == str('-'):
                range = int(0)
                loop = int(1)
            else:
                print("Введите + или - !")
        print(enemy_name, "Бросает кости...")
        time.sleep(2)
        enemy_one = random.randint(1, 6)
        enemy_two = random.randint(1, 6)
        enemy_bones = enemy_one + enemy_two
        print("Выпало:", enemy_one, "и", enemy_two)
        time.sleep(1)
        print("Сумма костей", enemy_name, "-", enemy_bones)
        time.sleep(1)
        if (you_bones > enemy_bones and range == 1) or (you_bones < enemy_bones and range == 0):
            print("Вы выиграли: " + str(rate) + "$")
            money = money + rate
            enemy_cash = enemy_cash - rate
            your_turn = 0
        elif (you_bones > enemy_bones and range == 0) or (you_bones < enemy_bones and range == 1):
            print("Вы проиграли: " + str(rate) + "$")
            money = money - rate
            enemy_cash = enemy_cash + rate
            your_turn = 0
        elif you_bones == enemy_bones:
            print("Ничья! Все остались при своих")
            your_turn = 0




    elif your_turn == 0:
        rate = random.choice([10,20,50,100])
        if rate > money:
            print("Вы не можете столько поставить, сделайте ставку меньше!")
            continue
        if rate > enemy_cash:
            if 10 < enemy_cash < 100:
                rate = 10
            else:
                print(enemy_name,"не может столько поставить, Он выбывает из игры, вам будет подобран новый соперник")
                enemy_status = 0
                while enemy_status == 0:
                    new_enemy = random.randint(0, 8)
                    if new_enemy != enemy:
                        enemy_name = text[new_enemy]['name']
                        enemy_cash = text[new_enemy]['cash']
                        enemy_status = 1
                        print("Ваш новый оппонент:", enemy_name)
                    else:
                        new_enemy = random.randint(0, 8)
                    continue
        print(enemy_name, "сделал ставку в размере -", str(rate)+'$')
        time.sleep(1)
        print(enemy_name, "Бросает кости...")
        time.sleep(2)
        enemy_one = random.randint(1, 6)
        enemy_two = random.randint(1, 6)
        enemy_bones = enemy_one + enemy_two
        print("Выпало:", enemy_one, "и", enemy_two)
        time.sleep(1)
        print("Сумма костей", enemy_name, "-", enemy_bones)
        loop = int(0)
        enemy_range = random.randint(1, 12)
        if enemy_bones > enemy_range or enemy_bones > 10:
            print(enemy_name, "Считает, что у него будет больше, чем у Вас.")
            range = int(1)
        elif enemy_bones <= enemy_range or enemy_bones < 4:
            print(enemy_name, "Считает, что у него будет меньше, чем у Вас.")
            range = int(0)
        print("Вы бросаете кости...")
        time.sleep(2)
        you_one = random.randint(1, 6)
        you_two = random.randint(1, 6)
        you_bones = you_one + you_two
        print("Выпало:", you_one, "и", you_two)
        time.sleep(1)
        print("Сумма ваших костей:", you_bones)
        time.sleep(1)
        if (you_bones < enemy_bones and range == 0) or (you_bones > enemy_bones and range == 1):
            print("Вы выиграли: " + str(rate) + "$")
            money = money + rate
            enemy_cash = enemy_cash - rate
            your_turn = 1
        elif (you_bones < enemy_bones and range == 1) or (you_bones > enemy_bones and range == 0):
            print("Вы проиграли: " + str(rate) + "$")
            money = money - rate
            enemy_cash = enemy_cash + rate
            your_turn = 1
        elif you_bones == enemy_bones:
            print("Ничья! Все остались при своих")
            your_turn = 1



    print("Продолжаем играть? y/n")
    game_over = str(input())
    if game_over == 'y' or game_over == 'Y':
        continue
    elif game_over == 'n' or game_over == 'N':
        with open(savedata, 'w', encoding='utf-8') as outfile:
            json.dump({
                "cash": money,
            }, outfile)
        print("До встречи!")
        break
    else:
        print("Мы воспринимаем это как да! Игра продолжается!")
        continue