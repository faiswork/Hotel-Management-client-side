from tkinter import*
from PIL import ImageTk
class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.root.geometry("1169x600+100+50")
        self.root.resizable(False,False)
        # background image code
        # self.bg=ImageTk.PhotoImage(file="images\wxyz.jpg")
        # self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        #frames code
        Frame_login=Frame(self.root,bg="sky blue")
        Frame_login.place(x=50,y=50,height=500,width=800)

        #Labels
        title=Label(Frame_login,text="MAIN MENU",font=("Arial black",45,"bold"),fg="blue",bg="sky blue").place(x=220,y=0)
        # label_roomAvail = Label(Frame_login, text="ROOM AVAILABILITY",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=30,y=120)
        # label_checkOUT = Label(Frame_login,text="CHECK OUT",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=550,y=120)
        # label_cabBook = Label(Frame_login,text="BOOK A CAB",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=30,y=350)
        # label_billing = Label(Frame_login,text="BILLING",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=550,y=350)

        #BUTTONS CODE
        roomAvail=Button(Frame_login,text="ROOM AVAILABILITY",bg="white",fg="black",bd=0,font=("Goudy old style",28)).place(x=30,y=140)
        checkOut = Button(Frame_login,text="CHECK-OUT",bg="white",fg="black",bd=0,font=("Goudy old style",28)).place(x=530,y=140)
        cabBook = Button(Frame_login,text="CAB BOOK",bg="white",fg="black",bd=0,font=("Goudy old style",28)).place(x=100,y=310)
        billing = Button(Frame_login,text="BILLING",bg="white",fg="black",bd=0,font=("Goudy old style",28)).place(x=560,y=310)
root=Tk()
obj= login(root)
root.mainloop()
