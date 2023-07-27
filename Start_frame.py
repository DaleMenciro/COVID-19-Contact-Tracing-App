import tkinter
import customtkinter as ctk
from tkinter import messagebox

class Frame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.frame=ctk.CTkFrame(parent, width=320, height=350)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)