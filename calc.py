from tkinter import *
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
from turtle import width
from functools import partial
import math

window = Tk()
window.title()
#window.geometry('800x800')
window.resizable(0, 0)
window.iconbitmap("icon.ico")

menu = Menu(window)

prev=""
znak=""
buf1 = 0
buf2 = ""
deistv = False
nepusto = ""
degr = True




txt = Label(window, width=33, height=2, text="", anchor=E, font=("Arial", 22), background='#a49c87', foreground='#2a2926')
txt.grid(row=0, column=0, columnspan=6)

def rads(x):
    global degr
    if degr == True:
        return math.radians(x)
    else:
        return x

def degpress():
    global degr
    degr = True
    deg.configure(background=grn)
    rad.configure(background='white')
def radpress():
    global degr
    degr = False
    rad.configure(background=grn)
    deg.configure(background='white')

def clk(n):
    global prev, buf2, znak, nepusto
    if n == "-" and nepusto != "":
        prev = float(prev)*-1
        prev = str(prev)
        s = prev[-2] + prev[-1]
        if s == ".0":
            prev = float(prev)
            prev = int(prev)
        prev = str(prev)
        nepusto = str(n)
        txt.configure(text=prev)
    else:
        prev += str(n)
        nepusto += str(n)
        txt.configure(text=prev)
        if znak != "":
            buf2 += str(n)
def dsv(t):
    global prev, buf1, buf2, znak, first_number, nepusto
    if deistv == False:
        buf1 = float(prev)
    prev += t
    nepusto = ""
    txt.configure(text=prev)
    znak = t
def equal():
    global prev, znak, buf1, buf2, deistv, nepusto
    if znak == "+":
        res = float(buf1)+float(buf2)
    if znak == "-":
        res = float(buf1)-float(buf2)
    if znak == "*":
        res = float(buf1)*float(buf2)
    if znak == "/":
        res = float(buf1)/float(buf2)
    if znak == "**":
        res = float(buf1)**float(buf2)
    res = round(res, 4)
    res = str(res)
    s = res[-2] + res[-1]
    if s == ".0":
        res = float(res)
        res = int(res)
    prev=str(res)
    nepusto=str(res)
    txt.configure(text=prev)
    prev=str(res)
    nepusto=str(res)
    znak = ""
    buf1 = res
    buf2 = ""
    deistv = True
def clear():
    global prev, buf1, buf2, znak, deistv, nepusto
    prev = ''
    nepusto = ''
    buf1 = 0
    buf2 = ''
    znak = ''
    deistv = False
    txt.configure(text=prev)

def percent():
    new = float(prev)*100
    new = round(new, 4)
    txt.configure(text=str(new)+"%")

def oneres(zn):
    global prev, znak, buf1, buf2, deistv, res, nepusto
    buf1 = float(prev)
    prev += zn
    nepusto += zn
    txt.configure(text=prev)
    res=1
    if zn == "!":
        n = int(buf1)
        res = math.factorial(n)
    if zn == "√":
        res = math.sqrt(buf1)
    res = round(res, 4)
    prev=str(res)
    nepusto =str(res)
    txt.configure(text=prev)
    prev=str(res)
    nepusto =str(res)
    znak = ""
    buf1 = res
    buf2 = ""
    deistv = True

def sinus():
    global buf1, prev
    buf1 = float(prev)
    prev = math.sin(rads(buf1))
    prev = round(prev, 4)
    txt.configure(text=prev)
    prev = str(prev)
def asinus():
    global buf1, prev
    buf1 = float(prev)
    prev = math.asin(rads(buf1))
    prev = round(prev, 4)
    txt.configure(text=prev)
    prev = str(prev)
def cosinus():
    global buf1, prev
    buf1 = float(prev)
    prev = math.cos(rads(buf1))
    prev = round(prev, 4)
    txt.configure(text=prev)
    prev = str(prev)
def acosinus():
    global buf1, prev
    buf1 = float(prev)
    prev = math.acos(rads(buf1))
    prev = round(prev, 4)
    txt.configure(text=prev)
    prev = str(prev)
def tangens():
    global buf1, prev
    buf1 = float(prev)
    prev = math.tan(rads(buf1))
    prev = round(prev, 4)
    txt.configure(text=prev)
    prev = str(prev)
def atangens():
    global buf1, prev
    buf1 = float(prev)
    prev = math.atan(rads(buf1))
    prev = round(prev, 4)
    txt.configure(text=prev)
    prev = str(prev)
def logn():
    global buf1, prev
    buf1 = float(prev)
    prev = math.log(rads(buf1))
    prev = round(prev, 4)
    txt.configure(text=prev)
    prev = str(prev)

def rd(n):
    pass

wid = 6
hei = 3
fnt = 'Arial'
fw = 18
bag = "#f1ffff"
fag = "#34332d"
yfag = "#544c08"
ylw = "#d4bf15"
grn = "#1d5a12"
red = "#b34d42"
wth = "#fffff1"
fag2 = "#8b8661"

b7 = Button(window, text="7", width=wid, height=hei, command=partial(clk, 7), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag)
b7.grid(column=0, row=1)
b8 = Button(window, text="8", width=wid, height=hei, command=partial(clk, 8), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag)
b8.grid(column=1, row=1)
b9 = Button(window, text="9", width=wid, height=hei, command=partial(clk, 9), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag)
b9.grid(column=2, row=1)

b4 = Button(window, text="4", width=wid, height=hei, command=partial(clk, 4), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag)
b4.grid(column=0, row=2)
b5 = Button(window, text="5", width=wid, height=hei, command=partial(clk, 5), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag)
b5.grid(column=1, row=2)
b6 = Button(window, text="6", width=wid, height=hei, command=partial(clk, 6), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag)
b6.grid(column=2, row=2)

b1 = Button(window, text="1", width=wid, height=hei, command=partial(clk, 1), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag)
b1.grid(column=0, row=3)
b2 = Button(window, text="2", width=wid, height=hei, command=partial(clk, 2), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag)
b2.grid(column=1, row=3)
b3 = Button(window, text="3", width=wid, height=hei, command=partial(clk, 3), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag)
b3.grid(column=2, row=3)

b0 = Button(window, text="0", width=13, height=hei, command=partial(clk, 0), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag)
b0.grid(column=0, row=4, columnspan=2)

dot = Button(window, text=".", width=wid, height=hei, command=partial(clk, "."), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag)
dot.grid(column=2, row=4)
dot = Button(window, text="±", width=wid, height=hei, command=partial(clk, "-"), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag2)
dot.grid(column=4, row=2)

plus = Button(window, text="+", width=wid, height=hei, command=partial(dsv, "+"), font=(fnt, fw), relief = FLAT, background=ylw, foreground=yfag)
plus.grid(column=3, row=1)
plus = Button(window, text="-", width=wid, height=hei, command=partial(dsv, "-"), font=(fnt, fw), relief = FLAT, background=ylw, foreground=yfag)
plus.grid(column=3, row=2)
plus = Button(window, text="*", width=wid, height=hei, command=partial(dsv, "*"), font=(fnt, fw), relief = FLAT, background=ylw, foreground=yfag)
plus.grid(column=3, row=3)
plus = Button(window, text="/", width=wid, height=hei, command=partial(dsv, "/"), font=(fnt, fw), relief = FLAT, background=ylw, foreground=yfag)
plus.grid(column=3, row=4)
plus = Button(window, text="%", width=wid, height=hei, command=percent, font=(fnt, fw), relief = FLAT, background=bag, foreground=fag2)
plus.grid(column=4, row=3)
plus = Button(window, text="xⁿ", width=wid, height=hei, command=partial(dsv, "**"), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag2)
plus.grid(column=5, row=1)
plus = Button(window, text="!", width=wid, height=hei, command=partial(oneres, "!"), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag2)
plus.grid(column=5, row=2)
plus = Button(window, text="√", width=wid, height=hei, command=partial(oneres, "√"), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag2)
plus.grid(column=5, row=3)
pi = Button(window, text="π", width=wid, height=hei, command=partial(clk, round(math.pi, 6)), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag2)
pi.grid(column=5, row=4)
pi = Button(window, text="e", width=wid, height=hei, command=partial(clk, round(math.e, 6)), font=(fnt, fw), relief = FLAT, background=bag, foreground=fag2)
pi.grid(column=6, row=4)
sinn = Button(window, text="sin()", width=wid, height=hei, command=sinus, font=(fnt, fw), relief = FLAT, background=bag, foreground=fag2)
sinn.grid(column=6, row=1)
coss = Button(window, text="cos()", width=wid, height=hei, command=cosinus, font=(fnt, fw), relief = FLAT, background=bag, foreground=fag2)
coss.grid(column=6, row=2)
tann = Button(window, text="tan()", width=wid, height=hei, command=tangens, font=(fnt, fw), relief = FLAT, background=bag, foreground=fag2)
tann.grid(column=6, row=3)
lnn = Button(window, text="ln()", width=wid, height=hei, command=logn, font=(fnt, fw), relief = FLAT, background=bag, foreground=fag2)
lnn.grid(column=7, row=4)
asinn = Button(window, text="asin()", width=wid, height=hei, command=asinus, font=(fnt, fw), relief = FLAT, background=bag, foreground=fag2)
asinn.grid(column=7, row=1)
acoss = Button(window, text="acos()", width=wid, height=hei, command=acosinus, font=(fnt, fw), relief = FLAT, background=bag, foreground=fag2)
acoss.grid(column=7, row=2)
atan = Button(window, text="atan()", width=wid, height=hei, command=atangens, font=(fnt, fw), relief = FLAT, background=bag, foreground=fag2)
atan.grid(column=7, row=3)


deg = Button(window, text="deg", width=6, height=2, command=degpress, font=(fnt, fw), relief = FLAT, background=grn)
deg.grid(column=6, row=0)
rad = Button(window, text="rad", width=6, height=2, command=radpress, font=(fnt, fw), relief = FLAT, background=wth)
rad.grid(column=7, row=0)


eq = Button(window, text="=", width=wid, height=hei, command=equal, font=(fnt, fw), relief = FLAT, background=ylw, foreground=yfag)
eq.grid(column=4, row=4)

clr = Button(window, text="C", width=wid, height=hei, command=clear, font=(fnt, fw), relief = FLAT, background=red, foreground=wth)
clr.grid(column=4, row=1)



window.mainloop()







