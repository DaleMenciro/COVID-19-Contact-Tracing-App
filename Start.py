import customtkinter as ctk
from PIL import ImageTk,Image
from Start_frame import Frame

class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("dark-blue")
        self.geometry("1200x750+150+20")
        self.title("Welcome!")
        self.grid_columnconfigure((0, 1), weight=1)
        self.image1=ImageTk.PhotoImage(Image.open("C:\\Users\\user\\Desktop\\OOP (LAB EXERCISES)\\COVID CONTACT TRACING\\Pattern.png"))
        self.bg_1=ctk.CTkLabel(self,image=self.image1)
        self.bg_1.pack()
        self.start_frame = Frame(parent=self)
