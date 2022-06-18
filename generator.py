import random
from time import sleep

import requests


def telegram_bot_sendtext(bot_message):

    bot_token = '5099605327:AAGtUk3n7lQCUMD10u5tlYdYBTC1-ZZqd08'
    bot_chatID = '444319764'
    send_text = 'https://api.telegram.org/bot' + bot_token + \
        '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


nums = []

for i in range(48, 58):
    nums.append(i)
for i in range(65, 91):
    nums.append(i)
for i in range(97, 123):
    nums.append(i)


def gen_link():
    link = "https://ya.cc/"
    for i in range(5):
        link += chr(random.choice(nums))
    return link


test = telegram_bot_sendtext("starting")
print(test)
for i in range(100500):
    # sleep(0.05)
    link = gen_link()
    if i % 1000 == 0:
        test = telegram_bot_sendtext(str(i) + " requests send")
        print(test)
    try:
        response = requests.get(link)
    except Exception:
        continue
    if response.status_code == 200 and "Yandex.Code" in str(response.content):
        print()
        print(link)
        test = telegram_bot_sendtext(link)
        print(test)
    # else:
    #     if i % 40 == 0:
    #         print()
    #     print("rej", end=' ')
