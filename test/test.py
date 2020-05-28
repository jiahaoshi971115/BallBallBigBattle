from threading import Thread
from queue import Queue

import time

from tkinter import *

def t(s:str):
    window = Tk()

    window.title("Welcome to LikeGeeks app")

    def call_back(s):
        print(s)

    b = Button(window, text='click', command=call_back(s))
    b.pack()
    window.mainloop()

def controller_send(q:Queue):
    window = Tk()

    window.title("Welcome to LikeGeeks app")

    def call_back():
        q.put("click")

    b = Button(window, text='click', command=call_back)
    b.pack()
    window.mainloop()


def gui_collect(q:Queue):
    count = 0
    while True:
        count += 1
        try:
            a = q.get(block=True, timeout=0.1)
            print("[GUI]" + str(int(time.time()*1000)) + " get message: "+a)
        except Exception:
            print("[GUI]" + str(int(time.time()*1000)) + " time out.")

q = Queue()
t1 = Thread(target=controller_send, args=(q,))
t2 = Thread(target=gui_collect, args=(q,))
t1.start()
t2.start()
#t("123")