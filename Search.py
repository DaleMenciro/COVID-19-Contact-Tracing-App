import customtkinter as ctk
import tkinter
from tkinter import messagebox
import csv

class Search(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.frame=ctk.CTkFrame(parent, width=900, height=650)
        self.frame.place(relx=0.5, rely=0.45, anchor=tkinter.CENTER)
        self.frame2=ctk.CTkFrame(parent, width=900, height=70)
        self.frame2.place(relx=0.5, rely=0.94, anchor=tkinter.CENTER)
        self.create_widgets()
        self.entries()
        self.search_button()
        self.back_exit_button() 

    def create_widgets(self):
         #respondent information labels
        self.title_label = ctk.CTkLabel(master=self.frame2, text = "Enter your Registration Number:", font=("Century Gothic", 18, "bold"))
        self.title_label.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)
        
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
        #search entry
        self.search_entry = ctk.CTkEntry(master=self.frame2, width=150, height=30, font=("Century Gothic", 17, "bold"))
        self.search_entry.place(relx=0.44, rely=0.5, anchor=tkinter.CENTER)

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

    def search_button(self):
        self.search_button=ctk.CTkButton(self.frame2,width=70, height=40, text="Search", font=('Century Gothic',19,"bold"), command= self.search_data)
        self.search_button.place(relx=0.58, rely=0.5, anchor=tkinter.CENTER)

    def back_exit_button (self):
        self.back_button=ctk.CTkButton(self.frame2,width=70, height=40, text="Back", font=('Century Gothic',19,"bold"), command= self.back)
        self.back_button.place(relx=0.8, rely=0.5, anchor=tkinter.CENTER)

        self.exit_button=ctk.CTkButton(self.frame2,width=70, height=40, text="Exit", font=('Century Gothic',19,"bold"), command= self.exit)
        self.exit_button.place(relx=0.9, rely=0.5, anchor=tkinter.CENTER)

    def exit(self):
        response = messagebox.askyesno("Message", "Are you sure you want to exit?")
        if response:
            messagebox.showinfo("Message", "Thank you for using the program!")
            from Start import Application
            Application.quit(self)

    def back(self):
        self.pack_forget()
        from COVID import COVID
        self.back_window = COVID(self.master)
    
    def search_data(self):
        # Get the registration number from the search_entry widget
        registration_number = self.search_entry.get()

        try:
            # Try to open the CSV file containing the contact tracing data
            with open("contact_tracing_data.csv", "r", newline='') as file:
                # Read the CSV data into a dictionary reader
                reader = csv.DictReader(file)
                # Convert the reader into a list of dictionaries
                user_data = list(reader)
        except FileNotFoundError:
            # If the file is not found, initialize an empty list for user_data
            user_data = []
        
        # Initialize a variable to store the found data (if any)
        data_found = None

        # Loop through the user_data to find the matching registration number
        for data in user_data:
            if "Registration Number" in data and data["Registration Number"] == registration_number:
                # If the registration number is found, store the data and break the loop
                data_found = data
                break

        # Check if data was found
        if data_found:
            # If data is found, display a message box with the information
            messagebox.showinfo("Hello!", "Registration Number found")
            # Populate the relevant entry widgets with the retrieved data
            self.name_entry.delete(0, tkinter.END)
            self.name_entry.insert(tkinter.END, data_found["Full_name"])
            self.gender.set(data_found["Gender"])
            self.number_entry.delete(0, tkinter.END)
            self.number_entry.insert(tkinter.END, data_found["Phone Number"])
            self.email_entry.delete(0, tkinter.END)
            self.email_entry.insert(tkinter.END, data_found["Email"])
            self.vaccination_status.set(data_found["Vaccination Status"])
            self.exposure.set(data_found["Exposure Status"])
            self.contact.set(data_found["Contact Exposure Status"])
            self.covid_test.set(data_found["COVID Test"])
        else:
            # If data is not found, display an error message box
            messagebox.showerror("Error!", "Registration Number not found, please try again.")
            # Clear the entry widgets and reset some variables to default values
            self.name_entry.delete(0, tkinter.END)
            self.number_entry.delete(0, tkinter.END)
            self.gender.set(value=0)
            self.email_entry.delete(0, tkinter.END)
            self.vaccination_status.set(value=0)
            self.exposure.set(value=0)
            self.contact.set(value=0)
            self.covid_test.set(value=0)
