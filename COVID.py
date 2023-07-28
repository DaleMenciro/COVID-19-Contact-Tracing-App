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

    def create_widgets(self):
        #respondent information labels
        self.title_label = ctk.CTkLabel(master=self.frame,bg_color="#367E18", width=900, height=40, text = "Respondent Information",text_color="#FCFFE7", font=("Century Gothic", 25, "bold"))
        self.title_label.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)
        
        #name label
        self.name_label = ctk.CTkLabel(master=self.frame, text = "Name:", font=("Century Gothic", 17, "bold"))
        self.name_label.place(x= 50, y=80)

    def entries(self):

