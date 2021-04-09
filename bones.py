import random
import time
import sys
import json
import os.path
import pygame
pygame.mixer.init()

money = int(100)
Cashback = int(0)
credit_status = int(0)

with open('player.json', 'r', encoding='utf-8') as x:
    save = json.load(x)  # Создание, либо загрузка сохранения
    name = save["name"]

savedata = ("savedata\\"+name+".json")

with open(savedata, 'r', encoding='utf-8') as x:
    save = json.load(x)                                                                                             # Создание, либо загрузка сохранения
    money = save["client_cash"]
    Cashback = save["client_cashback"]
    credit_status = save["credit_status"]


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
        error_status = 0
        while error_status == 0:
            try:
                pygame.mixer.music.load('music\\rate.mp3')
                pygame.mixer.music.play(0)
                print(name, "Какую ставку вы хотите сделать? у вас на счету сейчас -", str(money)+"$. У оппонента -", enemy_cash)
                rate = int(input())
            except ValueError:
                print("Не корректный формат! Введите число")
            else:
                error_status = 1
                if rate > money or rate < 10:
                    print("Вы не можете столько поставить, сделайте ставку больше 10$, но не больше суммы на вашем счету!")
                    continue
                if rate > enemy_cash or rate < 10:
                    pygame.mixer.music.load('music\\victory.mp3')
                    pygame.mixer.music.play(0)
                    print(enemy_name,"не может столько поставить, Он выбывает из игры, вам будет подобран новый соперник")
                    time.sleep(3)
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
                pygame.mixer.music.load('music\\bones.mp3')
                pygame.mixer.music.play(0)
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
                pygame.mixer.music.load('music\\bones.mp3')
                pygame.mixer.music.play(0)
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
                    pygame.mixer.music.load('music\\win.mp3')
                    pygame.mixer.music.play(0)
                    print("Вы выиграли: " + str(rate) + "$")
                    money = money + rate
                    enemy_cash = enemy_cash - rate
                    your_turn = 0
                elif (you_bones > enemy_bones and range == 0) or (you_bones < enemy_bones and range == 1):
                    pygame.mixer.music.load('music\\lose.mp3')
                    pygame.mixer.music.play(0)
                    print("Вы проиграли: " + str(rate) + "$")
                    money = money - rate
                    enemy_cash = enemy_cash + rate
                    your_turn = 0
                elif you_bones == enemy_bones:
                    print("Ничья! Все остались при своих")
                    your_turn = 0




    elif your_turn == 0:
        if  enemy_cash > 1000 and money > 1000:
            rate = random.choice([100,round(money/2),round(money/4),round(money/10)])
        else:
            rate = random.choice([10, 20, 50, 100])
        if rate > money:
            print("Вы не можете столько поставить, сделайте ставку меньше!")
            continue
        if rate > enemy_cash:
            if 10 < enemy_cash < 100:
                rate = 10
            else:
                pygame.mixer.music.load('music\\victory.mp3')
                pygame.mixer.music.play(0)
                print(enemy_name,"не может столько поставить, Он выбывает из игры, вам будет подобран новый соперник")
                time.sleep(3)
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
        pygame.mixer.music.load('music\\rate.mp3')
        pygame.mixer.music.play(0)
        print(enemy_name, "сделал ставку в размере -", str(rate)+'$')
        time.sleep(1)
        pygame.mixer.music.load('music\\bones.mp3')
        pygame.mixer.music.play(0)
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
        pygame.mixer.music.load('music\\bones.mp3')
        pygame.mixer.music.play(0)
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
            pygame.mixer.music.load('music\\win.mp3')
            pygame.mixer.music.play(0)
            print("Вы выиграли: " + str(rate) + "$")
            money = money + rate
            enemy_cash = enemy_cash - rate
            your_turn = 1
        elif (you_bones < enemy_bones and range == 1) or (you_bones > enemy_bones and range == 0):
            pygame.mixer.music.load('music\\lose.mp3')
            pygame.mixer.music.play(0)
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
                "client_cash": money,
                "client_cashback": Cashback,
                "credit_status": credit_status,
            }, outfile)
        with open('player.json', 'w', encoding='utf-8') as outfile:
            json.dump({"name": name, "cash": money}, outfile)
        print("До встречи!")
        pygame.mixer.music.unload()
        break
    else:
        print("Мы воспринимаем это как да! Игра продолжается!")
        continue