from tkinter import *

#creating the main window
root = Tk()

# entry widget
# many paramaters can be used as well (ie: bg, borderwidth, etc)
e = Entry(root, width=50, bg="yellow", borderwidth=5)
e.pack()
e.get() # gets the entry field text
e.insert(0, "Enter Your Name: ")# placeholder of the input field



def myClick():
    myLabel = Label(root, text=e.get()) #gets inputs
    myLabel.pack()


def myClick2():
    # created a variable named dope for cleaner code option (recommended riiiiight)
    dope = ".... you are a Genius!"
    myLabel = Label(root, text= dope) #gets inputs
    myLabel.pack()
    
    
myButton1 = Button(root, text="Submit Name", command=myClick, fg="yellow", bg="blue") # submits and displays entries
myButton1.pack()


myButton2 = Button(root, text="Button 2", command=myClick2, fg="white", bg="green") # displays message
myButton2.pack()


# create a loop for the GUI
root.mainloop()