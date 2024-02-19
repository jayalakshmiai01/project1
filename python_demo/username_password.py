


from tkinter import *
from tkinter import messagebox


def no():
	messagebox.showbox=(" ","login successflly")
	quit()

# Window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')

# Username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

# Password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  



# Login button
loginButton = Button(tkWindow, text="Login", command=no).grid(row=4, column=0)  

tkWindow.mainloop()