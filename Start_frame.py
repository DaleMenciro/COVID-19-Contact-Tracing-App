import tkinter
import customtkinter as ctk
from tkinter import messagebox

class Frame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.frame=ctk.CTkFrame(parent, width=320, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def create_widget(self):
        #Labels
        self.label2=ctk.CTkLabel(master=self.frame, text="Welcome to",font=('Century Gothic',30, "bold"))
        self.label2.place(x=70, y=40)

        self.label3=ctk.CTkLabel(master=self.frame, text="COVID-19 Contact Tracing App",font=('Century Gothic',17))
        self.label3.place(x=35, y=80)

    def buttons(self):
    
    def go_start(self):
    
    def exit(self):


