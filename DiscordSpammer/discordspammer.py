import threading
import requests
from tkinter import *


print("▒█▀▀█ █░░█ █▀▀ █▀▀ █░░█ 　 ▒█░▄▀ ░▀░ █░░ █░░ █▀▀ █▀▀█")
print("▒█▄▄█ █░░█ ▀▀█ ▀▀█ █▄▄█ 　 ▒█▀▄░ ▀█▀ █░░ █░░ █▀▀ █▄▄▀")
print("▒█░░░ ░▀▀▀ ▀▀▀ ▀▀▀ ▄▄▄█ 　 ▒█░▒█ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀░▀▀")

print("                              ☠  Made by Lososik  ☠")
channel = input('Id of channel: ')
mess = input('Message to spam: ')


def sendMessage(token1, token2, token3, token4, token5, token6, token7, token8, token9, token10):  #you can append tokens just add token11, token12 and You can spam with 12 tokens, but in default version only in 10




    url = 'https://discord.com/api/v9/channels/'+channel+'/messages'
    data = {"content": mess}
    header1 = {"authorization": token1}
    header2 = {"authorization": token2}
    header3 = {"authorization": token3}
    header4 = {"authorization": token4}
    header5 = {"authorization": token5}
    header6 = {"authorization": token6}
    header7 = {"authorization": token7}
    header8 = {"authorization": token8}
    header9 = {"authorization": token9}
    header10 = {"authorization": token10} #you can append tokens just add header11, header12 and You can spam with 12 tokens, but in default version only in 10


    r = requests.post(url, data=data, headers=header1)
    print(r.status_code)

    a = requests.post(url, data=data, headers=header2)
    print(a.status_code)

    b = requests.post(url, data=data, headers=header3)
    print(b.status_code)

    c = requests.post(url, data=data, headers=header4)
    print(c.status_code)

    d = requests.post(url, data=data, headers=header5)
    print(d.status_code)

    e = requests.post(url, data=data, headers=header6)
    print(e.status_code)

    f = requests.post(url, data=data, headers=header7)
    print(f.status_code)

    g = requests.post(url, data=data, headers=header8)
    print(g.status_code)

    h = requests.post(url, data=data, headers=header9)
    print(h.status_code)

    ch = requests.post(url, data=data, headers=header10) #and you need to add requests, if you want to add more tokens
    print(ch.status_code)

   


def spam():
    while True:
        sendMessage("token1", #put your tokens in ""
		    "token2",
                    "token3",
                    "token4",
		    "token5",
                    "token6",
		    "token7",
		    "token8", 
                    "token9",
		    "token10",
                    )


def thread():
    threds = []

    for i in range(100000):
        t = threading.Thread(target=spam)
        t.daemon = True
        threds.append(t)

    for i in range(100000):
        threds[i].start()

    for i in range(100000):
        threds[i].join()

window = Tk()

img = PhotoImage(file='evil.png') #this is bakground picture, you need to download the image or delete this line

window.title('Pussy Killer Spammer')
window.config(bg='#000000')
window.geometry('100x200')


window.resizable(0,0)

bg = Label(window,image=img, bg='black') #this is bakground picture, you need to download the image or delete this line
bg.pack()

box = LabelFrame(window,text="Modes", bg='#000000', fg='white') 
box.pack(pady=5, padx=5)

button = Button(box, text='Fast spam', command=thread, relief=RAISED)
button.pack(pady=5, padx=5)

button = Button(box, text='Normal spam', command=spam, relief=RAISED)
button.pack(pady=5, padx=5)

window.update()
window.mainloop()