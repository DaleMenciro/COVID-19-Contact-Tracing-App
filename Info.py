import tkinter
import customtkinter as ctk
from tkinter import messagebox
from COVID import COVID

class Info(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.frame=ctk.CTkFrame(parent, width=700, height=550)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def display_text(self):
        #About text
        self.about_label=ctk.CTkLabel(master=self.frame, text="ABOUT",font=('Century Gothic',50, "bold"),text_color="#91C8E4")
        self.about_label.place(relx=0.5, rely=0.12, anchor=tkinter.CENTER)

        self.about_text=ctk.CTkLabel(master=self.frame, 
                                 text="This app is specifically developed to assist individuals in monitoring their potential exposure to COVID-19 and tracking any related symptoms they may experience. By enabling users to input their personal details, the application allows them to create and maintain records within the secured database. With each new entry, users can easily track their interactions and health status, facilitating better COVID-19 contact tracing and symptom monitoring." , 
                                 font=('Century Gothic',15),wraplength=650)
        self.about_text.place(relx=0.5, rely=0.28, anchor=tkinter.CENTER)

        #Disclaimer text
        self.disclaimer_label=ctk.CTkLabel(master=self.frame, text="DISCLAIMER",font=('Century Gothic',50, "bold"),text_color="#EB455F")
        self.disclaimer_label.place(relx=0.5, rely=0.47, anchor=tkinter.CENTER)

        self.disclaimer_text=ctk.CTkLabel(master=self.frame, 
                                 text="By accessing and using this application, you agree to the following terms and conditions. This app is developed solely for academic purposes as part of a final project and should not be used for real-world COVID-19 contact tracing, symptom monitoring, or any health-related purposes. The application's contents and features are provided 'as-is,' and the creators bear no liability for inaccuracies, errors, or omissions. While personal data will be handled following data protection laws, users are strongly advised not to input any sensitive or personally identifiable information. All intellectual property rights related to the application, including design, code, and content, remain the property of the academic project creators, and unauthorized reproduction or exploitation is strictly prohibited. Users assume sole responsibility for their data input and usage of the application, and the academic project creators disclaim any liability for consequences resulting from its use. By continuing to use this application, users confirm their understanding and agreement to abide by these terms and conditions. ",
                                 font=('Century Gothic',11),wraplength=650
                                    )
        self.disclaimer_text.place(relx=0.5, rely=0.68, anchor=tkinter.CENTER)
    
    
    def create_button(self):
        self.button=ctk.CTkButton(master=self.frame,width=500, height=50, text="Get Started", font=('Century Gothic',19,"bold"),fg_color=("#367E18"), command=self.button_command)
        self.button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

    
    def button_command(self):
        response= messagebox.askyesno("Hello!", "Are you sure you want to get started?")
        if response:
            self.pack()
            self.frame.destroy()
            self.new_frame = COVID(self.master)

