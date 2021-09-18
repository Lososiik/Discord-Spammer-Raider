import threading
import requests
from tkinter import *
import time



print("")
print("▒█▀▀█ █░░█ █▀▀ █▀▀ █░░█ 　 ▒█░▄▀ ░▀░ █░░ █░░ █▀▀ █▀▀█")
print("▒█▄▄█ █░░█ ▀▀█ ▀▀█ █▄▄█ 　 ▒█▀▄░ ▀█▀ █░░ █░░ █▀▀ █▄▄▀")
print("▒█░░░ ░▀▀▀ ▀▀▀ ▀▀▀ ▄▄▄█ 　 ▒█░▒█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀░▀▀")

print("                                     Made by Lososik")
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




window = Tk()

img = PhotoImage(file='evil.png')

window.title('Pussy Killer Spammer')
window.config(bg='#000000')
window.geometry('100x170')


window.resizable(0,0)

bg = Label(window,image=img, bg='black')
bg.pack()

box = LabelFrame(window,text="Main", bg='#000000', fg='white')
box.pack(pady=5, padx=5)

button = Button(box, text='Spam', command=thread, relief=RAISED)
button.pack(pady=5, padx=25)


window.update()
window.mainloop()
