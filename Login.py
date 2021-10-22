# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 09:48:13 2021

@author: faish
"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from imp import reload
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Admin login")
        self.root.geometry("1169x600")
        #====login frame====
        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=100,y=150,height=400,width=500)
        title=Label(Frame_login,text="Admin Login",font=("Impact",35,"bold"),fg="gray",bg="white").place(x=90,y=40)
        desc=Label(Frame_login,text="Fill username and password here",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=100)
        #====Username module====
        lbl_username=Label(Frame_login,text="Username",font=("Impact",15),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170, width=350, height=35)
        #====Password module====
        lbl_password=Label(Frame_login,text="Password",font=("Impact",15),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,show="*",font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240, width=350, height=35)
        #====Button====
        forget_btn=Button(Frame_login,text="Forgot password?",bg="white",fg="gray",bd=0,font=("times new roman",12)).place(x=90,y=280)
        login_btn=Button(Frame_login,command=self.login_function,text="login",bg="white",fg="gray",font=("times new roman",15)).place(x=90,y=320)
    def login_function(self):
        if self.txt_user.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        elif self.txt_user.get()!="Admin" or self.txt_pass.get()!="1234":
            messagebox.showerror("Error","Invalid Username/password", parent=self.root)
        else:
            messagebox.showinfo("Welcome","Welcome Admin")
            import loginPage
            reload(loginPage)
         
root=Tk()
obj=Login(root)              
root.mainloop()