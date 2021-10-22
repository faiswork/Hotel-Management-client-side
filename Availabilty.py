# availability

#imports
from tkinter import*

#use this function to indicate room availablity
    
 
def ShowInfo():                                     
    if Occupants.get()=="1":
        BookButton=Button(window,text="Book now")
        BookButton.place(relx=0.5,rely=0.6,anchor=CENTER)
    else:
        pass
    InfoLabel.config(text="Availability Information will be shown here")



# setting up the window
window=Tk()
bag=PhotoImage(file ="D:\Python\HotelManagement\Background.png")
window.geometry("1169x600")
bglabel=Label(window,image=bag)
bglabel.place(x=0,y=0)
pane=Canvas(window,bg="White",height=1000,width=800)
pane.place(relx=0.5,y=500,anchor=CENTER)
label=Label(window,text="Availability",bg="White",font=("Product Sans",20)).place(relx=0.5,rely=0.05,anchor=CENTER)

# Getting the number of occupants
Occupants=StringVar()

OccupantLabel=Label(window,text="Select Number of Occupants",bg="White",font=("Product Sans",15)).place(relx=0.35,rely=0.2,anchor=CENTER)
OccupantSelect=OptionMenu(window,Occupants,*["1","2","3"])
OccupantSelect.config(indicatoron=0)
OccupantSelect.configure(bg="White",highlightthickness=0,highlightbackground="White",borderwidth=0)
OccupantSelect.place(relx=0.7,rely=0.2,anchor=CENTER)
Occupants.set("1")


# choosing the category of the room
Category=StringVar()
CategoryLabel=Label(window,text="Select Category",bg="White",font=("Product Sans",15)).place(relx=0.35,rely=0.3,anchor=CENTER)
CategorySelect=OptionMenu(window,Category,*[" A/C ","  Non A/C  ","  Presential Suite  "],)
CategorySelect.config(indicatoron=0)
CategorySelect.configure(bg="White",highlightthickness=0,highlightbackground="Grey",borderwidth=0)
CategorySelect.place(relx=0.7,rely=0.3,anchor=CENTER)
Category.set("  None Selected  ")


# label to display informataion

InfoLabel=Label(window,bg="White",font=("Product Sans",12))
InfoLabel.place(relx=0.5,rely=0.5,anchor=CENTER)



# Button

Clickme=Button(window,command=ShowInfo,text="Search")
Clickme.place(relx=0.5,rely=0.4,anchor=CENTER)

#variables to use while connecting to databse
def NumOfOcc():
    NumberOfOccupants=Occupants.get()
    return NumberOfOccupants
def RoomCategory():
    RoomCategory=Category.get()
    return RoomCategory
# mainloop
window.mainloop()
