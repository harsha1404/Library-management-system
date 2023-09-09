from tkinter import *
from tkinter import messagebox
import ast
from signup import*

root=Tk()
root.title('login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

def sign_up():
    execfile('signup.py')
    
def signin():
    username=user.get()
    password=code.get()
    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    if username == 'admin' and password == '1234':
        execfile('main.py')
    if username in r.keys() and password == r[username]:
        execfile('customer.py')
    else:
        messagebox.showerror("Invalid","invalid usename and password")


img=PhotoImage(file='login.jpg')
Label(root,image=img,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height='350',bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='log in',fg='#57a1f8',bg='white',font=('Microsoft YaHei Light',23,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'usernname')
user= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Ariel',11,'bold'))
user.place(x=30,y=80)
user.insert(0,'username')
user.bind('<FocusIn>', on_enter)
user.bind('FocusOut',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        code.insert(0,'password')
code= Entry(frame,width=25,fg='black',border=0,bg='white',font=('Ariel',11,'bold'))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('FocusOut',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

Button(frame,width=39,pady=7,text='Log In',bg='#57a178',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Ariel',11))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup)
sign_up.place(x=215,y=270)
root.mainloop()