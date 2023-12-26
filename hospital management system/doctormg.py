import time
import random 
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

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
              
        
        ############## Title Lable ##############
        
        title = Label(self.root,text = "Doctor Mangement System",font = ("monotype corsiva",42,"bold"),bd =5,
        relief = GROOVE, bg = "#b7d8d6",fg = "black")
        title.pack(side = TOP , fill = X)
        
        ###Frame
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
  root = Tk()
  app = Doctor(root)
  root.mainloop()