import tkinter as tk
# from tkinter import *
# win=Tk
win=tk.Tk()
win.geometry("500x500")
win.title("STUDENT MANAGEMENT SYSTEM")


def quit():
    win.destroy

def New():
    nw=tk.Tk()
    nw.geometry("500x500")
    nw.title("New File")
    
    nw.mainloop()
    
def about_notpad():
    abt=tk.Tk()
    abt.geometry("500x500")
    abt.title("About Us")
    message="""Windows Notepad is a simple text editor for Windows;
               it creates and edits plain text documents.
               First released in 1983 to commercialize the computer mouse in MS-DOS, 
               Notepad has been part of every version of Windows ever since. """
    intinfo=tk.Label(abt,text=message)
    intinfo.pack()
    abt.mainloop()


menubar=tk.Menu(win)                                 #common for all menu..create menubar(menu=syntax),win=obj
filemenu=tk.Menu(menubar,tearoff=0)                  #create for filemenu
menubar.add_cascade(label="File",underline=0,menu=filemenu)        #create file based on menubar
filemenu.add_command(label="New",underline=0,accelerator="Ctrl+N",command=New)                   #create submenus based on filemenu
filemenu.add_command(label="New Window",underline=0,accelerator="Ctrl+Shift+N")
filemenu.add_command(label="Open",underline=0,accelerator="Ctrl+O")
filemenu.add_command(label="Save",underline=0,accelerator="Ctrl+S")
filemenu.add_command(label="Save As",underline=0,accelerator="Ctrl+Shift+S")
filemenu.add_separator()
filemenu.add_command(label="Page Setup",underline=0)
filemenu.add_command(label="Print",underline=0,accelerator="Ctrl+P")
filemenu.add_separator()
filemenu.add_command(label="Exit",underline=0,command=quit)


editmenu=tk.Menu(menubar,tearoff=0)                  #create for filemenu
menubar.add_cascade(label="Edit",underline=0,menu=editmenu)        #create file based on menubar
editmenu.add_command(label="Undo",underline=0,accelerator="Ctrl+Z")  #create submenus based on filemenu
editmenu.add_separator()                                 
editmenu.add_command(label="Cut",underline=0,accelerator="Ctrl+X")
editmenu.add_command(label="Copy",underline=0,accelerator="Ctrl+C")
editmenu.add_command(label="Paste",underline=0,accelerator="Ctrl+P")
editmenu.add_command(label="Delete",underline=0,accelerator="Del")
editmenu.add_separator()
editmenu.add_command(label="Search with Bing",underline=0,accelerator="Ctrl+E")
editmenu.add_command(label="Find",underline=0,accelerator="Ctrl+F")
editmenu.add_command(label="Fine Next",underline=0,accelerator="F3")
editmenu.add_command(label="Find Previous",underline=0,accelerator="Shift+F3")
editmenu.add_command(label="Replace",underline=0,accelerator="Ctrl+H")
editmenu.add_command(label="Go To",underline=0,accelerator="Ctrl+P")
editmenu.add_separator()
editmenu.add_command(label="Select All",underline=0,accelerator="Ctrl+G")
editmenu.add_command(label="Time/Date",underline=0,accelerator="F5")


formatmenu=tk.Menu(menubar,tearoff=0)                  
menubar.add_cascade(label="Format",underline=0,menu=formatmenu)
formatmenu.add_command(label="Word Wrap",underline=0)
formatmenu.add_command(label="Font",underline=0)

viewmenu=tk.Menu(menubar,tearoff=0)                
menubar.add_cascade(label="View",underline=0,menu=viewmenu)
viewmenu.add_command(label="Zoom",underline=0)
viewmenu.add_command(label="Status",underline=0)

helpmenu=tk.Menu(menubar,tearoff=0)                
menubar.add_cascade(label="Help",underline=0,menu=helpmenu)
helpmenu.add_command(label="View Help",underline=0)
helpmenu.add_command(label="Send Feedback",underline=0)
helpmenu.add_separator()
helpmenu.add_command(label="About Notpad",underline=0,command=about_notpad)







win.config(menu=menubar)

win.mainloop()