import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from colorthief import ColorThief
import os

root = tk.Tk()
root.title('Color picker from image')
root.geometry('800x470+100+100')
root.configure(background='#9fc5e8')
root.resizable(False, False)

def showimage():
    global filename
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select Image File",
                                          filetype=(("PNG files","*.png"),("JPG files","*.jpg"),("JPEG files","*.jpeg"),("All files","*.*")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    lbl.config(image=img, width=310, height=270)
    lbl.image = img

def Findcolor():
    ct = ColorThief(filename)
    palette = ct.get_palette(color_count=11)
    
    colors_list = []
    for rgb in palette:
        color = f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"
        colors_list.append(color)
    
    colors.itemconfig(id1, fill=colors_list[0])
    colors.itemconfig(id2, fill=colors_list[1])
    colors.itemconfig(id3, fill=colors_list[2])
    colors.itemconfig(id4, fill=colors_list[3])
    colors.itemconfig(id5, fill=colors_list[4])

    colors2.itemconfig(id6, fill=colors_list[5])
    colors2.itemconfig(id7, fill=colors_list[6])
    colors2.itemconfig(id8, fill=colors_list[7])
    colors2.itemconfig(id9, fill=colors_list[8])
    colors2.itemconfig(id10, fill=colors_list[9])

    hex1.config(text=colors_list[0])
    hex2.config(text=colors_list[1])
    hex3.config(text=colors_list[2])
    hex4.config(text=colors_list[3])
    hex5.config(text=colors_list[4])
    hex6.config(text=colors_list[5])
    hex7.config(text=colors_list[6])
    hex8.config(text=colors_list[7])
    hex9.config(text=colors_list[8])
    hex10.config(text=colors_list[9])

#icon
image_icon = PhotoImage(file='./images/icon.png')
root.iconphoto(False, image_icon)

Label(root, width=120, height=10, bg="#990000").pack()

#frame
frame = Frame(root, width=700, height=370, bg="#fff")
frame.place(x=50,y=50)

logo = PhotoImage(file='./images/logo.png')
Label(frame, image=logo, bg="#fff").place(x=10,y=10)

Label(frame, text="Color Finder", font="arial 25 bold", bg="white").place(x=100,y=20)

#color1
colors = Canvas(frame, width=150, height=265, bd=0, bg="#fff")
colors.place(x=20, y=90)

id1 = colors.create_rectangle(10,10,50,50, fill="#1abc9c")
id2 = colors.create_rectangle(10,50,50,100, fill="#3498db")
id3 = colors.create_rectangle(10,100,50,150, fill="#9b59b6")
id4 = colors.create_rectangle(10,150,50,200, fill="#e74c3c")
id5 = colors.create_rectangle(10,200,50,250, fill="#f1c40f")

hex1 = Label(colors, text="#1abc9c", font="arial 12 bold", bg="white", fg="#000")
hex1.place(x=60,y=15)

hex2 = Label(colors, text="#3498db", font="arial 12 bold", bg="white", fg="#000")
hex2.place(x=60,y=65)

hex3 = Label(colors, text="#9b59b6", font="arial 12 bold", bg="white", fg="#000")
hex3.place(x=60,y=115)

hex4 = Label(colors, text="#e74c3c", font="arial 12 bold", bg="white", fg="#000")
hex4.place(x=60,y=165)

hex5 = Label(colors, text="#f1c40f", font="arial 12 bold", bg="white", fg="#000")
hex5.place(x=60,y=215)

#color2
colors2 = Canvas(frame, width=150, height=265, bd=0, bg="#fff")
colors2.place(x=180, y=90)

id6 = colors2.create_rectangle(10,10,50,50, fill="#e67e22")
id7 = colors2.create_rectangle(10,50,50,100, fill="#2ecc71")
id8 = colors2.create_rectangle(10,100,50,150, fill="#16a085")
id9 = colors2.create_rectangle(10,150,50,200, fill="#2980b9")
id10 = colors2.create_rectangle(10,200,50,250, fill="#8e44ad")

hex6 = Label(colors2, text="#e67e22", font="arial 12 bold", bg="white", fg="#000")
hex6.place(x=60,y=15)

hex7 = Label(colors2, text="#2ecc71", font="arial 12 bold", bg="white", fg="#000")
hex7.place(x=60,y=65)

hex8 = Label(colors2, text="#16a085", font="arial 12 bold", bg="white", fg="#000")
hex8.place(x=60,y=115)

hex9 = Label(colors2, text="#2980b9", font="arial 12 bold", bg="white", fg="#000")
hex9.place(x=60,y=165)

hex10 = Label(colors2, text="#8e44ad", font="arial 12 bold", bg="white", fg="#000")
hex10.place(x=60,y=215)

#select image
selectimage = Frame(frame, width=340, height=350, bg="#d6dee5")
selectimage.place(x=350, y=10)

f = Frame(selectimage, bd=3, bg="black", width=320, height=280, relief=GROOVE)
f.place(x=10, y=10)

lbl = Label(f, bg="black")
lbl.place(x=0, y=0)

Button(selectimage, text="Select Image", width=12, height=1, font="arial 14 bold", command=showimage).place(x=10, y=300)
Button(selectimage, text="Find Colors", width=12, height=1, font="arial 14 bold", command=Findcolor).place(x=176, y=300)

root.mainloop()
