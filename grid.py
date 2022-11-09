#importing all of tkinter module
from tkinter import *

#creating the main window
root = Tk()

# Creating the label widget
myLabel1 = Label(root, text="Greetings Orion!")
myLabel2 = Label(root, text="Welcome to Tkinter Tuts")

# another way to use the grid is placing it at end of widget but not recommended.
myLabel3 = Label(root, text="Label 3 Here").grid(row=2, column=0)

# displaying on the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)


# create a loop for the GUI
root.mainloop()