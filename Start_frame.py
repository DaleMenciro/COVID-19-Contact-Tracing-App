import tkinter
import customtkinter as ctk
from tkinter import messagebox

class Frame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.frame=ctk.CTkFrame(parent, width=320, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.create_widget()
        self.buttons()

    def create_widget(self):
        #Labels
        self.label2=ctk.CTkLabel(master=self.frame, text="Welcome to",font=('Century Gothic',30, "bold"))
        self.label2.place(x=70, y=40)

        self.label3=ctk.CTkLabel(master=self.frame, text="COVID-19 Contact Tracing App",font=('Century Gothic',17))
        self.label3.place(x=35, y=80)

    def buttons(self):
         #Create custom button
        self.button1 = ctk.CTkButton(master=self.frame,
                                        width=220, height=50 , text="Start",
                                        font=('Century Gothic',20 , "bold") 
                                        , fg_color=("#367E18"),
                                        command=self.go_start, corner_radius=6)
        self.button1.place(x=50, y=140)

        self.button2 = ctk.CTkButton(master=self.frame,
                                        width=220, height=50 , text="Exit",
                                        font=('Century Gothic',20 , "bold") 
                                        , fg_color=("#CC3636"),
                                        command=self.exit, corner_radius=6)
        self.button2.place(x=50, y=220)
    
    def go_start(self):
        self.pack()
        self.pack_forget()
    
    def exit(self):
            response= messagebox.askyesno("Warning!", "Are you sure you want to exit?")
            if response:
                from Start import Application
                Application.quit(self)


