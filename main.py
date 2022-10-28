import tkinter as tk
import pyglet, os
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
import winsound
from winsound import *
play=lambda:PlaySound('mixkit-alert-quick-chime-766.wav',SND_FILENAME)

#2nd window
tkWindow = Tk()
tkWindow.geometry('800x500')
tkWindow.title('Log in ')


#Email_address label and text entry box
title=Label(tkWindow,text="Log In",font=('Berlin Sans FB Demi', 25)).pack()
Email_addressLabel = Label(tkWindow, text="Email address",font=('Times New Roman',10)).place(x=340, y=150)
Email_address = StringVar()
Email_addressEntry = Entry(tkWindow,textvariable=Email_address,width=40)
Email_addressEntry.place(x=380,y=190,anchor=CENTER)
Email_addressEntry.insert(0, 'Enter email')


#password label and password entry box
passwordLabel = Label(tkWindow,text="Password",font=('Times New Roman',10)).place(x=340,y=220)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password,width=40)
passwordEntry.place(x=380,y=260,anchor=CENTER)
passwordEntry.insert(0, 'Enter password')


def validateSubmit(Email_address, password):
	print("Email address entered :", Email_address.get())
	print("password entered :", password.get())
	return
# call function when we click on entry box
def click1(*args):
    Email_addressEntry.delete(0, 'end')

def click2(*args):
    passwordEntry.delete(0, 'end')

#submit button
submitButton = Button(tkWindow, text="Submit",width=20,bg='blue',fg='white',font=('Times New Roman',10), command=validateSubmit).place(x=290,y=300)

def Delete(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0, select['id'])
    e2.insert(0, select['studentname'])
    e3.insert(0, select['course'])
    e4.insert(0, select['fee'])


def Add():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="school")
    mycursor = mysqldb.cursor()

    try:

        sql = "INSERT INTO record (id,stname,course,fee) VALUES (%s, %s, %s, %s)"
        val = (studid, studname, coursename, feee)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Info", "Registration done successfully ")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def update():
    studid = e1.get()
    studname = e2.get()
    coursename = e3.get()
    feee = e4.get()
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="school")
    mycursor = mysqldb.cursor()

    try:
        sql = "Update  record set stname= %s,course= %s,fee= %s where id= %s"
        val = (studname, coursename, feee, studid)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Info", "Changed done successfully")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:

         print(e)
         mysqldb.rollback()
         mysqldb.close()

def delete():
    studid = e1.get()

    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="school")
    mycursor = mysqldb.cursor()

    try:
        sql = "delete from record where id = %s"
        val = (studid,)
        mycursor.execute(sql, val)
        mysqldb.commit()
        lastid = mycursor.lastrowid
        messagebox.showinfo("Info", "Deleted done successfully")

        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e1.focus_set()

    except Exception as e:

        print(e)
        mysqldb.rollback()
        mysqldb.close()


def show():
    mysqldb = mysql.connector.connect(host="localhost", user="root", password="", database="school")
    mycursor = mysqldb.cursor()
    mycursor.execute("SELECT id,stname,course,fee FROM record")
    records = mycursor.fetchall()
    print(records)

    for i, (id, stname, course, fee) in enumerate(records, start=1):
        listBox.insert("", "end", values=(id, stname, course, fee))
        mysqldb.close()

#design part
root = Tk()
root.geometry("800x500")
root.title('Registration')
root['bg']='lightpink'
global e1
global e2
global e3
global e4
tk.Label(root, text="Student Registration System ", fg="deeppink3", font=('Berlin Sans FB Demi',25),bg="lightpink").place(x=320, y=50)
tk.Label(root, text="Student ID",fg="deeppink3",font=('Times New Roman',10),bg="lightpink").place(x=10, y=10)
Label(root, text="Student Name",fg="deeppink3",font=('Times New Roman',10),bg="lightpink").place(x=10, y=40)
Label(root, text="Course",fg="deeppink3",font=('Times New Roman',10),bg="lightpink").place(x=10, y=70)
Label(root, text="Fee",fg="deeppink3",font=('Times New Roman',10),bg="lightpink").place(x=10, y=100)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

e3 = Entry(root)
e3.place(x=140, y=70)

e4 = Entry(root)
e4.place(x=140, y=100)

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

Button(root, text="Add", command=combine_funcs(play,Add), height=3, width=13,font=('Times New Roman',10),bg="mistyrose1",fg="deeppink3").place(x=30, y=130)
Button(root, text="Update", command=combine_funcs(play,update), height=3, width=13,font=('Times New Roman',10),bg="mistyrose1",fg="deeppink3").place(x=140, y=130)
Button(root, text="Delete", command=combine_funcs(play,delete), height=3, width=13,font=('Times New Roman',10),bg="mistyrose1",fg="deeppink3").place(x=250, y=130)

#هذا لاتحبرشين به ياروف ! انتبهي
cols = ('id', 'studentname', 'course', 'fee')
listBox = ttk.Treeview( root, columns=cols, show='headings')

for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=1, columnspan=2)
    listBox.place(x=10, y=200)

show()
listBox.bind('<Double-Button-1>',Delete)

root.mainloop()