import serial
from time import sleep
port="COM4"
ser = serial.Serial(port=port, baudrate=57600, timeout=0)

from tkinter import *

root = Tk()

label = Label(text=0)
label.pack()

sleep(2)

def f():
    a = ser.readline()
    if a:
        print(a)
        label.config(text=a.decode('utf-8'))

    root.after(10, func=f)


f()

root.mainloop()

ser.close()