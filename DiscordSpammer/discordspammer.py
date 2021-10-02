import threading
import requests
import time

print("")
print("▒█▀▀█ █░░█ █▀▀ █▀▀ █░░█ 　 ▒█░▄▀ ░▀░ █░░ █░░ █▀▀ █▀▀█")
print("▒█▄▄█ █░░█ ▀▀█ ▀▀█ █▄▄█ 　 ▒█▀▄░ ▀█▀ █░░ █░░ █▀▀ █▄▄▀")
print("▒█░░░ ░▀▀▀ ▀▀▀ ▀▀▀ ▄▄▄█ 　 ▒█░▒█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀░▀▀")

print("                                      Made by Lososik")
channel = input('Id of channel: ')
mess = input('Message to spam: ')
delay = input('Delay: ')

tokens = open("tokens.txt", "r").read().splitlines()


def spam(token, channel, mess):
    url = 'https://discord.com/api/v9/channels/'+channel+'/messages'
    data = {"content": mess}
    header = {"authorization": token}

    while True:
        time.sleep(int(delay))
        r = requests.post(url, data=data, headers=header)
        print(r.status_code)



def thread():
    channel_id = channel
    text = mess
    for token in tokens:
        time.sleep(int(delay))
        threading.Thread(target=spam, args=(token, channel_id, text)).start()


start = input('Press eny key when you will be ready ')
start = thread()
