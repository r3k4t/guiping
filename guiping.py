
from tkinter import *
from pythonping import ping

def get_ping ():
	result = ping(r.get() ,verbose=True)
	t.set(result)
rkt = Tk()
rkt.title('GUI-PING(https://github.com/r3k4t)')
rkt.configure(bg='purple')
t = StringVar()
Label(rkt, text="Enter a URL or IP :",bg="purple").grid(row=0, sticky=W)
Label(rkt, text="Result :", bg="purple").grid(row=1, sticky=W)
Label(rkt, text="", textvariable=t,bg="purple").grid(row=1, column=1,sticky=W)
r = Entry(rkt)
r.grid(row=0, column=1)
b = Button(rkt,text="Click", command=get_ping)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=4, pady=8)
rkt.mainloop()


