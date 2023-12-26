############################ PROJECT BY PY-REBEL ########################################### 

import random
import time
import datetime
from tkinter import*
from tkinter import ttk
import tkinter.messagebox


def main ():
    root = Tk()
    app =window1(root)
    root.mainloop()
    
class window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Hospital Mangement System")
        self.master.geometry('1350x750+0+0') # x-axis , y-axis,0,0 are location from top leftmost
        self.frame = Frame(self.master)
        self.frame.pack()
        
        self.Username = StringVar()
        self.Password = StringVar()
        
        self.LabelTitle =Label(self.frame,text= "Hospital Mangement System",font = ("arial",40,"bold"),bd = 10,relief = "sunken")
        self.LabelTitle.grid(row = 0, column= 0 , columnspan = 2 , pady = 20)
        
        self.Loginframe1 = Frame(self.frame,width = 1000,height  = 300 ,bd = 10 ,relief = "groove")
        self.Loginframe1.grid(row = 1 , column = 0)
     
        self.Loginframe2 = Frame(self.frame,width = 1000,height  = 100 ,bd = 10 , relief = "groove")
        self.Loginframe2.grid(row = 2 , column = 0 , pady = 15)
        
        self.Loginframe3 = Frame(self.frame,width = 1000,height  = 200 ,bd = 10, relief = "groove")
        self.Loginframe3.grid(row = 6 , column = 0, pady = 5)
        
        self.button_reg = Button(self.Loginframe3 , text = "Patient Regristration Window",state = DISABLED, font = ("arial",15,"bold"),command = self.Registration_Window)
        self.button_reg.grid (row = 0 , column = 1 , padx = 10 , pady = 10)
       
        self.button_Hosp = Button(self.Loginframe3 , text = "Hospital Management Window",state = DISABLED, font = ("arial",15,"bold"),command = self.Hospital_Window)
        self.button_Hosp.grid (row = 1 , column = 1 , padx = 10 , pady = 10)
        
        self.button_Dr_appt = Button(self.Loginframe3 , text = "Doctor Management Window",state = DISABLED, font = ("arial",15,"bold"),command = self.Dr_Apoint_Window)
        self.button_Dr_appt.grid (row = 2 , column = 1 , padx = 50 , pady = 10)
        
        
        # now we will make user name and password frame
        
        self.LableUsername = Label(self.Loginframe1,text="User Name ", font = ("arial", 20,"bold"),bd = 3)
        self.LableUsername.grid(row = 0 , column= 0)
        
        self.textUsername = Entry(self.Loginframe1,font=("arial",10,"bold"),bd = 3, textvariable = self.Username)
        self.textUsername.grid(row = 0, column = 1 , padx = 40,pady = 15)
        
        
        self.LableUsername = Label(self.Loginframe1,text="Password  ", font = ("arial", 20,"bold"),bd = 3)
        self.LableUsername.grid(row = 1 , column= 0)
        
        self.textPassword = Entry(self.Loginframe1,font=("arial",10,"bold"),show = "*",bd = 3, textvariable = self.Password)
        self.textPassword.grid(row = 1, column = 1 , padx = 40,pady = 15)
        
        
        self.button_login = Button (self.Loginframe2, text = "Login", width = 20 , font = ("arial",18,"bold"),command = self.login_system)
        self.button_login.grid(row = 0, column = 0, padx=10 , pady = 10) 
        
        self.button_Reset = Button (self.Loginframe2, text = "Reset", width = 20 , font = ("arial",18,"bold"),command = self.reset_btn )
        self.button_Reset.grid(row = 0, column = 3, padx=10 , pady = 10) 
        
        self.button_Exit = Button (self.Loginframe2, text = "Exit", width = 20 , font = ("arial",18,"bold"),command = self.Exit_btn)
        self.button_Exit.grid(row = 0, column = 6, padx=10 , pady = 10) 
        
        
    def login_system(self):
        user = self.Username.get()
        pswd = self.Password.get()
        
        if (user == str("admin")and (pswd == str("admin"))):
            self.button_reg.config(state = NORMAL)
            self.button_Hosp.config(state = NORMAL)
            self.button_Dr_appt.config(state = NORMAL)
            self.button_med_stock.config(state = NORMAL)
        else:
            tkinter.messagebox.askyesno("Pharmacy Mangement System","You Have entered an invalid user name or password")
            self.button_reg.config(state = DISABLED)
            self.button_Hosp.config(state = DISABLED)
            self.button_Dr_appt.config(state = DISABLED)
            self.button_med_stock.config(state = DISABLED)
            # if user name or password is incorrect it will be in its disable state
            
            
            self.Username .set("")
            self.Password .set("")
            self.textUsername .focus("")
            
    def reset_btn(self):
            self.button_reg.config(state = DISABLED)
            self.button_Hosp.config(state = DISABLED)
            self.button_Dr_appt.config(state = DISABLED)
            self.button_med_stock.config(state = DISABLED)
            #because when we will reset still we haven't given correct user id and password
            self.Username .set("")
            self.Password .set("")
            self.textUsername .focus("")
            
    def Exit_btn(self):
        self.Exit_btn = tkinter.messagebox.askyesno("Pharmacy Mangement System","Are you sure you want to exit")
        if self.Exit_btn > 0 :
            #we will close that master screen
            self.master.destroy()
            return
            
            
        # first we will define all our widow
    def Registration_Window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Registration(self.newWindow)
        
    def Hospital_Window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Hospital(self.newWindow)
    
    def Dr_Apoint_Window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Doctor(self.newWindow)
        
        
class Registration:
    def __init__(self,root):
        self.root = root
        self.root.title("Patient Registration System ")
        self.root.geometry("1350x750+0+0")
        self.root.configure(background = "black")
        
###################################### we will take live time data by using time module ##################

        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))
        
        Ref = StringVar()
        Mobile_no  = StringVar()
        Pincode  = StringVar()
        Address = StringVar()
        Firstname  = StringVar()
        Lastname  = StringVar()
        
##################################### this var 1,2,3,4,5 for combobox ###############################

        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = StringVar()
        var5 = IntVar() ###numercial value ##########
        
        Membership = StringVar()
        Membership.set("0")
        
#################################### #functions ###################################################

        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Member Registration Form", "Are you sure you want to Exit ?")
            if exitbtn > 0:
                root.destroy()
            else:
                self.newWindow = Toplevel(self.master)
                self.app = Registration(self.newWindow)   
                return


        def resetbtn():
            Ref.set("")
            Mobile_no.set("")
            Pincode.set("")
            Address.set("")
            Firstname.set("")
            Lastname.set("")
            var1.set("")
            var2.set("")
            var3.set("")
            var4.set("")
            var5.set("")
            Membership.set("0")
            member_gendercmb.current(0)
            member_idpcmb.current(0)
            member_memtypecmb.current(0)
            member_paymentwithcmb.current(0)
            member_membershiptxt(state = DISABLED)
            
        def reeesetbtn():
            reeesetbtn = tkinter.messagebox.askokcancel("Member Registration Form","You want to add as new Record")
            if reeesetbtn > 0:
                resetbtn()
            elif reeesetbtn<=0:
                resetbtn()
                detail_labeltxt.delete("1.0",END)
                return
                        
        def Reference_num():
            ranumber = random.randint(1,99999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber) 
            
        def membership_fees():
            
            if(var5.get() ==1):
                member_membershiptxt.configure(state=NORMAL)
                item = float(15000)
                Membership.set(str(item)+"RS")
            elif(var5.get()==0):
                member_membershiptxt.configure(state=DISABLED)
                Membership.set("0")
                
        def Receiptbtn():
            Reference_num()
            detail_labeltxt.insert(END,"\t"+ Date_of_Registration.get()+"     \t" + Ref.get() + "       \t" + Firstname.get() + '    \t\t'+
            Lastname.get()+ "  \t" + Mobile_no.get() + "\t"+ "\t" + Address.get() + "    \t" + Pincode.get() + "   \t\t" + member_gendercmb.get() +
            "\t" + Membership.get() + "\n" )
            
            

############################## title ##########################################################

        title = Label(self.root, text = "Member Registration Form" , font = ("monotype corsiva",30,"bold"),bd = 5,
                relief = GROOVE,bg = "#E6005C", fg = "#000000")
        title.pack(side=TOP, fill = X)

########################### member frame #####################################################

        Manage_Frame = Frame(self.root , bd = 4, relief = RIDGE , bg = "#001a66")
        Manage_Frame.place(x=20,y=100,width=450,height = 630)
        
############################# text,label,comboboxes in manage frames ########################

        Cus_title = Label(Manage_Frame,text="Customer Details",font=("arial",20,"bold"),bg="#001a66",fg="white")
        Cus_title.grid(row=0,columnspan=2,pady=5)    
    
        member_datalbl = Label(Manage_Frame,text="Date",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_datalbl.grid(row=1,column=0,pady=5,padx=10,sticky="w")
        member_datetxt = Entry(Manage_Frame,font=("arial",15,"bold"),textvariable=Date_of_Registration)
        member_datetxt.grid(row=1,column=1,pady=5,padx=10,sticky="w")
        
        member_reflbl = Label(Manage_Frame,text="Reference ID",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_reflbl.grid(row=2,column=0,pady=5,padx=10,sticky="w")
        member_reftxt = Entry(Manage_Frame,font=("arial",15,"bold"),state=DISABLED,textvariable=Ref)
        member_reftxt.grid(row=2,column=1,pady=5,padx=10,sticky="w")
        
        member_fnamelbl = Label(Manage_Frame,text="First Name",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_fnamelbl.grid(row=3,column=0,pady=5,padx=10,sticky="w")
        member_fnametxt = Entry(Manage_Frame,font=("arial",15,"bold"),textvariable=Firstname)
        member_fnametxt.grid(row=3,column=1,pady=5,padx=10,sticky="w")  
        
        member_lnamelbl = Label(Manage_Frame,text="Last Name",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_lnamelbl.grid(row=4,column=0,pady=5,padx=10,sticky="w")
        member_lnametxt = Entry(Manage_Frame,font=("arial",15,"bold"),textvariable=Lastname)
        member_lnametxt.grid(row=4,column=1,pady=5,padx=10,sticky="w")      
        
        member_mobilelbl = Label(Manage_Frame,text="Mobile No.",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_mobilelbl.grid(row=5,column=0,pady=5,padx=10,sticky="w")
        member_mobiletxt = Entry(Manage_Frame,font=("arial",15,"bold"),textvariable=Mobile_no)
        member_mobiletxt.grid(row=5,column=1,pady=5,padx=10,sticky="w") 
        
        member_addresslbl = Label(Manage_Frame,text="Address",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_addresslbl.grid(row=6,column=0,pady=5,padx=10,sticky="w")
        member_addresstxt = Entry(Manage_Frame,font=("arial",15,"bold"),textvariable=Address)
        member_addresstxt.grid(row=6,column=1,pady=5,padx=10,sticky="w")  
        
        member_pincodelbl = Label(Manage_Frame,text="Pincode",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_pincodelbl.grid(row=7,column=0,pady=5,padx=10,sticky="w")
        member_pincodetxt = Entry(Manage_Frame,font=("arial",15,"bold"),textvariable= Pincode)
        member_pincodetxt.grid(row=7,column=1,pady=5,padx=10,sticky="w") 
        
        member_genderlbl = Label(Manage_Frame,text="Gender",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_genderlbl.grid(row=8,column=0,pady=5,padx=10,sticky="w")
        member_gendercmb = ttk.Combobox(Manage_Frame, text = "var4" ,state="readonly",font=("arial",15,"bold"),width=19)
        member_gendercmb['values'] = ("","Male","Female","Trans","Other")
        member_gendercmb.current(0)
        member_gendercmb.grid(row=8,column=1,pady=5,padx=10,sticky="w")
        
        member_idplbl = Label(Manage_Frame,text="ID Proof",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_idplbl.grid(row=9,column=0,pady=5,padx=10,sticky="w")
        member_idpcmb = ttk.Combobox(Manage_Frame, text = "var3" ,state="readonly",font=("arial",15,"bold"),width=19)
        member_idpcmb['values'] = ("","Adhaar Card","Passport","Pan-Card","Voter ID","Student ID")
        member_idpcmb.current(0)
        member_idpcmb.grid(row=9,column=1,pady=5,padx=10,sticky="w")
        
        member_memtypelbl = Label(Manage_Frame,text="Member Type",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_memtypelbl.grid(row=10,column=0,pady=5,padx=10,sticky="w")
        member_memtypecmb = ttk.Combobox(Manage_Frame, text = "var2" ,state="readonly",font=("arial",15,"bold"),width=19)
        member_memtypecmb['values'] = ("","Ayushman Card","Health Insurance","PAY Immediately","PAY After Leaving")
        member_memtypecmb.current(0)
        member_memtypecmb.grid(row=10,column=1,pady=5,padx=10,sticky="w")
        
        member_paymentwithlbl = Label(Manage_Frame,text="Payment",font=("arial",15,"bold"),bg="#001a66",fg="white")
        member_paymentwithlbl.grid(row=11,column=0,pady=5,padx=10,sticky="w")
        member_paymentwithcmb = ttk.Combobox(Manage_Frame, text = "var1" ,state="readonly",font=("arial",15,"bold"),width=19)
        member_paymentwithcmb['values'] = ("","Cash","Debit Card - RuPay","Debit Card - Visa","Debit Card - MasterCard","Credit Card","Phonepay","Google Pay","Paytm")
        member_paymentwithcmb.current(0)
        member_paymentwithcmb.grid(row=11,column=1,pady=5,padx=10,sticky="w")
        
        member_membership = Checkbutton(Manage_Frame,text="Membership Fees",variable= var5,onvalue=1, offvalue=0,font=("arial",15,"bold"),bg="#001a66",fg="white",command=membership_fees)
        member_membership.grid(row=12,column=0,sticky="w")
        member_membershiptxt= Entry(Manage_Frame,font =("arial",15,"bold"),state = DISABLED, justify=RIGHT,textvariable=Membership)
        member_membershiptxt.grid(row=12,column=1,pady=5,padx=10,sticky="w")     
        
######################## deails frame ############################################################

        detail_frame = Frame(self.root, relief=RIDGE,bg = "#001a66")
        detail_frame.place(x=500,y=100,width=820,height=630) 
        
        detail_label = Label(detail_frame,font=("arial",11,"bold"),pady=10,padx=2,width=95,
            text="Date\t  Ref Id\t  Firstname      Lastname      Mobile No      Address      Pincode      Gender      Membership")
        detail_label.grid(row= 0,column= 0,columnspan= 4, sticky="W")
        detail_labeltxt = Text(detail_frame,width=123,height=34,font=("arial",10,))
        detail_labeltxt.grid(row=1,column=0,columnspan=4)
        
################################# we will add button in detail frame ##############################

        recieptbtn = Button(detail_frame, padx = 15,bd= 5 , font=("arial",12,"bold"),bg="#ff9966",width=20, text="Receipt",command=Receiptbtn)
        recieptbtn.grid (row = 2 , column = 0)
        
        resetbtn = Button(detail_frame, padx = 15,bd= 5 , font=("arial",12,"bold"),bg="#ff9966",width=20, text="Reset",command=reeesetbtn)
        resetbtn.grid (row = 2 , column = 1)
        
        exitbtn = Button(detail_frame, padx = 15,bd= 5 , font=("arial",12,"bold"),bg="#ff9966",width=20, text="Exit",command = exitbtn)
        exitbtn.grid (row = 2 , column = 2)
        
class Hospital():
    def __init__(self,root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1700x900+0+0")  # we will take full windows (screen)
        self.root.configure(background = "black")
        
######################################## VARIABLE DECLARATION #############################

        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))
        
        Ref =                StringVar()
        cmbTabletNames =     StringVar()
        HospitalCode =       StringVar()
        Number_of_Tablets =  StringVar()
        Lot =                StringVar()
        IssuedDate =         StringVar()
        ExpiryDate =         StringVar()
        DailyDose =          StringVar()
        SideEffects =        StringVar()
        MoreInformation =    StringVar()
        StorageAdvice =      StringVar()
        Medication =         StringVar()
        PatientId =          StringVar()
        PatientNHnumver =    StringVar()
        PatientName =        StringVar()
        Dateofbirth =        StringVar()
        PatientAddress =     StringVar()
        Prescription =       StringVar()
        NHSnumber =          StringVar()
        
        def Reference_numfunc():
            ranumber = random.randint(1,9999)
            randomnumber = str(ranumber)
            Ref.set(randomnumber) 
            
        def prescriptionfunc():
            Reference_numfunc()
            TextPresciption.insert(END,"Patient Id: \t\t"+PatientId.get()+"\n")
            TextPresciption.insert(END,"Patient Name: \t\t"+PatientName.get()+"\n")
            TextPresciption.insert(END,"Tablet: \t\t"+cmbTabletNames.get()+"\n")
            TextPresciption.insert(END,"Number of tablet: \t\t"+Number_of_Tablets.get()+"\n")
            TextPresciption.insert(END,"Daily Dose: \t\t"+DailyDose.get()+"\n")
            TextPresciption.insert(END,"Issued Date: \t\t"+IssuedDate.get()+"\n")
            TextPresciption.insert(END,"Expiry Date: \t\t"+ExpiryDate.get()+"\n")
            TextPresciption.insert(END,"Storage: \t\t"+StorageAdvice.get()+"\n")
            TextPresciption.insert(END,"More Information: \t\t"+MoreInformation.get()+"\n")
            return
        
        def prescriptiondatafunc():
            Reference_numfunc()
            TextPresciptionData.insert(END,Date_of_Registration.get()+"\t"+Ref.get()+"\t\t"+PatientName.get()+"\t\t"+Dateofbirth.get()+"\t\t"+
            NHSnumber.get()+"\t\t"+cmbTabletNames.get()+"\t"+Number_of_Tablets.get()+"\t\t"+IssuedDate.get()+"\t\t"+ExpiryDate.get()+"\t\t"+DailyDose.get()+"\t\t"+
            StorageAdvice.get()+"\t\t"+PatientId.get()+"\n")
            return
                
        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Hospital Management System", "Are you sure you want to Exit ?")
            if exitbtn > 0:
                root.destroy()    
                return
            
        def deletefunc():
            Ref.set("")                
            cmbTabletNames.set("")
            HospitalCode.set("") 
            Number_of_Tablets.set("")   
            Lot.set("")                 
            IssuedDate.set("")          
            ExpiryDate.set("")          
            DailyDose.set("")           
            SideEffects.set("")         
            MoreInformation.set("")     
            StorageAdvice.set("")       
            Medication.set("")          
            PatientId.set("")           
            PatientNHnumver.set("")     
            PatientName.set("")         
            Dateofbirth.set("")         
            PatientAddress.set("")      
            Prescription.set("")        
            NHSnumber.set("")
            TextPresciption.delete("1.0",END)
            TextPresciptionData.delete("1.0",END)
            return 
        
        def resetfunc():
            Ref.set("")                
            cmbTabletNames.set("")
            HospitalCode.set("") 
            Number_of_Tablets.set("")   
            Lot.set("")                 
            IssuedDate.set("")          
            ExpiryDate.set("")          
            DailyDose.set("")           
            SideEffects.set("")         
            MoreInformation.set("")     
            StorageAdvice.set("")       
            Medication.set("")          
            PatientId.set("")           
            PatientNHnumver.set("")     
            PatientName.set("")         
            Dateofbirth.set("")         
            PatientAddress.set("")      
            Prescription.set("")        
            NHSnumber.set("")
            TextPresciption.delete("1.0",END)
            return           
            
        

##########################################TITLE###############################################

        title = Label(self.root,text = "Hospital Management System" , font =("monotype corsiva",42,"bold"),bd = 5,
            relief = GROOVE,bg = "#2eb8b8",fg = "black")
        title.pack(side= TOP , fill = X)
        
##########################################FRAMES###############################################

        Manage_Frame = Frame(self.root,width = 1510 , height = 400 , bd = 5 , relief = RIDGE , bg = "#0099cc")
        Manage_Frame.place(x=10,y=80)
        
        Button_Frame =  Frame(self.root,width = 1510 , height = 55 , bd = 4 , relief = RIDGE , bg = "#328695")
        Button_Frame.place(x=10,y=460)
        
        Data_Frame =  LabelFrame(self.root,width = 1510 , height = 270 , bd = 4 , relief = RIDGE , bg = "#266e73")
        Data_Frame.place(x=10,y=510)
        
###########################################INNER FRAME#############################################


        Data_FrameLeft =  LabelFrame(Manage_Frame,width = 1050, text = "General Information",
        font = ("arial",20,"italic bold"), height = 390 , bd = 7 , relief = RIDGE , bg = "#0099cc")
        Data_FrameLeft.pack(side = LEFT)

    
        Data_FrameRight =  LabelFrame(Manage_Frame,width = 1050, text = "Prescription",
        font = ("arial",15,"italic bold"), height = 390 , bd = 7 , relief = RIDGE , bg = "#0099cc")
        Data_FrameRight.pack(side = RIGHT)

        
        Data_FrameData =  LabelFrame(Data_Frame,width = 1050, text = "Prescription Data", font = ("arial",12,"italic bold"),
        height = 390 , bd = 4 , relief = RIDGE , bg = "#3eb7bb")
        Data_FrameData.pack(side = LEFT)
        
#####################################################   LABELS     ##################################################################

        Datelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Date" , padx = 2 , bg = "#0099cc")
        Datelbl.grid(row = 0 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Datetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = Date_of_Registration)
        Datetxt.grid(row = 0 , column = 1 , padx = 10 , pady = 4 , sticky= E)  
        
#########################################################   REF   ###################################################################

        Reflbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Reference Number" , padx = 2 , bg = "#0099cc")
        Reflbl.grid(row = 1 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Reftxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , state=DISABLED , textvariable = Ref)
        Reftxt.grid(row = 1 , column = 1 , padx = 10 , pady = 4 , sticky= E)  
        
##################################### PATIENT ID #############################

        PatientIdlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Patient Id" , padx = 2 , bg = "#0099cc")
        PatientIdlbl.grid(row = 2 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        PatientIdtxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = PatientId )
        PatientIdtxt.grid(row = 2 , column = 1 , padx = 10 , pady = 4 , sticky= E)
        
####################### PatientName  ######################################### 

        PatientNamelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Patient Name" , padx = 2 , bg = "#0099cc")
        PatientNamelbl.grid(row = 3 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        PatientNametxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = PatientName)
        PatientNametxt.grid(row = 3 , column = 1 , padx = 10 , pady = 4 , sticky= E)

############################ Date of Birth ###################################

        Dateofbirthlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Date of birth" , padx = 2 , bg = "#0099cc")
        Dateofbirthlbl.grid(row = 4 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Dateofbirthtxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = Dateofbirth)
        Dateofbirthtxt.grid(row = 4 , column = 1 , padx = 10 , pady = 4 , sticky= E)      
        
########################################## Address ############################

        Addresslbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Address" , padx = 2 , bg = "#0099cc")
        Addresslbl.grid(row = 5 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Addresstxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = PatientAddress)
        Addresstxt.grid(row = 5 , column = 1 , padx = 10 , pady = 4 , sticky= E)
        
######################################### NHS number ############################

        NHSnumberlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "NHS Unique Number" , padx = 2 , bg = "#0099cc")
        NHSnumberlbl.grid(row = 6 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        NHSnumbertxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = NHSnumber)
        NHSnumbertxt.grid(row = 6 , column = 1 , padx = 10 , pady = 4 , sticky= E)     
        
####################################### Tablet name #############################

        Tabletlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "Tablet" , padx = 2 , bg = "#0099cc")
        Tabletlbl.grid(row = 7 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        
        Tabletcmb = ttk.Combobox(Data_FrameLeft , textvariable = cmbTabletNames , width=25 , state="readonly",
            font=("arial",12,"bold"))
        Tabletcmb['values'] = ("", "Dolo 650mg", "Dan-p", "Dio-l One", "Calpol","Phenotine", "Nexium",
                                    "Singulair","Plavix","Amoxicillian","Azithromycin","Limcin-900")
        Tabletcmb.current(0)
        Tabletcmb.grid(row = 7, column = 1 , padx = 10 , pady = 5 )
        
########################################## NO of tablet to take ##########################

        No_of_Tabletslbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = " Number of Tablets  " , padx = 2 , bg = "#0099cc")
        No_of_Tabletslbl.grid(row = 8 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        No_of_Tabletstxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 27 , textvariable = Number_of_Tablets)
        No_of_Tabletstxt.grid(row = 8 , column = 1 , padx = 10 , pady = 4 , sticky= E) 
        
           
        ########### WILL MAKE 2ND COPY COLOUMN DETAILS IN SAME FRAME . ################

        
########################################### Hospital Code #####################################


        HospitalCodelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = " Hospital Code " , padx = 2 , bg = "#0099cc")
        HospitalCodelbl.grid(row = 0 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        HospitalCodetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 25 , textvariable = HospitalCode)
        HospitalCodetxt.grid(row = 0 , column = 3 , padx = 10 , pady = 5 , sticky= E) 

   
########################################### storage advice to keep medicine #####################


        StorageAdvicelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = " Storage Advice " , padx = 2 , bg = "#0099cc")
        StorageAdvicelbl.grid(row = 1 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        
        StorageAdvicecmb = ttk.Combobox(Data_FrameLeft , textvariable = StorageAdvice , width=23 , state="readonly",
            font=("arial",12,"bold"))       
        StorageAdvicecmb['values'] = ("", "Room temp.","Below 5*C","Below 0*C","Refrigration")
        StorageAdvicecmb.current(0)
        StorageAdvicecmb.grid(row = 1 , column = 3 , padx = 10 , pady = 5 , sticky= E)

        
########################################### Lot no. of medicine #############################################

        
        Lot_nolbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = " Lot Number " , padx = 2 , bg = "#0099cc")
        Lot_nolbl.grid(row = 2 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        Lot_notxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 25 , textvariable = Lot)
        Lot_notxt.grid(row = 2 , column = 3 , padx = 10 , pady = 5 , sticky= E) 

        
########################################## Isuues date ######################################################


        IssuedDatelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = " Issued Date " , padx = 2 , bg = "#0099cc")
        IssuedDatelbl.grid(row = 3 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        IssuedDatetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 25 , textvariable = IssuedDate)
        IssuedDatetxt.grid(row = 3 , column = 3 , padx = 10 , pady = 5 , sticky= E) 

        
############################################### expiry date #################################################


        ExpiryDatelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = " Expiry Date " , padx = 2 , bg = "#0099cc")
        ExpiryDatelbl.grid(row = 4 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        ExpiryDatetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 25 , textvariable = ExpiryDate)
        ExpiryDatetxt.grid(row = 4 , column = 3 , padx = 10 , pady = 5 , sticky= E) 


#############################################  daily dose ###################################################        


        DailyDoselbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = " Daily Dose " , padx = 2 , bg = "#0099cc")
        DailyDoselbl.grid(row = 5 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        DailyDosetxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 25 , textvariable = DailyDose)
        DailyDosetxt.grid(row = 5 , column = 3 , padx = 10 , pady = 5 , sticky= E) 

        
###################################### Side Effects  #########################################################


        SideEffectslbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = " Side Effects " , padx = 2 , bg = "#0099cc")
        SideEffectslbl.grid(row = 6 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        SideEffectstxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 25 , textvariable = SideEffects)
        SideEffectstxt.grid(row = 6 , column = 3 , padx = 10 , pady = 5 , sticky= E) 

        
######### more information like to meet dr. or something like that #####################################

        MoreInformationlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = " More Information " , padx = 2 , bg = "#0099cc")
        MoreInformationlbl.grid(row = 7 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        MoreInformationtxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 25 , textvariable = MoreInformation)
        MoreInformationtxt.grid(row = 7 , column = 3 , padx = 10 , pady = 5 , sticky= E)   
      
        
################################## medication (yes/no)###################################################


        Medicationlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"), width = 20 , text = "  Medication " , padx = 2 , bg = "#0099cc")
        Medicationlbl.grid(row = 8 , column = 2 , padx = 10 , pady = 5 , sticky = W)
        Medicationtxt = Entry(Data_FrameLeft , font = ("arial",12,"bold"),width = 25 , textvariable =  Medication)
        Medicationtxt.grid(row = 8 , column = 3 , padx = 10 , pady = 5 , sticky= E)   
        
        
####################################### text field for prescription ####################################

        TextPresciption = Text(Data_FrameRight , font = ("arail",12,"bold"), width= 55 , height = 17 , padx = 3 ,
            pady = 5)
        TextPresciption.grid(row = 0 , column = 0)
        
##################################### text for prescription data ################################################
        
        TextPresciptionData = Text(Data_FrameData , font = ("arial",12,"bold"), width= 203 , height = 17 )
        TextPresciptionData.grid(row = 1 , column = 0)
        
######################################### now will add button for middle for prescription data #################################

        Prescriptionbtn = Button(Button_Frame , text="Prescription",bg = "#ffaab0" , activebackground="#fcceb2",
        font=("arial",15,"bold") , width = 22 , command=prescriptionfunc)
        Prescriptionbtn.grid (row = 0 , column = 0 , padx = 15)
      
      
        
        Recieptbtn = Button(Button_Frame , text="Presciption Data",bg = "#ffaab0" , activebackground="#fcceb2",
        font=("arial",15,"bold") , width = 22 , command=prescriptiondatafunc)
        Recieptbtn.grid (row = 0 , column = 1 , padx = 15)
      
      
        
        Resetbtn = Button(Button_Frame , text="Reset",bg = "#ffaab0" , activebackground="#fcceb2",
        font=("arial",15,"bold") , width = 22, command = resetfunc )
        Resetbtn.grid (row = 0 , column = 2 , padx = 15)
      
      
        
        Deletebtn = Button(Button_Frame , text="Delete",bg = "#ffaab0" , activebackground="#fcceb2",
        font=("arial",15,"bold") , width = 22 , command= deletefunc )
        Deletebtn.grid (row = 0 , column = 3 , padx = 15)
      
      
        
        exitbtn = Button(Button_Frame , text="Exit",bg = "#ffaab0" , activebackground="#fcceb2",
        font=("arial",15,"bold") , width = 22 , command = exitbtn )
        exitbtn.grid (row = 0 , column = 4 , padx = 15)
      
        
        
        prescriptiondatarow = Label(Data_FrameData , bg="white", font=("arial",12,"bold"),
        text = "Date\tReference Id\tPatient Name\tDate of Birth\tNHS number\tTablet\tNo of Tablet\tIssued Date\tExpired Date\tDaily Dose\tStorage Device\tPatient ID")
        prescriptiondatarow.grid(row = 0 , column = 0 , sticky = W)




class Doctor():
    def __init__ (self,root):
        self.root = root
        self.root.title("Doctor Mangement System")
        self.root.geometry("1700x900+0+0")
        self.root.configure(background = "black")
      ########## We will  Delcare all function together ########  
        Date_of_Registration = StringVar()
        Date_of_Registration.set(time.strftime("%d/%m/%y"))
        Drid = StringVar()
        Drname = StringVar()
        DateofBirth = StringVar()
        spes = StringVar()
        GovtPri = StringVar()
        Surgeries = StringVar()
        Experiences = StringVar()
        Nurses = StringVar()
        DrMobile = StringVar()
        PtName = StringVar()
        AppTime = StringVar()
        PtAge = StringVar()
        PatientAddress = StringVar()
        PtMobile = StringVar()
        Disease = StringVar()
        Case = StringVar()
        BenefitCard = StringVar()
      
        
        def exitbtn():
            exitbtn = tkinter.messagebox.askyesno("Hospital Management System", "Are you sure you want to Exit ?")
            if exitbtn > 0:
                root.destroy()    
                return
      
        
        def resetfunc():
          Drid.set("")
          Drname.set("")
          DateofBirth.set("")
          spes.set("")
          GovtPri.set("")
          Surgeries.set("")
          Experiences.set("")
          Nurses.set("")
          DrMobile.set("")
          PtName.set("")
          AppTime.set("")
          PtAge.set("")
          PatientAddress.set("")
          PtMobile.set("")
          Disease.set("")
          Case.set("")
          BenefitCard.set("")
          TextPresciption.delete("1.0", END)
          return
        
              
        def deletefunc():
            Drid.set("")
            Drname.set("")
            DateofBirth.set("")
            spes.set("")
            GovtPri.set("")
            Surgeries.set("")
            Experiences.set("")
            Nurses.set("")
            DrMobile.set("")
            PtName.set("")
            AppTime.set("")
            PtAge.set("")
            PatientAddress.set("")
            PtMobile.set("")
            Disease.set("")
            Case.set("")
            BenefitCard.set("")
            TextPresciption.delete("1.0", END)
            TextPresciptionData.delete("1.0", END)
            return
        
          
        def Patient_idfunc():
            ranumber = random.randint(1,9999)
            randomnumber = str(ranumber)
            Drid.set(randomnumber)
        
        
        def prescriptiondatafunc():
            Patient_idfunc()
            TextPresciptionData.insert(END,Date_of_Registration.get()+"\t"+Drid.get()+"\t"+Drname.get()+"\t\t"+DateofBirth.get()+"\t\t"+
            spes.get()+"\t\t"+GovtPri.get()+"\t\t"+Surgeries.get()+"\t\t"+Experiences.get()+"\t\t"+Nurses.get()+"\t"+DrMobile.get()+"\t\t"+PtName.get()+"\t\t"+
            Case.get()+"\t"+PtAge.get()+"\n")
            return
        
              
        def prescriptionfunc():
            Patient_idfunc()
            TextPresciption.insert(END,"Date : \t\t"+Date_of_Registration.get()+"\n")
            TextPresciption.insert(END,"Patient Name: \t\t"+PtName.get()+"\n")
            TextPresciption.insert(END,"Appt. Time: \t\t"+AppTime.get()+"\n")
            TextPresciption.insert(END,"Age: \t\t"+PtAge.get()+"\n")
            TextPresciption.insert(END,"Address: \t\t"+PatientAddress.get()+"\n")
            TextPresciption.insert(END,"Disease: \t\t"+Disease.get()+"\n")
            TextPresciption.insert(END,"Case: \t\t"+Case.get()+"\n")
            TextPresciption.insert(END,"Benefit Card: \t\t"+BenefitCard.get()+"\n")
            TextPresciption.insert(END,"To Meet Dr.: \t\t"+Drname.get()+"\n")
            TextPresciption.insert(END,"Dr. Mobile No. : \t\t"+DrMobile.get()+"\n")
            return
              
        
############################################################### Title Lable ##############
       
        
        title = Label(self.root,text = "Doctor Mangement System",font = ("monotype corsiva",42,"bold"),bd =5,
        relief = GROOVE, bg = "#b7d8d6",fg = "black")
        title.pack(side = TOP , fill = X)
        
############################################# Frame ############################################
        
        
        Manage_Frame = Frame(self.root , width = 1510 , height = 400 , bd = 5 , relief = RIDGE , bg = "#eef3db")
        Manage_Frame.place(x=10 , y = 80)
        
        Button_Frame = Frame(self.root , width = 1510, height = 55 , bd = 4, relief = RIDGE , bg = "#eef3db")
        Button_Frame.place(x=10 , y = 460)
        
        Data_Frame = Frame(self.root , width = 1510 ,height= 270 , bd = 4 , relief = RIDGE , bg = "#eef3db")
        Data_Frame.place(x=10 , y = 510)
        
###########################################################
        
        Data_FrameLeft =  LabelFrame(Manage_Frame,width = 1050, text = "General Information",
        font = ("arial",20,"italic bold"), height = 390 , bd = 7 , relief = RIDGE , bg = "#789e9e")
        Data_FrameLeft.pack(side = LEFT)
    
    
        Data_FrameRight =  LabelFrame(Manage_Frame,width = 1050, text = "Patient Details",
        font = ("arial",15,"italic bold"), height = 390 , bd = 7 , relief = RIDGE , bg = "#789e9e")
        Data_FrameRight.pack(side = RIGHT)
    
        
        Data_FrameData =  LabelFrame(Data_Frame,width = 1050, text = "Doctor's Details", font = ("arial",12,"italic bold"),
        height = 390 , bd = 4 , relief = RIDGE , bg = "#b7d8d6")
        Data_FrameData.pack(side = LEFT)
    
        
        ##################doctor's ID#####################################

        DrIdlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20 , text = "Doctor ID", bg = "#789e9e")        
        DrIdlbl.grid(row = 0 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        DrIdtxt = Entry(Data_FrameLeft, font =("arial",12,"bold"),width = 27 , state = DISABLED, textvariable=Drid)
        DrIdtxt.grid(row= 0 , column = 1,padx = 10, pady = 5 , sticky = E)
    
        
        DrNamelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20 , text = "Doctor Name", bg = "#789e9e")        
        DrNamelbl.grid(row = 1 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        DrNametxt = Entry(Data_FrameLeft, font =("arial",12,"bold"),width = 27, textvariable=Drname)
        DrNametxt.grid(row= 1 , column = 1,padx = 10, pady = 5 , sticky = E)
    
        
        DateofBirthlbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20 , text = "Date of Birth", bg = "#789e9e")        
        DateofBirthlbl.grid(row = 2 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        DateofBirthtxt = Entry(Data_FrameLeft, font =("arial",12,"bold"),width = 27 ,  textvariable= DateofBirth)
        DateofBirthtxt.grid(row= 2 , column = 1,padx = 10, pady = 5 , sticky = E)
    
        
        Speslbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20 , text = "Specialisation", bg = "#789e9e")        
        Speslbl.grid(row = 3 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Spestxt = Entry(Data_FrameLeft, font =("arial",12,"bold"),width = 27 ,  textvariable=spes)
        Spestxt.grid(row= 3 , column = 1,padx = 10, pady = 5 , sticky = E)
    
    
        
        GovtPrilbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20 , text = "Govt/Private", bg = "#789e9e")        
        GovtPrilbl.grid(row = 4 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        GovtPricmb = ttk.Combobox(Data_FrameLeft,textvariable=GovtPri, width = 25 , state = "readonly",font=("arial",12,"bold"))
        GovtPricmb["values"] = ("","Goverment","Private")
        GovtPricmb.current(0)
        GovtPricmb.grid(row= 4 , column = 1,padx = 10, pady = 5 , sticky = E) 
    
    
        
        Surgerieslbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20 , text = "Surgeries", bg = "#789e9e")        
        Surgerieslbl.grid(row = 5 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Surgeriestxt = Entry(Data_FrameLeft, font =("arial",12,"bold"),width = 27 ,  textvariable=Surgeries)
        Surgeriestxt.grid(row= 5 , column = 1,padx = 10, pady = 5 , sticky = E)
    
    
        
        Experiencelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20 , text = "Experience", bg = "#789e9e")        
        Experiencelbl.grid(row = 6 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Experiencetxt = Entry(Data_FrameLeft, font =("arial",12,"bold"),width = 27 ,  textvariable=Experiences)
        Experiencetxt.grid(row= 6 , column = 1,padx = 10, pady = 5 , sticky = E)
    
    
        
        Nurseslbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20 , text = "Nurse's Under DR.", bg = "#789e9e")        
        Nurseslbl.grid(row = 7 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        Nursestxt = Entry(Data_FrameLeft, font =("arial",12,"bold"),width = 27 ,  textvariable=Nurses)
        Nursestxt.grid(row= 7 , column = 1,padx = 10, pady = 5 , sticky = E)
   
   
        
        DrMobilelbl = Label(Data_FrameLeft , font = ("arial",12,"bold"),width = 20 , text = "Doctor Mobile No.", bg = "#789e9e")        
        DrMobilelbl.grid(row = 8 , column = 0 , padx = 10 , pady = 5 , sticky = W)
        DrMobiletxt = Entry(Data_FrameLeft, font =("arial",12,"bold"),width = 27 ,  textvariable=DrMobile)
        DrMobiletxt.grid(row= 8, column = 1,padx = 10, pady = 5 , sticky = E)
   
   
        
        Datelbl = Label(Data_FrameLeft, font = ("arial",12,"bold"),width=20,text = "Date",padx=2,bg="#789e9e")
        Datelbl.grid(row = 0,column=2 , padx=10,pady = 5 , sticky= W)
        Datetext = Entry(Data_FrameLeft, font = ("arial",12,"bold"),width=27,textvariable= Date_of_Registration)
        Datetext.grid(row = 0,column=3 , padx=10,pady = 5 , sticky= E)
   
   
        
        PtNamelbl = Label(Data_FrameLeft, font = ("arial",12,"bold"),width=20,text = "Patient Name",padx=2,bg="#789e9e")
        PtNamelbl.grid(row = 1,column=2 , padx=10,pady = 5 , sticky= W)
        PtNametext = Entry(Data_FrameLeft, font = ("arial",12,"bold"),width=27,textvariable= PtName)
        PtNametext.grid(row = 1,column=3 , padx=10,pady = 5 , sticky= E)
    
    
        
        Apptimelbl = Label(Data_FrameLeft, font = ("arial",12,"bold"),width=20,text = "Appointment Time",padx=2,bg="#789e9e")
        Apptimelbl.grid(row = 2,column=2, padx=10,pady = 5 , sticky= W)
        Apptimetext = Entry(Data_FrameLeft, font = ("arial",12,"bold"),width=27,textvariable= AppTime)
        Apptimetext.grid(row = 2,column=3 , padx=10,pady = 5 , sticky= E)
    
    
         
        
        PtAgelbl = Label(Data_FrameLeft, font = ("arial",12,"bold"),width=20,text = "Patient Age",padx=2,bg="#789e9e")
        PtAgelbl.grid(row = 3,column=2, padx=10,pady = 5 , sticky= W)
        PtAgetext = Entry(Data_FrameLeft, font = ("arial",12,"bold"),width=27,textvariable= PtAge)
        PtAgetext.grid(row = 3,column=3 , padx=10,pady = 5 , sticky= E) 
    
    
        
        PtAddresslbl = Label(Data_FrameLeft, font = ("arial",12,"bold"),width=20,text = "Patient Address",padx=2,bg="#789e9e")
        PtAddresslbl.grid(row = 4,column=2, padx=10,pady = 5 , sticky= W)
        PtAddresstext = Entry(Data_FrameLeft, font = ("arial",12,"bold"),width=27,textvariable= PatientAddress)
        PtAddresstext.grid(row = 4,column=3 , padx=10,pady = 5 , sticky= E)
    
    
        
        PtMobilelbl = Label(Data_FrameLeft, font = ("arial",12,"bold"),width=20,text = "Patient Mobile No",padx=2,bg="#789e9e")
        PtMobilelbl.grid(row = 5,column=2, padx=10,pady = 5 , sticky= W)
        PtMobiletext = Entry(Data_FrameLeft, font = ("arial",12,"bold"),width=27,textvariable= PtMobile )
        PtMobiletext.grid(row = 5,column=3 , padx=10,pady = 5 , sticky= E)
    
    
        
        Diseaselbl = Label(Data_FrameLeft, font = ("arial",12,"bold"),width=20,text = "Patient Disease",padx=2,bg="#789e9e")
        Diseaselbl.grid(row = 6,column=2, padx=10,pady = 5 , sticky= W)
        Diseasetext = Entry(Data_FrameLeft, font = ("arial",12,"bold"),width=27,textvariable= Disease )
        Diseasetext.grid(row = 6,column=3 , padx=10,pady = 5 , sticky= E)
    
    
        
        Caselbl = Label(Data_FrameLeft, font = ("arial",12,"bold"),width=20,text = "Case",padx=2,bg="#789e9e")
        Caselbl.grid(row = 7,column=2, padx=10,pady = 5 , sticky= W)
        Casecmb = ttk.Combobox(Data_FrameLeft, textvariable= Case, width = 25, state="readonly", font=("arial", 12,"bold"))
        Casecmb["values"] = ("","New Case","Old case")
        Casecmb.current(0)
        Casecmb.grid(row = 7,column=3 , padx = 10 , pady= 5 , sticky = E)
    
    
        
        BenefitCardlbl = Label(Data_FrameLeft, font = ("arial",12,"bold"), width=20 ,text = "Benefit Card", padx=10 ,bg="#789e9e")
        BenefitCardlbl.grid(row = 8,column=2,sticky= W)
        BenefitCardcmb = ttk.Combobox(Data_FrameLeft, textvariable= BenefitCard , width = 25, state="readonly", font=("arial", 12,"bold"))
        BenefitCardcmb["values"] = ("","Ayushman Card ","Health Insurance","Senior Citizen","Army Card","NONE")
        BenefitCardcmb.current(0)
        BenefitCardcmb.grid(row = 8,column=3 , padx = 10 , sticky = E)
        
        
############################## Text Prescription ######################################

        TextPresciption = Text(Data_FrameRight , font = ("arail",12,"bold"), width= 55 , height = 17 , padx = 3 , pady = 5)
        TextPresciption.grid(row = 0 , column = 0)
        
        
############################ TEXT prescription for doctor details #########################

        TextPresciptionData = Text(Data_FrameData , font = ("arial",12,"bold"), width= 203 , height = 17 )
        TextPresciptionData.grid(row = 1 , column = 0)
        
################### BUTTON #############################################################

        Prescriptionbtn = Button(Button_Frame , text="Patient Information",bg = "#fe615a" , activebackground="#cc6686",
        font=("arial",15,"bold") , width = 22 , command=prescriptionfunc)
        Prescriptionbtn.grid (row = 0 , column = 0 , padx = 15)

        
        DoctorDetailbtn = Button(Button_Frame , text="Doctor's Details",bg = "#fe615a" , activebackground="#cc6686",
        font=("arial",15,"bold") , width = 22 , command=prescriptiondatafunc)
        DoctorDetailbtn.grid (row = 0 , column = 1 , padx = 15)

        
        Resetbtn = Button(Button_Frame , text="Reset",bg = "#fe615a" , activebackground="#cc6686",
        font=("arial",15,"bold") , width = 22 , command= resetfunc)
        Resetbtn.grid (row = 0 , column = 2 , padx = 15)

        
        Deletebtn = Button(Button_Frame , text="Delete",bg = "#fe615a" , activebackground="#cc6686",
        font=("arial",15,"bold") , width = 22 , command= deletefunc)
        Deletebtn.grid (row = 0 , column = 3 , padx = 15)

        
        Exitbtn = Button(Button_Frame , text="Exit",bg = "#fe615a" , activebackground="#cc6686",
        font=("arial",15,"bold") , width = 22 , command = exitbtn)
        Exitbtn.grid (row = 0 , column = 4 , padx = 15)

        
        Prescriptiondatarow = Label(Data_FrameData , bg="white", font=("arial",12,"bold"),
        text = "Date\tDoctor ID   Doctor Name\tDate of Birth\tSpecialisation\tGovt/Private\tSurgeries\tExperience\tNurses\tDR Mobile No\tPatient Name\tCase\tPt. Age")
        Prescriptiondatarow.grid(row = 0 , column = 0 , sticky = W)


if __name__ == "__main__":
    main()