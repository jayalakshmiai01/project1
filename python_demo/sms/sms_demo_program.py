import os
from tkinter import *
from tkinter import ttk
from db.dbfile import DBManipulate
#from db.mydbfile import DBManipulate as kk
#import tkinter as tk


root_window=Tk()

root_window.title("Student Management System")
root_window.geometry("500x500")
#root_window.state("zoomed")
imgdir1=os.path.join(os.path.dirname(__file__),'img')
root_window.wm_iconbitmap('sms.ico')

imgdir=os.path.join((os.path.join(os.path.dirname(__file__),'img')),"image.gif")
getTitleImage=PhotoImage('titleimage',file=imgdir)

titleImageFrame=Frame(root_window, bg="white")#, height=200)
titleImageFrame.pack(padx=10,fill="both")

lblDisplayTitleImage=Label(titleImageFrame,image=getTitleImage).pack()

#mydbcon=kk()
mydbcon=DBManipulate()


def quit():
    root_window.destroy

def New():
    nw=Tk()
    nw.geometry("500x500")
    nw.title("New File")
    
    nw.mainloop()
    
def about_notpad():
    abt=Tk()
    abt.geometry("500x500")
    abt.title("About Us")
    message="""Windows Notepad is a simple text editor for Windows;
               it creates and edits plain text documents.
               First released in 1983 to commercialize the computer mouse in MS-DOS, 
               Notepad has been part of every version of Windows ever since. """
    intinfo=Label(abt,text=message)
    intinfo.pack()
    abt.mainloop()


menubar=Menu(root_window)

submenu=Menu(menubar,tearoff=0) 


# submenu.add_command(label="Zoom In",underline=0,accelerator="ctrl+plus")
# submenu.add_command(label="Zoom Out",underline=0,accelerator="ctrl+minus")
# submenu.add_command(label="Restore Default Zoom",underline=0,accelerator="ctrl+0")




                               
filemenu=Menu(menubar,tearoff=0)                  
menubar.add_cascade(label="File",underline=0,menu=filemenu)       
filemenu.add_command(label="New",underline=0,accelerator="Ctrl+N",command=New)             
filemenu.add_command(label="New Window",underline=0,accelerator="Ctrl+Shift+N")
filemenu.add_command(label="Open",underline=0,accelerator="Ctrl+O")
filemenu.add_command(label="Save",underline=0,accelerator="Ctrl+S")
filemenu.add_command(label="Save As",underline=0,accelerator="Ctrl+Shift+S")
filemenu.add_separator()
filemenu.add_command(label="Page Setup",underline=0)
filemenu.add_command(label="Print",underline=0,accelerator="Ctrl+P")
filemenu.add_separator()
filemenu.add_command(label="Exit",underline=0,command=quit)


editmenu=Menu(menubar,tearoff=0)                  
menubar.add_cascade(label="Edit",underline=0,menu=editmenu)        
editmenu.add_command(label="Undo",underline=0,accelerator="Ctrl+Z")  
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


formatmenu=Menu(menubar,tearoff=0)                  
menubar.add_cascade(label="Format",underline=0,menu=formatmenu)
formatmenu.add_command(label="Word Wrap",underline=0)
formatmenu.add_command(label="Font",underline=0)

viewmenu=Menu(menubar,tearoff=0)                
menubar.add_cascade(label="View",underline=0,menu=viewmenu)
viewmenu.add_cascade(label="Zoom",underline=0,menu=submenu)
viewmenu.add_command(label="Status",underline=0)
# viewmenu.add_checkbutton(label="Show Done", onvalue=1, offvalue=0)
#view submenu
submenu.add_command(label="Zoom In",underline=0,accelerator="ctrl+plus")
submenu.add_command(label="Zoom Out",underline=0,accelerator="ctrl+minus")
submenu.add_command(label="Restore Default Zoom",underline=0,accelerator="ctrl+0")


helpmenu=Menu(menubar,tearoff=0)                
menubar.add_cascade(label="Help",underline=0,menu=helpmenu)
helpmenu.add_command(label="View Help",underline=0)
helpmenu.add_command(label="Send Feedback",underline=0)
helpmenu.add_separator()
helpmenu.add_command(label="About Notpad",underline=0,command=about_notpad)







root_window.config(menu=menubar)





tablist=ttk.Notebook(root_window)
tablist.pack(padx=10, pady=5)

tabInsert=ttk.Frame(tablist, width=root_window.winfo_screenwidth(), height=root_window.winfo_screenheight())
tabInsert.pack()

tabUpdate=ttk.Frame(tablist, width=root_window.winfo_screenwidth(), height=root_window.winfo_screenheight())
tabUpdate.pack()

tabDelete=ttk.Frame(tablist, width=root_window.winfo_screenwidth(), height=root_window.winfo_screenheight())
tabDelete.pack()

tablist.add(tabInsert,text="Insert")
tablist.add(tabUpdate,text="Update")
tablist.add(tabDelete,text="Delete")


titledisplayframeintab=Frame(tabInsert,width=root_window.winfo_screenwidth(), height=root_window.winfo_screenheight())
titledisplayframeintab.pack()

lbl_insertTitle=Label(titledisplayframeintab, text="Inserting Student Details")
lbl_insertTitle.grid(pady=10,row=0, columnspan=10)

lbl_StdName=Label(titledisplayframeintab,text="Name of the student ")
lbl_StdName.grid(pady=10,row=1,column=1)
Ety_StdName=Entry(titledisplayframeintab)
Ety_StdName.grid(padx=10,pady=10,row=1, column=2)



lbl_StdMkTamil=Label(titledisplayframeintab,text="Tamil")
lbl_StdMkTamil.grid(pady=10,row=2,column=1)
Ety_StdMkTamil=Entry(titledisplayframeintab)
Ety_StdMkTamil.grid(padx=10,pady=10,row=2, column=2)


lbl_StdMkEng=Label(titledisplayframeintab,text="Eng")
lbl_StdMkEng.grid(pady=10,row=3,column=1)
Ety_StdMkEng=Entry(titledisplayframeintab)
Ety_StdMkEng.grid(padx=10,pady=10,row=3, column=2)

lbl_StdMkMath=Label(titledisplayframeintab,text="Math")
lbl_StdMkMath.grid(pady=10,row=4,column=1)
Ety_StdMkMath=Entry(titledisplayframeintab)
Ety_StdMkMath.grid(padx=10,pady=10,row=4, column=2)

lbl_StdMkSci=Label(titledisplayframeintab,text="Sci")
lbl_StdMkSci.grid(pady=10,row=5,column=1)
Ety_StdMkSci=Entry(titledisplayframeintab)
Ety_StdMkSci.grid(padx=10,pady=10,row=5, column=2)


lbl_StdMkSS=Label(titledisplayframeintab,text="SS")
lbl_StdMkSS.grid(pady=10,row=6,column=1)
Ety_StdMkSS=Entry(titledisplayframeintab)
Ety_StdMkSS.grid(padx=10,pady=10,row=6, column=2)

btn_Insert=Button(titledisplayframeintab, text="Insert")
btn_Insert.grid(row=7,column=1)

btn_Clear=Button(titledisplayframeintab, text="Clear")
btn_Clear.grid(row=7,column=2)

btn_Exit=Button(titledisplayframeintab, text="Quit", command=quit)
btn_Exit.grid(row=7,column=3)

msg=mydbcon.returnMsg()
# lblConMsg=Label(titledisplayframeintab, text=msg)
# lblConMsg.grid(row=8,column=2, pady=20)


root_window.mainloop()
