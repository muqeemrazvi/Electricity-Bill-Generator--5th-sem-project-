from tkinter import ttk,messagebox
from tkinter import*
import mysql.connector
from PIL import ImageTk, Image

_root=Tk()
_root.geometry("1900x10080")
_root.title("Electricity Bill")


fheading=Frame(_root,bg="gray",borderwidth=5)
fheading.pack(fill=BOTH)

lheading1=Label(fheading,text="ELECTRICITY  BILL",font="lucida 15 bold italic").pack()

image = Image.open("bg12.webp") 
# Resize the image using resize() method
resize_image = image.resize((1525, 990))
 
img2 = ImageTk.PhotoImage(resize_image)
# create label and add resize image
label1 = Label(_root,image=img2)
label1.image = img2
label1.place(x=0,y=45)




def showdata():    
    global listBox
    cloms=('Name','Meter_Number','Previous_Unit','Current_Unit','Bill_Amount')
    listBox=ttk.Treeview(_root,columns=cloms,show='headings')
    style=ttk.Style()

    style.configure('Treeview', rowheight=40,font=('arial', 12, 'bold'), fieldbackground='white', background='white',)
    style.configure('Treeview.Heading',font=('arial', 14, 'bold'),foreground='red')

    listBox.config(show='headings')
    listBox.column('Name',width=200,anchor=CENTER)
    listBox.column('Meter_Number',width=200,anchor=CENTER)
    listBox.column('Previous_Unit',width=300,anchor=CENTER)
    listBox.column('Current_Unit',width=200,anchor=CENTER) 
    listBox.column('Bill_Amount',width=200,anchor=CENTER) 

    for col in cloms:
        listBox.heading(col,text=col)
        listBox.place(x=350,y=120)
    show()


fsidebar=Frame(_root)
fsidebar.place(x=10,y=100)
fsidebar.configure(bg="#C1C1CD",width=250,height=500)
ShowDataBtn=Button(fsidebar,text="Show Data",command=showdata,bg="#A2A2CD",borderwidth=5,height=2,width=15,font="lucida 15 bold italic").place(x=10,y=50)


minamt=50
def genrate():
    global billamt,unit
    unit=currUnitValue.get()-preUnitValue.get()
    if(unit>=1 and unit<=100):
        billamt=minamt+(10*unit)
    elif(unit>100 and unit<=200):    
        billamt=minamt+1000+(15*(unit-100))
    elif(unit>200 and unit<=300):    
        billamt=minamt+2500+(20*(unit-200))

    elif(unit>300 and unit<=400):    
        billamt=minamt+4500+(25*(unit-300))   
     
    else:    
        billamt=minamt+7000+(35*(unit-400))

    fFram.destroy()
  
    bill()

def bill():
    global fBill
    l1=Label(fBill,text=f"Name               =  {nameValue.get()}",font="bold").place(x=30,y=40)
    l2=Label(fBill,text=f"Meter Number =  {miterNoValue.get()}",font="bold").place(x=30,y=70)     
    l3=Label(fBill,text=f"Unit Consumed                  =  {unit}kWh",font="bold",background="#C1C1CD").place(x=330,y=150)   
    
    if(unit>=1 and unit<=100):
        l4= Label(fBill,text=f"Minimum Charge                                                                        {minamt}/-",font="bold").place(x=30,y=200)
        l5=Label(fBill,text=f"Block Usage       Consumption (kWh)         Rates",font="bold").place(x=30,y=245)
        l6=Label(fBill,text=f"First                       1 - 100                              10                       {billamt-50}/-",font="bold").place(x=30,y=270)
     
      

    elif(unit>100 and unit<=200):
        l7=Label(fBill,text=f"Minimum Charge                                                                        {minamt}/-",font="bold").place(x=20,y=200)
        l8=Label(fBill,text=f"Block Usage       Consumption (kWh)         Rates",font="bold").place(x=20,y=240)
        l9=Label(fBill,text=f"First                       1  - 100                              10                       {10*100}/-",font="bold").place(x=20,y=270)
        l10=Label(fBill,text=f"Second              101 - 200                              15                           {billamt-1050}/-",font="bold").place(x=20,y=295)

    elif(unit>200 and unit<=300):
        l11=Label(fBill,text=f"Minimum Charge                                                                        {minamt}/-",font="bold").place(x=20,y=200)
        l12=Label(fBill,text=f"Block Usage       Consumption (kWh)         Rates",font="bold").place(x=20,y=240)
        l13=Label(fBill,text=f"First                       1  - 100                              10                       {10*100}/-",font="bold").place(x=20,y=270)
        l14=Label(fBill,text=f"Second              101 - 200                              15                        {15*100}/-",font="bold").place(x=20,y=295)
        l15=Label(fBill,text=f"Third                   201 - 300                              20                        {billamt-2550}/-",font="bold").place(x=20,y=320)   
    elif(unit>300 and unit<=400):
        l16=Label(fBill,text=f"Minimum Charge                                                                        {minamt}/-",font="bold").place(x=20,y=200)
        l17=Label(fBill,text=f"Block Usage       Consumption (kWh)         Rates",font="bold").place(x=20,y=240)
        l18=Label(fBill,text=f"First                       1  - 100                              10                       {10*100}/-",font="bold").place(x=20,y=270)
        l19=Label(fBill,text=f"Second              101 - 200                              15                        {15*100}/-",font="bold").place(x=20,y=295)
        l20=Label(fBill,text=f"Third                   201 - 300                              20                        {2000}/-",font="bold").place(x=20,y=320)   
        l21=Label(fBill,text=f"Forth                   301 - 400                              25                        {billamt-4550}/-",font="bold").place(x=20,y=345)   

    else:
        l22=Label(fBill,text=f"Minimum Charge                                                                        {minamt}/-",font="bold").place(x=20,y=200)
        l23=Label(fBill,text=f"Block Usage       Consumption (kWh)         Rates",font="bold").place(x=20,y=240)
        l24=Label(fBill,text=f"First                       1  - 100                         10                       {10*100}/-",font="bold").place(x=20,y=270)
        l25=Label(fBill,text=f"Second                101 - 200                        15                        {15*100}/-",font="bold").place(x=20,y=295)
        l26=Label(fBill,text=f"Third                   201 - 300                         20                        {2000}/-",font="bold").place(x=20,y=320)   
        l27=Label(fBill,text=f"Forth                   301 - 400                         25                        {2500}/-",font="bold").place(x=20,y=345)   
        l28=Label(fBill,text=f"Fifth                   400 onwards                      35                        {billamt-7050}/-",font="bold").place(x=20,y=370)   

    l29=Label(fBill,text=f"Total amount     =     {billamt}/-",font="bold").place(x=430,y=405)   
    l30=Button(fBill,text="Add to Data Base",command=add,bg="#A2A2CD",font="bold",borderwidth=5,height=1,width=16).place(x=300,y=450)
    l31=Button(fBill,text="X",command=BillDestroy,bg="red",font="bold").place(x=675,y=0)
  

def BillDestroy():
    fBill.destroy()



def add():
    global namedata,mitNodat,preNodata,currNodata
    namedata=nameValue.get()
    mitNodat=miterNoValue.get()
    preNodata=preUnitValue.get()
    currNodata=currUnitValue.get()

    conn=mysql.connector.connect(host='localhost',username='root',password='muqeem123',database='Electricity_Bill')
    my_cursor=conn.cursor()

    
    sql = "INSERT INTO customer_record (Name,Meter_No,Previous_Unit,Current_Unit,Bill_Amount) VALUES (%s, %s, %s, %s,%s)"
    val = (namedata,mitNodat,preNodata,currNodata,billamt)
    my_cursor.execute(sql,val)
    conn.commit()
    messagebox.showinfo("information","Record inserted successfully..")
    nameValue.delete(0,END)
    miterNoValue.delete(0,END)
    preUnitValue.delete(0,END)
    currUnitValue.delete(0,END)

    
    

def show():
    btn=Button(listBox,text="X",command=showDestroy,bg="red",font="bold").place(x=1075,y=0)
    conn=mysql.connector.connect(host='localhost',username='root',password='muqeem123',database='electricity_bill')
    my_cursor=conn.cursor()
    my_cursor.execute("select *from customer_record")
    rows=my_cursor.fetchall()
    
    for i, (Name,Meter_Number,Previous_Unit,Current_Unit,Bill_Amount) in enumerate(rows,start=1):
        listBox.insert("","end", values=(Name,Meter_Number,Previous_Unit,Current_Unit,Bill_Amount))
    conn.close()     
  
    



def showDestroy():
     listBox.destroy() 
     



nameValue=StringVar()
miterNoValue=StringVar()
preUnitValue=IntVar()
currUnitValue=IntVar()

def genrateBill():
    global fFram,fBill
    global name,mitNo,preNo,currNo,nameentry,mitNoentry,preNoentry,currNoentry,gentareFrmBtn
    fBill=Frame(_root)
    fFram=Frame(_root)
    fFram.pack(pady=70)
    # fFram.pack_propagate(False)
    fFram.configure(bg="#9898F5",width=800,height=500)
    name=Label(fFram,text="Name            :",font="bold").place(x=170,y=130)
    mitNo=Label(fFram,text="meter Number :",font="bold").place(x=170,y=170)
    preNo=Label(fFram,text="previous units :",font="bold").place(x=170,y=210)
    currNo=Label(fFram,text="current units   :",font="bold").place(x=170,y=250)


    nameentry=Entry(fFram,textvariable=nameValue,font="bold").place(x=330,y=130)
    mitNoentry=Entry(fFram,text="enter",textvariable=miterNoValue,font="bold").place(x=330,y=170)
    preNoentry=Entry(fFram,textvariable=preUnitValue,font="bold").place(x=330,y=210)
    currNoentry=Entry(fFram,textvariable=currUnitValue,font="bold").place(x=330,y=250)


    gentareFrmBtn=Button(fFram,text="Generate Bill",command=genrate,font="bold").place(x=300,y=340)

    fBill.pack(pady=70)
    fBill.configure(bg="#9898F5",width=700,height=500)

GenrateBillBtn=Button(fsidebar,text="Generate Bill",command=genrateBill,bg="#A2A2CD",borderwidth=5,height=2,width=15,font="lucida 15 bold italic").place(x=10,y=170)




nameCheckValue=StringVar()
miterNoCheckValue=StringVar()
def checkBill():
    global fcheckBill
    global nameCheck,mitNoCheck,preNo,currNo,nameCheckentry,mitNoCheckentry,preNoCheckentry,currNoentry,SearchBtn
    fcheckBill=Frame(_root)
    fcheckBill.pack(pady=70)
    fcheckBill.configure(bg="#9898F5",width=800,height=500)
    Label(fcheckBill,text="OR",font="bold 20",bg="#9898F5").place(x=300,y=180)
    nameCheck=Label(fcheckBill,text="Name            :",font="bold").place(x=170,y=130)
    mitNoCheck=Label(fcheckBill,text="Meter Number :",font="bold").place(x=170,y=230)
    

    nameCheckentry=Entry(fcheckBill,textvariable=nameCheckValue,font="bold").place(x=330,y=130)
    mitNoCheckentry=Entry(fcheckBill,text="enter",textvariable=miterNoCheckValue,font="bold").place(x=330,y=230)


    SearchBtn=Button(fcheckBill,text="Search Bill",command=searchBill,font="bold").place(x=300,y=340)

checkBillBtn=Button(fsidebar,text="Check Bill",command=checkBill,bg="#A2A2CD",borderwidth=5,height=2,width=15,font="lucida 15 bold italic").place(x=10,y=290)


def searchBill():
    fcheckBill.destroy()
    global listBox1
    cloms=('Name','Meter_Number','Previous_Unit','Current_Unit','Bill_Amount')
    listBox1=ttk.Treeview(_root,columns=cloms,show='headings',height=2)
    style=ttk.Style()

    style.configure('Treeview', rowheight=40,font=('arial', 12, 'bold'), fieldbackground='white', background='white')
    style.configure('Treeview.Heading',font=('arial', 14, 'bold'),foreground='red')

    listBox1.config(show='headings')
    listBox1.column('Name',width=200,anchor=CENTER)
    listBox1.column('Meter_Number',width=200,anchor=CENTER)
    listBox1.column('Previous_Unit',width=300,anchor=CENTER)
    listBox1.column('Current_Unit',width=200,anchor=CENTER) 
    listBox1.column('Bill_Amount',width=200,anchor=CENTER) 

    for col in cloms:
        listBox1.heading(col,text=col)
        listBox1.place(x=350,y=200)
    searchInDb()    

def searchBilldestroy():
      listBox1.destroy()

def searchInDb():
    btn=Button(listBox1,text="X",command=searchBilldestroy,bg="red",font="bold").place(x=1075,y=0)   

    conn=mysql.connector.connect(host='localhost',username='root',password='muqeem123',database='electricity_bill')
    my_cursor=conn.cursor()
    namev=nameCheckValue.get()
    metrv=miterNoCheckValue.get()
    my_cursor.execute(f"SELECT * FROM electricity_bill.customer_record where Name='{namev}' or Meter_No='{metrv}';")
    rows=my_cursor.fetchall()
    namev=nameCheckValue.get()
    for i, (Name,Meter_Number,Previous_Unit,Current_Unit,Bill_Amount) in enumerate(rows,start=1):
        listBox1.insert("","end", values=(Name,Meter_Number,Previous_Unit,Current_Unit,Bill_Amount))
    conn.close() 


def creatore():
   global fcreatore ,cnLabel
   fcreatore=Frame(_root,width=800,height=500,bg="#E0E0EE")
   fcreatore.pack(pady=70)

   image = Image.open("admin.jpg") 
   # Resize the image using resize() method
   resize_image = image.resize((200, 250))
 
   img1 = ImageTk.PhotoImage(resize_image)
   # create label and add resize image
   label1 = Label(fcreatore,image=img1)
   label1.image = img1
   label1.place(x=10,y=70)


   
   
   cclassLabel=Label(fcreatore,text=" Devoloped By",font="lucida 22 bold italic",bg="#C1C1FF").place(x=250)
   cnLabel=Label(fcreatore,text="Name : MOHD ABDUL MUQEEM",font="lucida 20 bold italic").place(x=250,y=80)
   cVtuLabel=Label(fcreatore,text="VTU : 3PD20CS046",font="lucida 20 bold italic").place(x=250,y=130)
   cageLabel=Label(fcreatore,text="Age : 20",font="lucida 20 bold italic").place(x=250,y=180)
   cPhnoLabel=Label(fcreatore,text="Phone No : 7204728158",font="lucida 20 bold italic").place(x=250,y=230)
   cPhnoLabel=Label(fcreatore,text="Email Id : abdulmuqeem298@gmail.com",font="lucida 20 bold italic").place(x=250,y=280)
   cgitLabel=Label(fcreatore,text=" User Name : muqeemrazvi \n \n Link : https://github.com/muqeemrazvi ",font="lucida 20 bold italic").place(x=160,y=340)
   creatoreBtnclose=Button(fcreatore,text="X",command=creatoreDestroy,bg="red",font="bold").place(x=775,y=0)
   image = Image.open("gitlogo.png") 
   # Resize the image using resize() method
   resize_image = image.resize((70, 55))
 
   img = ImageTk.PhotoImage(resize_image)
   # create label and add resize image
   label2 = Label(fcreatore,image=img)
   label2.image = img
   label2.place(x=160,y=340)
   cPhnoLabel=Label(fcreatore,text="GitHub",font="bold 8").place(x=180,y=395)

def creatoreDestroy():
    fcreatore.destroy()
checkBillBtn=Button(fsidebar,text="Devoloped By",command=creatore,bg="#A2A2CD",borderwidth=5,height=2,width=15,font="lucida 15 bold italic").place(x=10,y=410)

_root.mainloop()