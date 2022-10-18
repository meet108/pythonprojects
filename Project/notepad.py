'''''
from tkinter import *
root = Tk()
root.geometry("744x133")
root.title("MeetNews")
root = Label(text="Meet Newspaper")
title_label = Label(text ='''#Abdul Rashid Salim Salman Khan is an Indian \nfilm actor, producer, occasional playback
#singer and television personality. In a film career spanning \nalmost thirty years, Khan has received numerous awards, including two National
#Film Awards as a film \nproducer, and two Filmfare Awards for acting. He has a significant following in Asia and the Indian \ndiaspora worldwide,
#and is cited in the media as one of the most commercially successful actors of Indian \ncinema. According to the Forbes 2018 list of Top-Paid 100
##bg="red",fg="white",padx=13,pady=94, font="bold", borderwidth=3, relief=SUNKEN )
#title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)
#root.pack(side=LEFT, fill=X, padx=34, pady=34 )
#root.mainloop()
''''''


'''''
from tkinter import *
root = Tk()
root.geometry("655x333")
def hello():
    print("Hii Everyone")
def name():
    print("Meet Shah")

frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, bg="grey", fg="blue",text="Hello",command=hello)
b1.pack(side=LEFT, padx=23)
b2 = Button(frame, fg="red", text="Tell me name now", command=name)
b2.pack(side=LEFT, padx=23)


root.mainloop()
'''''
'''''
from tkinter import *

def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")
root = Tk()
root.geometry("655x333")

user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid()
password.grid(row=1)

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid()
root.mainloop()
'''''
'''''
from tkinter import *

def getvals():
    print("Welcome to our travels and Thanks for your register")
    print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get()}")

    with open("records.txt","a") as f:
       f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentmodevalue.get()} \n")
root = Tk()

root.geometry("500x500")

Label(root, text="Welcome to travels",font="TimesNewRoman",pady=5).grid(row=0,column=3)
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
paymentmode= Label(root, text="PaymentMode")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

foodservice = Checkbutton(text="Want to prebook your meals?",variable=foodservicevalue)
foodservice.grid(row=6,column=3)

Button(text="Submit", command=getvals).grid(row=7, column=3)
root.mainloop()
'''''
'''''
from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Meet")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

can_widget.create_line(0, 0, 800, 400, fill="blue")
can_widget.create_line(0, 400, 800, 0, fill="red")


can_widget.create_rectangle(3, 5, 700, 300, fill="green")

can_widget.create_text(200, 200, text="python")

can_widget.create_oval(344, 233, 244, 355)
can_widget.create_arc(3, 5, 700, 300)
can_widget.create_polygon(3, 5, 700, 300)
root.mainloop()
'''''
'''''
from  tkinter import *
def meet(event):
    print(f"Hello From Meet {event.x}, {event.y}")
root = Tk()
root.title("Meet Event")
root.geometry("644x344")

widget = Button(root, text="Click Me")
widget.pack()

widget.bind('<Button-1>',meet)
widget.bind('<Double-1>',quit)
root.mainloop()
'''''
'''''
from tkinter import *

root = Tk()
root.title("Excercise 2")
root.geometry("644x344")
def resize():
    width_value=widthvalue.get()
    height_value=heightvalue.get()
    root.geometry(f"{width_value}x{height_value}")

height = Label(root, text="Height")
width = Label(root, text="Width")

height.grid(row=1,column=2)
width.grid(row=2,column=2)

heightvalue = StringVar()
widthvalue = StringVar()

heightentry = Entry(root, textvariable=heightvalue)
widthentry = Entry(root, textvariable=widthvalue)

heightentry.grid(row=1, column=3)
widthentry.grid(row=2, column=3)

Button(text="Submit", command=resize).grid(row=5, column=3)
root.mainloop()
'''''
'''''
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("644x566")
root.title("Menus Practice")

def myfunc():
    print("HaHa")

def help():
    print("I will Help you")
    tmsg.showinfo("Help","I will help you")

def rate():
    print("Rate us")
    value = tmsg.askquestion("How was your experience?","Is it good?")
    if value == "yes":
        msg = "Great. Rate us an appstore please"
    else:
        msg = "Ok We will try to improve"
    tmsg.showinfo("Experience",msg)
    print(value)

def divya():
    #ans = tmsg.askretrycancel("dosti krlo","sorry divaya dont want to be")
    #if ans:
    #    print("dosti")
    #else:
     #   print("save by yourself")

    #ans1 = tmsg.askyesnocancel("hey","dont")
    #if ans1:
    #    print("good")
    #else:
     #   print("Hard luck")
     ans2 = tmsg.showwarning("warn you","dont do it next time")
     if ans2:
         print("warning")
     else:
         print("Great")



mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New Project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save as", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File",menu=m1)

m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate",command=rate)
m3.add_command(label="Divya",command=divya)
mainmenu.add_cascade(label="Help",menu=m3)
root.config(menu=mainmenu)

root.mainloop()
'''''
'''''
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("455x233")
root.title("Slider tutorial")

def getdollar():
    print(f"we have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("Amount Credited",f"we have credited {myslider2.get()} dollars to your bank account")
#myslider = Scale(root, from_=0, to=100)
#myslider.pack()
Label(root, text="How many dollars do you want?").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval=50)
#myslider2.set(34)
myslider2.pack()
Button(root, text="Get dollars!",pady=10, command=getdollar).pack()

root.mainloop()
'''''
# You have to make a GUI for an online restaurant from which people order foods and you have to make the GUI in such
# a way which has a horizontal slider and which has a value from 0-10. The customer has to give rating to the ordered food
# and the rating has to be stored in a file. Also you have to make a button just below the slider with a title rate.
# The GUI has a label of "Rate us using the slider below."
'''''
from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

def rate():
    print("Thanks for giving good rating if u dont enjoy then we will try to improve.")
    tmsg.showinfo("Rating", f"Thanks for {slider1.get()} your rating And Visit again")
root.geometry("600x500")
root.title("Slider Practice for Online Restaurant")
Label(root, text="How much rating do you want to give my food?")
slider1 = Scale(root, from_=0, to=10, orient=HORIZONTAL)
slider1.pack()
Button(root, text="Rate",pady=10, command=rate).pack()
root.mainloop()
'''''
'''''
#radiobutton 

from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
def order():
      tmsg.showinfo("Order Recieved!",f"We have receiving order {var.get()}.Thanks for ordering")
      print("Thanks for visit")
root.geometry("655x444")
root.title("RadioButton")

#var = IntVar()
var = StringVar()
var.set("Radio")
#var.set(1)

Label(root, text = "What would you like to have?",font="TimesNewRoman",
      justify=LEFT, padx=14).pack()
radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa").pack(anchor='w')
radio = Radiobutton(root, text="Pizza", padx=14, variable=var, value="Pizza").pack(anchor='w')
radio = Radiobutton(root, text="Samosha", padx=14, variable=var, value="Samosha").pack(anchor='w')
radio = Radiobutton(root, text="Panipuri", padx=14, variable=var, value="Panipuri").pack(anchor='w')
Button(root, text="Order Now", command=order).pack()
root.mainloop()
'''''
'''''
#Listbox using tkinter

from tkinter import *
import tkinter.messagebox as tmsg

def add():
      global i
      lbx.insert(ACTIVE, f"{i}")
      i+=1
i=0
root = Tk()
root.geometry("455x233")
root.title("Listbox Tutorial ")

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "First Item of Our listbox")

Button(root, text="Add Item", command=add).pack()
root.mainloop()
'''''
'''''
#Scrollbar using tkinter

from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()
root.geometry("455x233")
root.title("Scrollbar Tutorial ")
# for connecting scrollbar to a widget
#1. widhget(yscrollcommand = scrollbar.set)
#2 scrollbar.config(command=widget.yview)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
#listbox = Listbox(root,yscrollcommand = scrollbar.set)
#for i in range(344):
#      listbox.insert(END, f"Item {i}")

#listbox.pack(fill="both",padx=22)
text = Text(root,yscrollcommand = scrollbar.set)
text.pack(fill=BOTH)
#scrollbar.config(command=listbox.yview)
scrollbar.config(command=text.yview)
root.mainloop()
'''''
'''''
# Status Bar using gui

from tkinter import *
import tkinter.messagebox as tmsg

def upload():
    statusvar.set("Busy...")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready")

root = Tk()
root.geometry("455x233")
root.title("Status Bar Tutorial ")

statusvar = StringVar()
statusvar.set("Ready")
sbar = Label(root,textvariable=statusvar, relief=SUNKEN,anchor='w')
sbar.pack(side=BOTTOM, fill=X)
Button(root, text="Upload",command=upload).pack()
root.mainloop()
'''''
#Using Classes And Objects To Create GUIs
'''''
from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("744x377")

    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvar=self.var, relief=SUNKEN, anchor='w')
        self.statusbar.pack(side=BOTTOM, fill=X)

    def click(self):
        print("Button Clicked")

    def createButton(self, inptext):
        Button(text=inptext, command=self.click).pack()
if __name__ == '__main__':
    window = GUI()
    window.status()
    window.createButton("Click me")
    window.mainloop()
'''''
#More Tkinter Tips, Tricks & Functions
'''''
from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("More knowledge")
root.wm_iconbitmap()
root.configure(background="grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="Close", command = root.destroy).pack()
root.mainloop()
'''''
#Calculator Using Tkinter
'''''
from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"
                
        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
root = Tk()
root.geometry("644x900")
root.title("Calculator By MeetShah")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f1 = Frame(root, bg="grey")
b1 = Button(f1, text="9",padx=28,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)

b1 = Button(f1, text="8",padx=28,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)

b1 = Button(f1, text="7",padx=28,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
f1.pack()

f1 = Frame(root, bg="grey")
b1 = Button(f1, text="6",padx=28,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)

b1 = Button(f1, text="5",padx=28,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)

b1 = Button(f1, text="4",padx=28,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
f1.pack()
f1 = Frame(root, bg="grey")
b1 = Button(f1, text="3",padx=28,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)

b1 = Button(f1, text="2",padx=28,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)

b1 = Button(f1, text="1",padx=28,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
f1.pack()
f1 = Frame(root, bg="grey")
b1 = Button(f1, text="0",padx=30,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)

b1 = Button(f1, text="-",padx=31,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)

b1 = Button(f1, text="*",padx=30,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
f1.pack()

f1 = Frame(root, bg="grey")
b1 = Button(f1, text="/",padx=29,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)

b1 = Button(f1, text="+",padx=29,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)

b1 = Button(f1, text="%",padx=25,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
f1.pack()

f1 = Frame(root, bg="grey")
b1 = Button(f1, text="C",padx=28,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)

b1 = Button(f1, text="=",padx=28,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)

b1 = Button(f1, text=".",padx=28,pady=18,font="lucida 25 bold")
b1.pack(side=LEFT,padx=18,pady=5)
b1.bind("<Button-1>",click)
f1.pack()
root.mainloop()
'''''
#GUI Notepad in TKinter


from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad by Meet")

if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x788")

    #Add TextArea
    TextArea = Text(root, font="TimesNewRoman")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Lets create a menubar
    MenuBar = Menu(root)

    #File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)

    # To save the current file

    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)

    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends

    root.config(menu=MenuBar)

    #Adding Scrollbar using rules from Tkinter
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()
