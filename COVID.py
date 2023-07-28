import customtkinter as ctk
import tkinter
from tkinter import messagebox
from tkinter import END
import csv
import uuid

class COVID(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.frame=ctk.CTkFrame(parent, width=900, height=650)
        self.frame.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
        self.frame2=ctk.CTkFrame(parent, width=900, height=70)
        self.frame2.place(relx=0.5, rely=0.94, anchor=tkinter.CENTER)
        self.create_widgets()
        self.entries()

    def create_widgets(self):
        #respondent information labels
        self.title_label = ctk.CTkLabel(master=self.frame,bg_color="#367E18", width=900, height=40, text = "Respondent Information",text_color="#FCFFE7", font=("Century Gothic", 25, "bold"))
        self.title_label.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)
        
        #name label
        self.name_label = ctk.CTkLabel(master=self.frame, text = "Name:", font=("Century Gothic", 17, "bold"))
        self.name_label.place(x= 50, y=80)

        #gender label
        self.gender_label = ctk.CTkLabel(master=self.frame, text = "Gender:", font=("Century Gothic", 17, "bold")) 
        self.gender_label.place(x= 50, y=130)

        #number label
        self.number_label = ctk.CTkLabel(master= self.frame, text = "Phone Number:" , font=("Century Gothic", 17, "bold"))
        self.number_label.place(x= 50, y=180)

        #email label
        self.email_label = ctk.CTkLabel(master= self.frame, text = "Email Address:", font=("Century Gothic", 17, "bold"))
        self.email_label.place(x= 50, y=230)

        #health questions labels
        self.title2_label = ctk.CTkLabel(master=self.frame,bg_color="#367E18", width=900, height=40, text = "Health Questions",text_color="#FCFFE7", font=("Century Gothic", 25, "bold"))
        self.title2_label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        #vaccination_status label
        self.vaccination_status_label = ctk.CTkLabel(master=self.frame, text = "Have you received the COVID-19 vaccination?", font=("Century Gothic", 17, "bold"))
        self.vaccination_status_label.place(x= 50, y=370)

        #symptoms label
        self.symptoms_label = ctk.CTkLabel(master=self.frame, text = "Have you been exposed to COVID-19 in the last 14 days?",font=("Century Gothic", 17, "bold"))
        self.symptoms_label.place(x= 50, y=440)

        #exposure label
        self.exposure_label = ctk.CTkLabel(master=self.frame, text = "Have you been in contact with someone experiencing COVID-19 symptoms in the past week?",font=("Century Gothic", 17, "bold"))
        self.exposure_label.place(x= 50, y=510)

        #covid_test label
        self.covid_test_label = ctk.CTkLabel(master=self.frame, text = "Have you undergone a COVID-19 test within the past two weeks?",font=("Century Gothic", 17, "bold"))
        self.covid_test_label.place(x= 50, y=580)

    def entries(self):
        #name entry
        self.name_entry = ctk.CTkEntry(master=self.frame, width=200, height=25)
        self.name_entry.place(x=115, y=83)

        #gender radiobutton
        self.gender = tkinter.IntVar()
        
        self.male_radiobutton = ctk.CTkRadioButton(master= self.frame, variable= self.gender, value= 1, text="Male", font=("Century Gothic", 16), command=None )
        self.male_radiobutton.place(x=125, y=133)
        self.female_radiobutton = ctk.CTkRadioButton(master=self.frame, variable= self.gender,value= 2, text="Female", font=("Century Gothic", 16), command=None )
        self.female_radiobutton.place(x=215, y=133)

        #number entry
        self.number_entry = ctk.CTkEntry(master=self.frame, width=200, height=25)
        self.number_entry.place(x=190, y=183)

        #email entry
        self.email_entry = ctk.CTkEntry(master=self.frame, width=200, height=25)
        self.email_entry.place(x=180, y=233)

        #vaccionation status radiobutton
        self.vaccination_status = tkinter.IntVar()

        self.not_yet_radiobutton = ctk.CTkRadioButton(master= self.frame, variable= self.vaccination_status, text="Not Yet", font=("Century Gothic", 12), value= 1, command= self.status_vaccination)
        self.not_yet_radiobutton.place(x=50, y=410)

        self.onedose_radiobutton = ctk.CTkRadioButton(master=self.frame, variable= self.vaccination_status, text="1st Dose", font=("Century Gothic", 12), value= 2, command= self.status_vaccination)
        self.onedose_radiobutton.place(x=140, y=410)

        self.twodose_radiobutton = ctk.CTkRadioButton(master=self.frame, variable= self.vaccination_status, text="Fully Vaccine", font=("Century Gothic", 12), value= 3, command= self.status_vaccination)
        self.twodose_radiobutton.place(x=235, y=410)

        self.onebooster_radiobutton = ctk.CTkRadioButton(master=self.frame, variable= self.vaccination_status, text="1st Booster Shot", font=("Century Gothic", 12), value= 4, command= self.status_vaccination)
        self.onebooster_radiobutton.place(x=355, y=410)

        self.twobooster_radiobutton = ctk.CTkRadioButton(master=self.frame, variable= self.vaccination_status, text="Second Booster", font=("Century Gothic", 12), value= 5, command= self.status_vaccination)
        self.twobooster_radiobutton.place(x=485, y=410)

        #exposure radiobutton

        self.exposure = tkinter.IntVar()

        self.yes_radiobutton = ctk.CTkRadioButton(master= self.frame, variable= self.exposure, text="Yes", font=("Century Gothic", 12), value= 1, command= self.covid_exposure)
        self.yes_radiobutton.place(x=50, y=475)

        self.no_radiobutton = ctk.CTkRadioButton(master=self.frame, variable= self.exposure, text="No", font=("Century Gothic", 12), value= 2, command= self.covid_exposure)
        self.no_radiobutton.place(x=140, y=475)

        self.uncertain_radiobutton = ctk.CTkRadioButton(master=self.frame, variable= self.exposure, text="Uncertain", font=("Century Gothic", 12), value= 3, command= self.covid_exposure)
        self.uncertain_radiobutton.place(x=235, y=475)

        #contact exposure radiobutton

        self.contact = tkinter.IntVar()

        self.yes_contact_radiobutton = ctk.CTkRadioButton(master= self.frame, variable= self.contact, text="Yes", font=("Century Gothic", 12), value= 1,)
        self.yes_contact_radiobutton.place(x=50, y=545)

        self.no_contact_radiobutton = ctk.CTkRadioButton(master=self.frame, variable= self.contact, text="No", font=("Century Gothic", 12), value= 2,)
        self.no_contact_radiobutton.place(x=140, y=545)

        self.uncertain_contact_radiobutton = ctk.CTkRadioButton(master=self.frame, variable= self.contact, text="Uncertain", font=("Century Gothic", 12), value= 3,)
        self.uncertain_contact_radiobutton.place(x=235, y=545)

        #covid test radiobutton
        self.covid_test = tkinter.IntVar()

        self.no_test_radiobutton = ctk.CTkRadioButton(master= self.frame, variable= self.covid_test, text="No", font=("Century Gothic", 12), value= 1)
        self.no_test_radiobutton.place(x=50, y=610)

        self.yes_positive_contact_radiobutton = ctk.CTkRadioButton(master=self.frame, variable= self.covid_test, text="Yes-Positive", font=("Century Gothic", 12), value= 2)
        self.yes_positive_contact_radiobutton.place(x=120, y=610)
        
        self.yes_negative_contact_radiobutton = ctk.CTkRadioButton(master=self.frame, variable= self.covid_test, text="Yes-Negative", font=("Century Gothic", 12), value= 3)
        self.yes_negative_contact_radiobutton.place(x=230, y=610)
        
        self.yes_pending_contact_radiobutton = ctk.CTkRadioButton(master=self.frame, variable= self.covid_test, text="Yes-Pending", font=("Century Gothic", 12), value= 4)
        self.yes_pending_contact_radiobutton.place(x=350, y=610)
        

    def create_button(self):
        self.save_button=ctk.CTkButton(self.frame2,width=400, height=50, text="Save", font=('Century Gothic',19,"bold"), command= None)
        self.save_button.place(relx=0.25, rely=0.5, anchor=tkinter.CENTER)
        self.search_button=ctk.CTkButton(self.frame2,width=400, height=50, text="Search", font=('Century Gothic',19,"bold"),fg_color=("#CC3636"), command= None)
        self.search_button.place(relx=0.75, rely=0.5, anchor=tkinter.CENTER)

    def registration_number(self):
        short_uuid = str(uuid.uuid4().int)[:6]
        return short_uuid
    
    def on_save_button_click(self):
          # Get values from widgets
          name = self.name_entry.get()
          gender = self.gender.get()
          phone_number = self.number_entry.get()
          email = self.email_entry.get()
          vaccine = self.vaccination_status.get()
          exposure = self.exposure.get()
          contact= self.contact.get()
          covid_test = self.covid_test.get()
          short_uuid = self.registration_number()