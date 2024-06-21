import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image

FUTURA_FONT = ("Futura", 18, 'normal')

TITLE_NAME = "LockBox"
P_TEXT = "Stay safe, stay locked"

WINDOW_DIM = "1100x700"

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700

OPTIONSIDEBAR_WIDTH = 237

LOGO_PATH = "./assets/lockboxlogo.png"
PAGELOGO_PATH = "./assets/lockboxpagelogo.png"

rowCounter = 2

mainApp = tk.Tk()

# app init settings

mainApp.title("LockBox")
mainApp.iconbitmap("./assets/lockboxlogo.ico")
mainApp.geometry(WINDOW_DIM)
mainApp.resizable(False, False)

# frames setup

optionsSideBarFrame = tk.Frame(
    mainApp,
    bg="#F5F5F5"
)
optionsSideBarFrame.pack(
    side=tk.LEFT,
    fill=tk.Y
)
contextMainFrame = tk.Frame(
    mainApp,
    bg="#FFFFFF"
)
contextMainFrame.pack(
    side=tk.LEFT,
    fill=tk.Y
)

optionsSideBarFrame.pack_propagate(False)
contextMainFrame.pack_propagate(False)

optionsSideBarFrame.configure(
    width=OPTIONSIDEBAR_WIDTH,
)
contextMainFrame.configure(
    width=WINDOW_WIDTH - OPTIONSIDEBAR_WIDTH,
    height=WINDOW_HEIGHT
)

options = [
    tk.Canvas(optionsSideBarFrame, width=OPTIONSIDEBAR_WIDTH - 35, height=1, bg="grey", highlightthickness=0),
    ctk.CTkButton(optionsSideBarFrame, text="🔑Le mie password", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=82, height=32, hover_color="#BEBEBE"),
    ctk.CTkButton(optionsSideBarFrame, text="⌨️LockGen", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=82, height=32, hover_color="#BEBEBE"),
    ctk.CTkButton(optionsSideBarFrame, text="🧪Test di resistenza", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=82, height=32, hover_color="#BEBEBE"),
    tk.Canvas(optionsSideBarFrame, width=OPTIONSIDEBAR_WIDTH - 35, height=1, bg="grey", highlightthickness=0),
    ctk.CTkButton(optionsSideBarFrame, text="📁Criptazione dei file", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=82, height=32, hover_color="#BEBEBE"),
    ctk.CTkButton(optionsSideBarFrame, text="🚦Permessi di accesso", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=82, height=32, hover_color="#BEBEBE"),
    ctk.CTkButton(optionsSideBarFrame, text="✍️Firma digitale", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=82, height=32, hover_color="#BEBEBE"),
    ctk.CTkButton(optionsSideBarFrame, text="📫Steganografia", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=82, height=32, hover_color="#BEBEBE"),
    tk.Canvas(optionsSideBarFrame, width=OPTIONSIDEBAR_WIDTH - 35, height=1, bg="grey", highlightthickness=0),
    ctk.CTkButton(optionsSideBarFrame, text="🪪La mia identita’", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=82, height=32, hover_color="#BEBEBE"),
    ctk.CTkButton(optionsSideBarFrame, text="💳Carte di credito", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=82, height=32, hover_color="#BEBEBE"),
    tk.Canvas(optionsSideBarFrame, width=OPTIONSIDEBAR_WIDTH - 35, height=1, bg="grey", highlightthickness=0),
    tk.Label(optionsSideBarFrame, text=P_TEXT, font=("Futura", 10), fg="#9C9C9C", background="#F5F5F5"),
    tk.Label(optionsSideBarFrame, text="LockBox® 2024 by Giovanni Desio (amuchina)", font=("Futura", 6), fg="#9C9C9C", background="#F5F5F5")
]

sideBarLogoImage = ImageTk.PhotoImage((Image.open(PAGELOGO_PATH).resize((52, 52))).convert(mode="RGBA"))
sideBarLogoPanel = tk.Label(optionsSideBarFrame, image=sideBarLogoImage, bg="#F5F5F5")
sideBarLogoPanel.grid(row=0, column=0, padx=10, pady=5, sticky="w")

sideBarLogoLabel = tk.Label(optionsSideBarFrame, text=TITLE_NAME, font=("Futura", 22), fg="#E52481", background="#F5F5F5")
sideBarLogoLabel.grid(row=0, column=1, padx=0, pady=0)

for i in range(len(options)):
    options[i].grid(row=rowCounter, column=0, columnspan=2, pady=10)
    rowCounter += 1

searchFrame = tk.Frame(contextMainFrame, bg="#FFFFFF")
searchFrame.pack(fill=tk.X, padx=20, pady=20)

searchEntry = tk.Entry(searchFrame, font=FUTURA_FONT, fg="#9C9C9C", width=30, bd=0, highlightthickness=1, highlightbackground="#E0E0E0")
searchEntry.pack(side=tk.LEFT, padx=(0, 10))

usernameFrame = tk.Frame(contextMainFrame, bg="#FFFFFF")
usernameFrame.pack(side=tk.RIGHT, padx=20)

usernameLabel = tk.Label(usernameFrame, text="Username", font=FUTURA_FONT, fg="#9C9C9C", bg="#FFFFFF")
usernameLabel.pack(side=tk.RIGHT)

mainApp.mainloop()
