from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Button One Clicked - Orion3000")
    myLabel.pack()
    

def myClick2():
    myLabel = Label(root, text="Button Three Clicked - Orion3000")
    myLabel.pack()
    

def myClick3():
    myLabel = Label(root, text="Clear Button Clicked - Orion3000")
    myLabel.pack()


myButton1 = Button(root, text="Button One", command=myClick, padx=50, pady=50, fg="yellow", bg="blue")
myButton1.pack()


myButton2 = Button(root, text="Button Two", state=DISABLED, padx=50, pady=50, fg="black", bg="yellow")
myButton2.pack()

myButton3 = Button(root, text="Button Three", command=myClick2, padx=50, pady=50, fg="white", bg="red")
myButton3.pack()

myButton3 = Button(root, text="Clear Screen", command=myClick3)
myButton3.pack()

# create a loop for the GUI
root.mainloop()