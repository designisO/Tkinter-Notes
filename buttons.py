#importing all of tkinter module
from tkinter import *

#creating the main window
root = Tk()

# button action function
def myClick():
    myLabel = Label(root, text="Look! Software made by Orion!")
    myLabel.pack()

# Creating a button
# command allows the function to occur.
# fg (foreground), bg(background) colors
# You can use hex color codes

myButton1 = Button(root, text="Button One", command=myClick, fg="yellow", bg="blue")
myButton1.pack()


# made the button disabled using state
myButton2 = Button(root, text="Button Two", state=DISABLED)
myButton2.pack()

# padx and pady changes the sizes
myButton3 = Button(root, text="Button Three", padx=50, pady=50)
myButton3.pack()

# create a loop for the GUI
root.mainloop()