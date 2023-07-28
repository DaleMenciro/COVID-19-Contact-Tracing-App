import customtkinter as ctk
import tkinter
from tkinter import messagebox

class COVID(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.frame=ctk.CTkFrame(parent, width=900, height=650)
        self.frame.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
        self.frame2=ctk.CTkFrame(parent, width=900, height=70)
        self.frame2.place(relx=0.5, rely=0.94, anchor=tkinter.CENTER)
        self.create_widgets()

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
        
        self.male_radiobutton = ctk.CTkRadioButton(master= self.frame, variable= self.gender, value= 1, text="Male", font=("Century Gothic", 16), command= )
        self.male_radiobutton.place(x=125, y=133)
        self.female_radiobutton = ctk.CTkRadioButton(master=self.frame, variable= self.gender,value= 2, text="Female", font=("Century Gothic", 16), command= )
        self.female_radiobutton.place(x=215, y=133)


