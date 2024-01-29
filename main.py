"""
Made by Hamed Pourheidari
pip install tkinter
pip install stegano
pip install pillow
"""

from tkinter import *
from tkinter import filedialog, Scrollbar
from tkinter import Tk, ttk, PhotoImage
from PIL import Image, ImageTk
import os
from stegano import lsb

root = Tk()
# ----------------------APP NAME-----------------------------------
root.title("Steganography-Hide a Secret Text Message in an Image")
# ----------------------APP NAME-----------------------------------

root.geometry("700x500+350+180")
root.resizable(False, False)
root.configure(bg="#2f4155")


def showimage():
    global lbl
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File',filetypes=(('PNG file', "*.png"), ('JPG ile', "*.jpg"), ('All file', "*.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl= Label(root, bg="black")
    lbl.configure(image=img, width=250, height=250)
    lbl.image = img

def Hide():
    global secret
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)


def Show():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)


def save():
    secret.save("hidden.png")


# -----------------ICON---------------------
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)
# -----------------ICON---------------------

# ------------------------------------------------LOGO-----------------------------------------------
logo = PhotoImage(file="logo.png")
Label(root,image=logo, bg="#2f4155").place(x=0, y=0)
Label(root, text="CYBER SCIENCE", bg="#2d4155", fg="white", font="BTitr 25 bold").place(x=220, y=10)
# ------------------------------------------------LOGO-----------------------------------------------

# ---------------------------------------- First Frame ----------------------------------------
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE).place(x=10, y=80)
lbl = Label(f, bg="black").place(x=40, y=10)
# ---------------------------------------- First Frame ----------------------------------------

# ---------------------------------------- Second Frame ----------------------------------------
frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE).place(x=350, y=80)
text1 = Text(frame2, font="BTitr 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=350, y=80, width=340, heigh=280)
scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=690, y=75, height=290)
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)
# ---------------------------------------- Second Frame ----------------------------------------


# ----------------------------------------Third Frame----------------------------------------
frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)
Button(frame3, text="Open Image", width=10, height=2, font="BTit 12", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="BTit 12", command=save).place(x=180, y=30)
Label(frame3, text="Picture, Image, Photo, File", bg="#2f4155", fg="yellow").place(x=20, y=5)
# ----------------------------------------Third Frame----------------------------------------


# ----------------------------------------Fourth Frame----------------------------------------
frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)
Button(frame4, text="Hide Data", width=10, height=2, font="BTit 12", command=Hide).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="BTit 12", command=Show).place(x=180, y=30)
Label(frame4, text="Picture, Image, Photo, File", bg="#2f4155", fg="yellow").place(x=20, y=5)
# ----------------------------------------Fourth Frame----------------------------------------


root.mainloop()
