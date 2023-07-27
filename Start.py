import customtkinter as ctk
from PIL import ImageTk,Image

class Application(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
        ctk.set_default_color_theme("dark-blue")
        self.geometry("1200x750+150+20")
        self.title("Welcome!")
        self.grid_columnconfigure((0, 1), weight=1)
  