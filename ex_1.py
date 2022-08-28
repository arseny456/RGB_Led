import serial
from time import sleep
from tkinter import Tk, BOTH, IntVar, LEFT
from tkinter.ttk import Frame, Label, Scale, Style

port = "COM4"
ser = serial.Serial(port=port, timeout=0, baudrate=57600)

root = Tk()
root.geometry("550x400+300+300")

sleep(2)

# ser.write(b'3,55,0;')
# answer = ser.readline()
# print(answer)
var = IntVar()
var2 = IntVar()
var3 = IntVar()


def onScale(val):
    # global var
    v = int(float(val))
    var.set(v)
    ser.write(f'1,{v},0;'.encode('utf-8'))
    # ser.readline()


def onScale2(val):
    # global var
    b = int(float(val))
    var2.set(b)
    ser.write(f'2,{b},0;'.encode('utf-8'))
    # ser.readline()


def onScale3(val):
    # global var
    c = int(float(val))
    var3.set(c)
    ser.write(f'3,{c},0;'.encode('utf-8'))
    # ser.readline()


scale = Scale(root, from_=0, to=255, command=onScale)
scale.pack(side=LEFT, padx=15)

scale2 = Scale(root, from_=0, to=255, command=onScale2)
scale2.pack(side=LEFT, padx=15)

scale3 = Scale(root, from_=0, to=255, command=onScale3)
scale3.pack(side=LEFT, padx=15)

label = Label(root, text=0, textvariable=var)
label.pack(side=LEFT, padx=15)

label2 = Label(root, text=0, textvariable=var2)
label2.pack(side=LEFT, padx=15)

label3 = Label(root, text=0, textvariable=var3)
label3.pack(side=LEFT, padx=15)

root.mainloop()

ser.close()
