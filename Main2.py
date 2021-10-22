from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import sqlite3

root=Tk()
root.geometry("1196x600")
root.title("Hotel Management System")
#bg=PhotoImage(file ="D:\Python\HotelManagement\Background.png")
#bglabel=Label(root,image=bg)
#bglabel.place(x=0,y=0)
backimage=PhotoImage("D:\Python\HotelManagement\Back.png")
#====database
conn=sqlite3.connect('Hotel_Management.db')
c=conn.cursor()
# c.execute("""CREATE TABLE room(
#           Name varchar,
#           Phone_number varchar,
#           address varchar,
#           adhar varchar,
#           occupants varchar,
#           category varchar)""")
conn.commit()
conn.close()








class BookingPage:
    global root
    global backimage
    global confirm_function
    def __init__(self,root):
        self.root=root
        root.geometry("1196x600")
        root.title("Room Booking")
        #self.bag=PhotoImage(file ="D:\Python\HotelManagement\Background.png")
        #self.bglabel=Label(root,image=self.bag)
        #self.bglabel.place(x=0,y=0)
        self.pane=Canvas(root,bg="White",height=1000,width=800)
        self.pane.place(relx=0.5,y=500,anchor=CENTER)
        self.label=Label(root,text="Availability",bg="White",font=("Product Sans",20)).place(relx=0.5,rely=0.05,anchor=CENTER)
#====================================================================================================================================================================================================
        # Getting the number of occupants
        self.Occupants=StringVar()
        OccupantLabel=Label(root,text="Select Number of Occupants",bg="White",font=("Product Sans",12)).place(relx=0.3,rely=0.55)
        self.OccupantSelect=OptionMenu(root,self.Occupants,*["1","2","3"],command=self.NumOfOcc())
        self.OccupantSelect.config(indicatoron=0)
        self.OccupantSelect.configure(bg="White",highlightthickness=0,highlightbackground="White",borderwidth=0)
        self.OccupantSelect.place(relx=0.7,rely=0.55,anchor=CENTER)
        self.Occupants.set("1")
#====================================================================================================================================================================================================
        # choosing the category of the room
        self.Category=StringVar()
        self.CategoryLabel=Label(root,text="Select Category",bg="White",font=("Product Sans",12)).place(relx=0.3,rely=0.65)
        self.CategorySelect=OptionMenu(root,self.Category,*["A/C","Non A/C","Presidential Suite"])
        self.CategorySelect.config(indicatoron=0)
        self.CategorySelect.configure(bg="White",highlightthickness=0,highlightbackground="Grey",borderwidth=0)
        self.CategorySelect.place(relx=0.6,rely=0.65)
        self.Category.set("A/C")
#====================================================================================================================================================================================================
        # Info label

        self.InfoLabel=Label(root,bg="White",font=("Product Sans",12),text="")
        self.InfoLabel.place(relx=0.5,rely=0.5,anchor=CENTER)

        # Price Lablel
        self.PriceLabel=Label(root,bg="White",font=("Product Sans",12))
        self.PriceLabel.place(relx=0.5,rely=0.6,anchor=CENTER)
#====================================================================================================================================================================================================
        # Buttons
    
        self.IDProof=StringVar()
        self.IDProof.set("Aadhar")
        self.label=Label(root,text="Enter Customer Details",bg="White",font=("Product Sans",20)).place(relx=0.5,rely=0.05,anchor=CENTER)
        self.name=Label(root,text="Name",font=("Product Sans",12),bg="White").place(relx=0.3,rely=0.1)
        self.Number=Label(root,text="Phone Number",font=("Product Sans",12),bg="White").place(relx=0.3,rely=0.2)
        self.Address=Label(root,text="Address",font=("Product Sans",12),bg="White").place(relx=0.3,rely=0.3)
        self.ID=OptionMenu(root,self.IDProof,*["Aadhar","Driving Licence","Other"])
        self.ID.config(indicatoron=0,font=("Product Sans",12))
        self.ID.configure(bg="White",highlightthickness=0,highlightbackground="Grey",borderwidth=0)
        self.ID.place(relx=0.6,rely=0.4)
        self.IDLabel=Label(root,text="ID Proof",bg="White",font=("Product Sans",12)).place(relx=0.3,rely=0.4)
        self.EnterName=Entry(root,font=("Product Sans",12)).place(relx=0.6,rely=0.1)
        self.EnterNumber=Entry(root,font=("Product Sans",12)).place(relx=0.6,rely=0.2)
        self.EnterAddress=Entry(root,font=("Product Sans",12)).place(relx=0.6,rely=0.3)
        self.EnterIdProof=Entry(root,font=("Product Sans",12)).place(relx=0.6,rely=0.45)
        self.bookbutton=Button(root,text="Confirm",command=self.confirm_function)
        self.bookbutton.place(relx=0.5,rely=0.95,anchor=CENTER)
        self.Days=Label(root,text="No of days",font=("Product Sans",12),bg="White").place(relx=0.3,rely=0.75)
        self.Day=IntVar()
        self.DaysSelect=OptionMenu(root,self.Day,*[1,2,3,4])
        self.DaysSelect.config(indicatoron=0)
        self.DaysSelect.configure(bg="White",highlightthickness=0,highlightbackground="Grey",borderwidth=0)
        self.DaysSelect.place(relx=0.6,rely=0.75)
        self.Day.set(1)
        self.subtotal=Label(root,bg="white",font=("Product Sans",12))
        self.subtotal.place(relx=0.5,rely=0.85,anchor=CENTER)

    # def Book(self):  #Book Button Command
    #     self.RoomCategory=self.Category.get()
    #     self.days=self.Day.get()
    #     if self.RoomCategory=="Non A/C":
    #         price=1000
    #     elif self.RoomCategory=="A/C":
    #         price=1500
    #     elif self.RoomCategory=="Presidential Suite":
    #         price=2000
    #     self.totalPrice=price*self.days
    #     self.totalPrice=str(self.totalPrice)
    #     self.TXT=("Your subtotal will be "+self.totalPrice )
    #     self.subtotal.config(text=self.TXT)

    
    def ShowInfo(self):
        self.InfoLabel.config(text="Info will be shown")
        self.ShowBook()
    
    def NumOfOcc(self):
        NumberOfOccupants=self.Occupants.get()
        return NumberOfOccupants
    
    def RoomCategoryFun(self,Category):
        
        RoomCategory=self.Category.get()
        if RoomCategory=="Non A/C":
            self.PriceLabel.config(text="Price: 1000")
        elif RoomCategory=="A/C":
            self.PriceLabel.config(text="Price: 1500")
        elif RoomCategory=="Presidential Suite":
            self.PriceLabel.config(text="Price: 2000") 

            
    def Back(self):
        for widget in root.winfo_children():
            widget.destroy()
        SplashScreen(root)

    def FinalPage(self):
            for widget in root.winfo_children():
                widget.destroy()
            UserInfo(root)  

    # def BillingPage(self):
    #     self.newWindow = Toplevel(self.root)
    #     self.app = BillingPage(self.newWindow) 
    def confirm_function(self):
        conn=sqlite3.connect('Hotel_Management.db')
        c=conn.cursor()
        c.execute("INSERT INTO room VALUES(:Name,:Phone_number,:address,:adhar,:occupants,:category)",
                {
                    'Name':self.EnterName.get(),
                    'Phone_number':self.EnterNumber.get(),
                    'address':self.EnterAddress.get(),
                    'adhar':self.EnterIdProof.get(),
                    'occupants':self.Occupants.get(),
                    'category':self.Category.get()
                })
        conn.commit()
        conn.close()
    
    
    def delete(self):
        self.EnterName.delete(0,END)
        self.EnterAddress.delete(0,END)
        self.EnterIdProof.delete(0,END)
        self.En.delete(0,END)
    

class BillingPage:
    global root
    global backimage
    def __init__(self,root):
        self.root=root
        #self.bg=PhotoImage(file ="D:\Python\HotelManagement\Background.png")
        #self.bglabel=Label(root,image=bg)
        #self.bglabel.place(x=0,y=0)
#===========================================================================================================================================================================================================================
        
        self.label5=Label(root,text='BILL PAYMENT',borderwidth=1,relief='solid',width=12,height=3)
        self.label5.pack()
        self.label5.place(x=460,y=30)
        self.label6 = Label(root, borderwidth=5, relief='solid', width=50, height=20)
        self.label6.pack()
        self.label6.place(x=500, y=120)
        self.pay=StringVar()
        self.payno=IntVar()
        self.r1=Radiobutton(root,text='PAY WITH CREDIT CARD',variable=self.payno,value=1)
        self.r1.pack()
        self.r1.place(x=20,y=100)
        self.r2 = Radiobutton(root, text='CASH', variable=self.payno, value=2)
        self.r2.pack()
        self.r2.place(x=20,y=170)
        self.r3 = Radiobutton(root, text='ONLINE PAYMENT', variable=self.payno, value=3)
        self.r3.pack()
        self.r3.place(x=20,y=240)
        def fun_pay(self):
            self.messagebox.showinfo('Hello','THANKS FOR CHOOSING\nOUR HOTEL\n\n\nPAYMENT DONE SUCCESSFULLY')
        self.b = Label(root, text="PAY NOW", foreground="blue", bg='pink', activebackground="red", width=10, height=2)
        self.b.pack()
        self.b.place(x=50,y=420)
        self.backbutton=Button(root,text="Back",image=backimage,command=self.Back,compound=LEFT)
        self.backbutton.place(relx=0.1,rely=0.1,anchor=CENTER)

    def Back(self):
            for widget in root.winfo_children():
                widget.destroy()
            SplashScreen(root)       

class Login:
    def WelcomePage(self):
        for widget in root.winfo_children():
            widget.destroy()
        SplashScreen(root)


    def __init__(self,root):
        self.root=root
        self.root.title("Admin login")
        self.root.geometry("1169x600")
        #====login frame====
        root=Frame(self.root,bg="white")
        root.place(x=100,y=150,height=400,width=500)
        title=Label(root,text="Admin Login",font=("Impact",35,"bold"),fg="gray",bg="white").place(x=90,y=40)
        desc=Label(root,text="Fill username and password here",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=100)
        #====Username module====
        lbl_username=Label(root,text="Username",font=("Impact",15),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=Entry(root,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170, width=350, height=35)
        #====Password module====
        lbl_password=Label(root,text="Password",font=("Impact",15),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(root,show="*",font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240, width=350, height=35)
        #====Button====
        forget_btn=Button(root,text="Forgot password?",bg="white",fg="gray",bd=0,font=("times new roman",12)).place(x=90,y=280)
        login_btn=Button(root,command=self.login_function,text="login",bg="white",fg="gray",font=("times new roman",15)).place(x=90,y=320)
    def login_function(self):
        if self.txt_user.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All fields are required", parent=self.root)
        elif self.txt_user.get()!="Admin" or self.txt_pass.get()!="1234":
            messagebox.showerror("Error","Invalid Username/password", parent=self.root)
        else:
            messagebox.showinfo("Welcome","Welcome Admin")
            self.WelcomePage()
        
    
class SplashScreen:

    global root
    
    
    def Booking(self):
        for widget in root.winfo_children():
            widget.destroy()
        BookingPage(root)
    
    def Billing(self):
        for widget in root.winfo_children():
            widget.destroy()
        BillingPage(root)
    
    def Cab(self):
        for widget in root.winfo_children():
            widget.destroy()
        SplashScreen(root)
    
    def LogOut(self):
        for widget in root.winfo_children():
            widget.destroy()
        Login(root)

    
    def __init__(self,root):
        self.root=root
        #self.root.title("Login Page")
        #self.bag=PhotoImage(file ="D:\Python\HotelManagement\Background.png")
        #self.bglabel=Label(root,image=self.bag)
        #self.bglabel.place(x=0,y=0)

        #frames code

        #Labels
        title=Label(root,text="MAIN MENU",font=("Arial black",45,"bold"),fg="blue",bg="sky blue").place(x=220,y=0)
        # label_roomAvail = Label(root, text="ROOM AVAILABILITY",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=30,y=120)
        # label_checkOUT = Label(root,text="CHECK OUT",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=550,y=120)
        # label_cabBook = Label(root,text="BOOK A CAB",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=30,y=350)
        # label_billing = Label(root,text="BILLING",font=("Goudy old style",20,"bold"),fg="black",bg="white").place(x=550,y=350)

        #BUTTONS CODE
        roomAvail=Button(root,text="ROOM AVAILABILITY",bg="white",fg="black",bd=0,font=("Goudy old style",28),command=self.Booking).place(x=30,y=140)
        checkOut = Button(root,text="CHECK-OUT",bg="white",fg="black",bd=0,font=("Goudy old style",28),command=self.Billing).place(x=530,y=140)
        #cabBook = Button(root,text="CAB BOOK",bg="white",fg="black",bd=0,font=("Goudy old style",28),command=self.Cab).place(x=100,y=310)
        billing = Button(root,text="Log Out",bg="white",fg="black",bd=0,font=("Goudy old style",28),command=self.LogOut).place(x=560,y=310)

class UserInfo:
    global root
    global backimage
    def __init__(self,root):
        self.root=root
        root.geometry("1196x600")
        root.title("Room Booking")
        #self.bag=PhotoImage(file ="D:\Python\HotelManagement\Background.png")
        #self.bglabel=Label(root,image=self.bag)
        #self.bglabel.place(x=0,y=0)
        self.pane=Canvas(root,bg="White",height=1000,width=800)
        self.pane.place(relx=0.5,y=500,anchor=CENTER)
        self.IDProof=StringVar()
        self.IDProof.set("Aadhar")
        self.label=Label(root,text="Enter Customer Details",bg="White",font=("Product Sans",20)).place(relx=0.5,rely=0.05,anchor=CENTER)
        self.name=Label(root,text="Name",font=("Product Sans",14),bg="White").place(relx=0.3,rely=0.2)
        self.Number=Label(root,text="Phone Number",font=("Product Sans",14),bg="White").place(relx=0.3,rely=0.3)
        self.Address=Label(root,text="Address",font=("Product Sans",14),bg="White").place(relx=0.3,rely=0.4)
        self.ID=OptionMenu(root,self.IDProof,*["Aadhar","Driving Licence","Other"])
        self.ID.config(indicatoron=0,font=("Product Sans",12))
        self.ID.configure(bg="White",highlightthickness=0,highlightbackground="Grey",borderwidth=0)
        self.ID.place(relx=0.6,rely=0.5)
        self.IDLabel=Label(root,text="ID Proof",bg="White",font=("Product Sans",14)).place(relx=0.3,rely=0.5)
        self.EnterName=Entry(root,font=("Product Sans",12)).place(relx=0.6,rely=0.2)
        self.EnterNumber=Entry(root,font=("Product Sans",12)).place(relx=0.6,rely=0.3)
        self.EnterAddress=Entry(root,font=("Product Sans",12)).place(relx=0.6,rely=0.4)
        self.EnterIdProof=Entry(root,font=("Product Sans",12)).place(relx=0.6,rely=0.6)
        self.bookbutton=Button(root,text="Confirm",command=self.Book)
        self.bookbutton.place(relx=0.5,rely=0.9,anchor=CENTER)

    def Book(self):  #Book Button Command
        pass



        # self.name=Label(root,text="Name",font=("Product Sans",14),bg="White").place(relx=0.3,rely=0.3,anchor=CENTER)
# class Cab:
#     global root
#     def __init__(self):

#         root=Tk()
#         root.geometry("1200x600")
#         self.f1=Frame(root,bg="black",borderwidth=6,relief=RIDGE)
#         self.f1.pack(side=TOP,fill="y",pady=20)
#         self.l1=Label(self.f1,text="WELCOME TO OUR CAB SERVICES",fg="red",padx=13,pady=13,font="comicsansms 25 bold",borderwidth=3)
#         self.l1.pack(fill="x")
#         self.f2=Frame(root,bg="PINK",borderwidth=6,relief=RIDGE)
#         self.f2.pack(side=LEFT,fill=Y,pady=20)
#         self.l2=Label(f2,text="CUSTOMER DETAILS ",fg="RED",padx=30,pady=30,font="comicsansms 19 bold",borderwidth=3)
#         self.l2.grid(row=0,column=0)
#         self.f3=Frame(root,bg="PINK",borderwidth=6,relief=RIDGE)
#         self.f3.pack(fill=Y,side=LEFT,padx=30,pady=20)
#         self.l3=Label(f3,text="BOOKING DETAILS",fg="RED",padx=30,pady=30,font="comicsansms 19 bold",borderwidth=3)
#         self.l3.grid(row=0,column=0)
#         self.f4=Frame(root,bg="pink",borderwidth=6,relief=RIDGE)
#         self.f4.pack(fill=Y,side=LEFT,pady=20)
#         self.l4=Label(f4,text="RECEIPT",fg="RED",padx=30,pady=30,font="comicsansms 19 bold",borderwidth=3)
#         self.l4.grid()
#         #text for  2nd frame
#         self.name=Label(f2,text="NAME",font="comicsansma 15 bold")
#         self.gender=Label(f2,text="GENDER",font="comicsansma 15 bold")
#         self.address=Label(f2,text="ADDRESS",font="comicsansma 15 bold")
#         self.mobile=Label(f2,text="MOBILE",font="comicsansma 15 bold")
#         self.email=Label(f2,text="EMAIL",font="comicsansma 15 bold")
#         #pack text for 2nd frame
#         self.name.grid(row=1,column=0,sticky=W,pady=2,padx=2)
#         self.gender.grid(row=2,column=0,sticky=W,pady=6,padx=2)
#         self.address.grid(row=3,column=0,sticky=W,pady=6,padx=2)
#         self.mobile.grid(row=4,column=0,sticky=W,pady=6,padx=2)
#         self.email.grid(row=5,column=0,sticky=W,pady=6,padx=2)
#         #variables for 2nd frame
#         """namevalue=StringVar()
#         gendervalue=StringVar()
#         addressvalue=StringVar()
#         mobilevalue=StringVar()
#         emailvalue=StringVar()"""
#         #entries for 2nd frame
#         self.nameentry=Entry(f2)
#         self.genderentry=Entry(f2)
#         self.addressentry=Entry(f2)
#         self.mobileentry=Entry(f2)
#         self.emailentry=Entry(f2)
#         #packing entries for 2nd frame
#         self.nameentry.grid(row=1,column=0,pady=2)
#         self.genderentry.grid(row=2,column=0,pady=6)
#         self.addressentry.grid(row=3,column=0,pady=6)
#         self.mobileentry.grid(row=4,column=0,pady=6,padx=4)
#         self.emailentry.grid(row=5,column=0,pady=6)
#         #buttons for 2nd frame
#         self.b1=Button(f2, text="SUBMIT", foreground="RED", bg='sky blue', activebackground="YELLOW", width=12, height=2)
#         self.b1.grid()
#         self.b1.place(x=50,y=410,anchor=S)
#         self.b2=Button(f2, text="CANCEL", foreground="RED", bg='sky blue', activebackground="YELLOW", width=12, height=2)
#         self.b2.grid()
#         self.b2.place(x=270,y=410,anchor=S)
#         #text for 3rd frame
#         self.pickup=Label(f3,text="PICKUP",font="comicsansma 12 bold")
#         self.drop=Label(f3,text="DROP",font="comicsansma 12 bold")
#         self.pooling=Label(f3,text="POOLING",font="comicsansma 12 bold")
#         self.luggage=Label(f3,text="LUGGAGE",font="comicsansma 12 bold")
#         self.car=Label(f3,text="CAR TYPE",font="comicsansma 12 bold")
#         #pack text for 3RD frame
#         self.pickup.grid(row=1,column=0,sticky=W,pady=6,padx=2)
#         self.drop.grid(row=2,column=0,sticky=W,pady=6,padx=2)
#         self.pooling.grid(row=3,column=0,sticky=W,pady=6,padx=2)
#         self.luggage.grid(row=4,column=0,sticky=W,pady=6,padx=2)
#         self.car.grid(row=5,column=0,sticky=W,pady=6,padx=2)
#         #entries for 3RD frame
#         self.pickupentry=Entry(f3)
#         self.dropentry=Entry(f3)
#         self.poolingentry=Entry(f3)
#         self.luggageentry=Entry(f3)
#         self.carentry=Entry(f3)
#         #packing entries for 3RD frame
#         self.pickupentry.grid(row=1,column=0,pady=2)
#         self.dropentry.grid(row=2,column=0,pady=6)
#         self.poolingentry.grid(row=3,column=0,pady=16,padx=16)
#         self.luggageentry.grid(row=4,column=0,pady=6,padx=4)
#         self.carentry.grid(row=5,column=0,pady=6)
#         #buttons for 3rd frame
#         self.b1=Button(f3, text="SUBMIT", foreground="RED", bg='sky blue', activebackground="YELLOW", width=12, height=2)
#         self.b1.grid()
#         self.b1.place(x=50,y=410,anchor=S)
#         self.b2=Button(f3, text="CANCEL", foreground="RED", bg='sky blue', activebackground="YELLOW", width=12, height=2)
#         self.b2.grid()
#         self.b2.place(x=240,y=410,anchor=S)
#         #buttons for 4th frame
#         self.b1=Button(f4, text="TOTAL", foreground="RED", bg='sky blue', activebackground="YELLOW", width=12, height=2)
#         self.b1.grid()
#         self.b1.place(x=50,y=250,anchor=S)
#         self.b2=Button(f4, text="RECIEPT", foreground="RED", bg='sky blue', activebackground="YELLOW", width=12, height=2)
#         self.b2.grid()
#         self.b2.place(x=50,y=300,anchor=S)
#         self.b3=Button(f4, text="RESET", foreground="RED", bg='sky blue', activebackground="YELLOW", width=12, height=2)
#         self.b3.grid()
#         self.b3.place(x=50,y=350,anchor=S)
#         self.b4=Button(f4, text="EXIT", foreground="RED", bg='sky blue', activebackground="YELLOW", width=12, height=2)
#         self.b4.grid()
#         self.b4.place(x=50,y=400,anchor=S)
    
Login(root)
root.mainloop()
