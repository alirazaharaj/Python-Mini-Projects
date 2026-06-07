from tkinter import *
import os


def res():
    os.system('shutdown /r /t 1')

def rest():
    os.system('shutdown /s /t 20')

def logout():
    os.system('shutdown -1')

def shut():
    os.system('shutdown /s /t 1')

app=Tk()

app.title('Shut Down App')
app.geometry('400x550')
app.config(bg='white')

la_name=Label(app,text='Shut Down App',font=('Lucida Handwriting',25,'bold'))
la_name.config(bg='white')
la_name.pack(pady=10)

rb=Button(app,text='Restart',font=('Lucida Handwriting',25,'bold'),relief=RAISED,command=res)
rb.pack(pady=(50,0))

tr=Button(app,text='Restart.Time',font=('Lucida Handwriting',25,'bold'),relief=RAISED,command=rest)
tr.pack(pady=(30,0))

log=Button(app,text='Logout',font=('Lucida Handwriting',25,'bold'),relief=RAISED,command=logout)
log.pack(pady=(30,0))

Shut=Button(app,text='Shutdown',font=('Lucida Handwriting',25,'bold'),relief=RAISED,command=shut)
Shut.pack(pady=(30,0))

app.mainloop()
