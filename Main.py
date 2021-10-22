
from sqlite3.dbapi2 import ProgrammingError
from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
import sqlite3 as lite

root=Tk()
root.geometry("1196x600")
root.title("Hotel Management System")
#bg=PhotoImage(file ="HotelManagement\Background.png")
#bglabel=Label(root,image=bg)
#bglabel.place(x=0,y=0)
#backimage=PhotoImage(file="HotelManagement\Back.png")



conn=lite.connect("HotelManagement\Hotel_Management.db")
#  
c=conn.cursor()
# 
conn.commit()
# 

class BookingPage:
    global root
    global backimage
    def __init__(self,root):
        self.root=root
        root.geometry("1196x600")
        root.title("Room Booking")
        #self.bag=PhotoImage(file ="HotelManagement\Background.png")
        #self.bglabel=Label(root,image=self.bag)
        #self.bglabel.place(x=0,y=0)
        self.pane=Canvas(root,bg="White",height=1000,width=800)
        self.pane.place(relx=0.5,y=500,anchor=CENTER)
        self.label=Label(root,text="Availability",bg="White",font=("Product Sans",20)).place(relx=0.5,rely=0.05,anchor=CENTER)
#====================================================================================================================================================================================================
        # Getting the number of occupants
        self.Occupants=StringVar()
        OccupantLabel=Label(root,text="Select Number of Occupants",bg="White",font=("Product Sans",12)).place(relx=0.3,rely=0.4)
        self.OccupantSelect=OptionMenu(root,self.Occupants,*["1","2","3"],command=self.NumOfOcc())
        self.OccupantSelect.config(indicatoron=0)
        self.OccupantSelect.configure(bg="White",highlightthickness=0,highlightbackground="White",borderwidth=0)
        self.OccupantSelect.place(relx=0.6,rely=0.4,)
        self.Occupants.set("1")
#====================================================================================================================================================================================================
        # choosing the category of the room
        self.Category=StringVar()
        self.CategoryLabel=Label(root,text="Select Category",bg="White",font=("Product Sans",12)).place(relx=0.3,rely=0.5)
        self.CategorySelect=OptionMenu(root,self.Category,*["A/C","Non A/C","Presidential Suite"],command=self.showinfo)
        self.CategorySelect.config(indicatoron=0)
        self.CategorySelect.configure(bg="White",highlightthickness=0,highlightbackground="Grey",borderwidth=0)
        self.CategorySelect.place(relx=0.6,rely=0.5)
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
    
        self.label=Label(root,text="Enter Customer Details",bg="White",font=("Product Sans",20)).place(relx=0.5,rely=0.05,anchor=CENTER)
        self.name=Label(root,text="Name",font=("Product Sans",12),bg="White").place(relx=0.3,rely=0.1)
        self.Number=Label(root,text="Phone Number",font=("Product Sans",12),bg="White").place(relx=0.3,rely=0.2)
        self.Address=Label(root,text="Address",font=("Product Sans",12),bg="White").place(relx=0.3,rely=0.3)
        self.EnterName=Entry(root,font=("Product Sans",12),fg="Black",bg="light gray")
        self.EnterName.place(relx=0.6,rely=0.1)
        self.EnterNumber=Entry(root,font=("Product Sans",12),fg="Black",bg="light gray")
        self.EnterNumber.place(relx=0.6,rely=0.2)
        self.EnterAddress=Entry(root,font=("Product Sans",12),fg="Black",bg="light gray")
        self.EnterAddress.place(relx=0.6,rely=0.3)
        self.BackButton=Button(root,image=backimage,command=self.Back,borderwidth=0,background="White")
        self.BackButton.place(relx=0.2,rely=0.03)
        self.bookbutton=Button(root,text="Confirm",command=self.Book)
        self.bookbutton.place(relx=0.5,rely=0.95,anchor=CENTER)
        self.Days=Label(root,text="No of days",font=("Product Sans",12),bg="White").place(relx=0.3,rely=0.6)
        self.Day=IntVar()
        self.DaysSelect=OptionMenu(root,self.Day,*[1,2,3,4],command=self.showinfo)
        self.DaysSelect.config(indicatoron=0)
        self.DaysSelect.configure(bg="White",highlightthickness=0,highlightbackground="Grey",borderwidth=0)
        self.DaysSelect.place(relx=0.6,rely=0.6)
        self.Day.set(1)
        self.subtotal=Label(root,bg="white",font=("Product Sans",12))
        self.subtotal.place(relx=0.5,rely=0.8,anchor=CENTER)

    def showinfo(self,Category):
        self.RoomCategory=self.Category.get()
        self.days=self.Day.get()
        if self.RoomCategory=="Non A/C":
            price=1000
        elif self.RoomCategory=="A/C":
            price=1500
        elif self.RoomCategory=="Presidential Suite":
            price=2000
        self.totalPrice=price*self.days
        self.totalPrice=str(self.totalPrice)
        self.TXT=("Your subtotal will be "+self.totalPrice )
        self.subtotal.config(text=self.TXT)
    
    def Book(self):  #Book Button Command
        c.execute("Select Rno from Available where Category=? and Avail=? ORDER by Rno LIMIT 1",(self.Category.get(),"A"))
        conn.commit()
        self.roomnumber=c.fetchone()
        self.room=self.roomnumber[0]
        self.room=str(self.room)
        print(self.room)
        if self.roomnumber!=[]:
            if (self.EnterName.get()=="" or self.EnterNumber.get()=="" or self.EnterAddress.get()==""):
                messagebox.showerror("Error","Fill all the required Fields", parent=self.root)
            else:
                try:
                    self.showinfo(self.Category)
                    c.execute("INSERT INTO Details (Name,Number,Address,Occupants,Category,Days,Subtotal) VALUES(?,?,?,?,?,?,?)",(self.EnterName.get(),self.EnterNumber.get(),self.EnterAddress.get(),self.Occupants.get(),self.Category.get(),self.Day.get(),self.totalPrice))
                    conn.commit()
                    c.execute("UPDATE Available SET Avail=? WHERE Rno=?",("N",self.room))
                    conn.commit()
                    c.execute("Update Details SET Rno=? where Number=?",(self.room,self.EnterNumber.get()) )
                    conn.commit()
                    self.roomnumberinfo="Your Room Number is: "+self.room
                    messagebox.showinfo("Booking Successful",self.roomnumberinfo,parent=self.root)
                except:
                    messagebox.showerror("Error","Some Error Occured", parent=self.root)
        else:
            print(self.roomnumber)
            messagebox.showerror("Error","Room Not Available", parent=self.root)
    
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

     

    # def BillingPage(self):
    #     self.newWindow = Toplevel(self.root)
    #     self.app = BillingPage(self.newWindow) 

class BillingPage:
    global root
    global backimage
    def __init__(self,root):
        self.root=root
        self.root.title("Login Page")
        self.bag=PhotoImage(file ="HotelManagement\Background.png")
        self.bglabel=Label(root,image=self.bag)
        self.bglabel.place(x=0,y=0)

        self.cnv=Canvas(root,bg="White",height=600,width=600,highlightthickness=0)
        self.cnv.place(relx=0.5,rely=0.5,anchor=CENTER)

#===========================================================================================================================================================================================================================
        self.RoomLabel=Label(self.cnv,text='Room Number',font=("Product Sans",12),borderwidth=0,width=12,height=3,bg="White")
        self.RoomLabel.place(relx=0.3,rely=0.15,anchor=CENTER)
        self.RoomEntry=Entry(self.cnv,font=("Product Sans",12),background="Light gray",fg="Black")
        self.RoomEntry.place(relx=0.7,rely=0.15,anchor=CENTER)
        self.label5=Label(self.cnv,text='BILL PAYMENT',font=("Product Sans",20),borderwidth=0,width=12,height=3,bg="White")
        self.label5.place(relx=0.5,rely=0.04,anchor=CENTER)
        self.BackButton=Button(root,image=backimage,command=self.Back,borderwidth=0,background="White")
        self.BackButton.place(relx=0.3,rely=0.04,anchor=CENTER)
        
        self.BillPane=Canvas(self.cnv,bg="Light gray",height=300,width=400)
        self.BillPane.place(relx=0.5,rely=0.55,anchor=CENTER)
        self.NameLabel=Label(self.BillPane,font=("Product Sans",12),bg="Light Gray",text="Name")
        self.CatLabel=Label(self.BillPane,font=("Product Sans",12),bg="Light Gray",text="Room")
        self.StayLabel=Label(self.BillPane,font=("Product Sans",12),bg="Light Gray",text="Duration of Stay")
        self.TotalLabel=Label(self.BillPane,font=("Product Sans",12),bg="Light Gray",text="Total Amount")

        self.NameLabel.place(relx=0.1,rely=0.1)
        self.CatLabel.place(relx=0.1,rely=0.25)
        self.StayLabel.place(relx=0.1,rely=0.4)
        self.TotalLabel.place(relx=0.1,rely=0.55)
        

        self.NameLabelI=Label(self.BillPane,font=("Product Sans",12),bg="Light Gray")
        self.CatLabelI=Label(self.BillPane,font=("Product Sans",12),bg="Light Gray")
        self.StayLabelI=Label(self.BillPane,font=("Product Sans",12),bg="Light Gray")
        self.TotalLabelI=Label(self.BillPane,font=("Product Sans",12),bg="Light Gray")

        self.NameLabelI.place(relx=0.6,rely=0.1)
        self.CatLabelI.place(relx=0.6,rely=0.25)
        self.StayLabelI.place(relx=0.6,rely=0.4)
        self.TotalLabelI.place(relx=0.6,rely=0.55)
        
        self.b=Button(root, text="Show Bill", foreground="blue", bg='pink', activebackground="red", width=10, height=2,command=self.ShowBill)
        self.b.place(relx=0.5,rely=0.25,anchor=CENTER)
        self.checkout=Button(root, text="Checkout", foreground="blue", bg='pink', activebackground="red", width=10, height=2,command=self.Checkout)
        self.checkout.place(relx=0.5,rely=0.9,anchor=CENTER)

    def ShowBill(self):
        try:
            c.execute("Select Name from Details where Rno=?",(self.RoomEntry.get()))
            conn.commit()
            self.name=c.fetchone()
            self.name=self.name[0]
            self.NameLabelI.config(text=self.name)
            c.execute("Select Category from Details where Rno=?",(self.RoomEntry.get()))
            conn.commit()
            self.cat=c.fetchone()
            self.cat=self.cat[0]
            self.CatLabelI.config(text=self.cat)
            c.execute("Select Days from Details where Rno=?",(self.RoomEntry.get()))
            conn.commit()
            self.stay=c.fetchone()
            self.stay=self.stay[0]
            self.StayLabelI.config(text=self.stay)
            c.execute("Select Subtotal from Details where Rno=?",(self.RoomEntry.get()))
            conn.commit()
            self.total=c.fetchone()
            self.total=self.total[0]
            self.TotalLabelI.config(text=self.total)
        except TypeError:
            messagebox.showerror("Error","Room is not booked")
        except ProgrammingError:
            messagebox.showerror("Error","Room Number must be a number in the range 1-9")
    
    def Checkout(self):
        try:
            c.execute("Select Avail from Available where Rno=?",(self.RoomEntry.get()))
            conn.commit()
            self.status=c.fetchone()
            self.status=self.status[0]
        except:
            messagebox.showerror("Error","Room Number must be a number in the range 1-9")
        if self.status=="N":
            c.execute("UPDATE Available SET Avail=? WHERE Rno=?",("A",self.RoomEntry.get()))
            conn.commit()
            c.execute("Delete from Details where Rno=?",(self.RoomEntry.get()))
            conn.commit()            
            messagebox.showinfo("Successful","Checked-Out Successfully")
        elif self.status=="A":
            messagebox.showwarning("Cant Check-Out","This room is not booked")
        


    
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
        root.place(relx=0.5,rely=0.5,height=400,width=500,anchor=CENTER)
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
        # forget_btn=Button(root,text="Forgot password?",bg="white",fg="gray",bd=0,font=("times new roman",12)).place(x=90,y=280)
        self.loginimage=PhotoImage(file="HotelManagement\Login.png")
        self.login_btn=Button(root,command=self.login_function,image=self.loginimage,bg="white",borderwidth=0)
        self.login_btn.place(relx=0.5,y=320,anchor=CENTER)
   

    
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
        self.root.title("Login Page")
        #self.bag=PhotoImage(file ="HotelManagement\Background.png")
        #self.bglabel=Label(root,image=self.bag)
        #self.bglabel.place(x=0,y=0)

        self.cnv=Canvas(root,bg="White",height=600,width=600,highlightthickness=0)
        self.cnv.place(relx=0.5,rely=0.5,anchor=CENTER)

        #button Image
        self.RoomButton=PhotoImage(file="HotelManagement\Checkin.png")
        self.OutButton=PhotoImage(file="HotelManagement\Checkout.png")
        self.CabButton=PhotoImage(file="HotelManagement\Cab.png")
        self.LogoutButton=PhotoImage(file="HotelManagement\Logout.png")


        #Labels
        self.title=Label(self.cnv,text="MAIN MENU",font=("Product Sans",45),fg="#95B8D1",bg="White").place(relx=0.5,rely=0.1,anchor=CENTER)
        #BUTTONS CODE
        self.roomAvail=Button(self.cnv,command=self.Booking,image=self.RoomButton,borderwidth=0,border=0,background="White").place(relx=0.3,rely=0.3,anchor=CENTER)
        self.checkOut = Button(self.cnv,command=self.Billing,image=self.OutButton,borderwidth=0,border=0,background="White").place(relx=0.7,rely=0.3,anchor=CENTER)
        self.cabBook = Button(self.cnv,command=self.Cab,image=self.CabButton,borderwidth=0,border=0,background="White").place(relx=0.5,rely=0.5,anchor=CENTER)
        self.billing = Button(self.cnv,command=self.LogOut,image=self.LogoutButton,borderwidth=0,border=0,background="White").place(relx=0.5,rely=0.9,anchor=CENTER)


Login(root)
root.mainloop()
