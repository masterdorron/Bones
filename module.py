import subprocess
import random
import time
import sys
import json
import os.path


if_exit = 0
money = int(500)
Cashback = int(0)
credit_status = int(0)

print("Представьтесь, пожалуйста!")
name = str(input())

with open('player.json', 'w', encoding='utf-8') as outfile:
    json.dump({
        "name": name
    }, outfile)

savedata = ("savedata\\"+name+".json")                                                                                  #Проверка на наличие сохранения
save_not_null = os.path.isfile(savedata)


if save_not_null is False:
    with open(savedata, 'w', encoding='utf-8') as outfile:
        json.dump({
            "client_cash": money,
            "client_cashback": Cashback,
            "credit_status": credit_status,
        }, outfile)


while if_exit == 0:
    print("Выберите отдел казино: 1 - Угадать число, 2 - кости. exit - выход.")
    start = str(input())
    if start == str('1'):
        retcode = subprocess.call(["Scripts\\python.exe", "azino.py"])
    elif start == str('2'):
        retcode = subprocess.call(["Scripts\\python.exe", "bones.py"])
    elif start == str('exit'):
        sys.exit(0)
    else:
        print("Некорректный формат данных!")



