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

# Add paths for emoji images
EMOJI_KEY_PATH = "./assets/key.png"
EMOJI_PASSWORD_PATH = "./assets/password.png"
EMOJI_TEST_PATH = "./assets/test.png"
EMOJI_FILE_PATH = "./assets/file.png"
EMOJI_PERMISSIONS_PATH = "./assets/permissions.png"
EMOJI_SIGNATURE_PATH = "./assets/signature.png"
EMOJI_STEGANOGRAPHY_PATH = "./assets/steganography.png"
EMOJI_IDENTITY_PATH = "./assets/identity.png"
EMOJI_CREDIT_CARD_PATH = "./assets/credit_card.png"
EMOJI_BELL_PATH = "./assets/bell.png"
EMOJI_GEAR_PATH = "./assets/gear.png"
EMOJI_USER_PATH = "./assets/user.png"

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

# Load emoji images
keyImage = ImageTk.PhotoImage(Image.open(EMOJI_KEY_PATH).resize((20, 20)))
keyboardImage = ImageTk.PhotoImage(Image.open(EMOJI_PASSWORD_PATH).resize((20, 20)))
testImage = ImageTk.PhotoImage(Image.open(EMOJI_TEST_PATH).resize((20, 20)))
fileImage = ImageTk.PhotoImage(Image.open(EMOJI_FILE_PATH).resize((20, 20)))
permissionsImage = ImageTk.PhotoImage(Image.open(EMOJI_PERMISSIONS_PATH).resize((20, 20)))
signatureImage = ImageTk.PhotoImage(Image.open(EMOJI_SIGNATURE_PATH).resize((20, 20)))
steganographyImage = ImageTk.PhotoImage(Image.open(EMOJI_STEGANOGRAPHY_PATH).resize((20, 20)))
identityImage = ImageTk.PhotoImage(Image.open(EMOJI_IDENTITY_PATH).resize((20, 20)))
creditCardImage = ImageTk.PhotoImage(Image.open(EMOJI_CREDIT_CARD_PATH).resize((20, 20)))
bellImage = ImageTk.PhotoImage(Image.open(EMOJI_BELL_PATH).resize((25, 25)))
gearImage = ImageTk.PhotoImage(Image.open(EMOJI_GEAR_PATH).resize((25, 25)))
userImage = ImageTk.PhotoImage(Image.open(EMOJI_USER_PATH).resize((25, 25)))

options = [
    tk.Canvas(optionsSideBarFrame, width=OPTIONSIDEBAR_WIDTH - 35, height=1, bg="grey", highlightthickness=0),
    ctk.CTkButton(optionsSideBarFrame, image=keyImage, text=" Le mie password", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE"),
    ctk.CTkButton(optionsSideBarFrame, image=keyboardImage, text=" LockGen", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE"),
    ctk.CTkButton(optionsSideBarFrame, image=testImage, text=" Test di resistenza", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE"),
    tk.Canvas(optionsSideBarFrame, width=OPTIONSIDEBAR_WIDTH - 35, height=1, bg="grey", highlightthickness=0),
    ctk.CTkButton(optionsSideBarFrame, image=fileImage, text=" Criptazione dei file", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE"),
    ctk.CTkButton(optionsSideBarFrame, image=permissionsImage, text=" Permessi di accesso", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE"),
    ctk.CTkButton(optionsSideBarFrame, image=signatureImage, text=" Firma digitale", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE"),
    ctk.CTkButton(optionsSideBarFrame, image=steganographyImage, text=" Steganografia", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE"),
    tk.Canvas(optionsSideBarFrame, width=OPTIONSIDEBAR_WIDTH - 35, height=1, bg="grey", highlightthickness=0),
    ctk.CTkButton(optionsSideBarFrame, image=identityImage, text=" La mia identita’", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE"),
    ctk.CTkButton(optionsSideBarFrame, image=creditCardImage, text=" Carte di credito", corner_radius=8, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE"),
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

# Create a frame to hold both search and username frames
topFrame = tk.Frame(contextMainFrame, bg="#FFFFFF")
topFrame.pack(fill=tk.X, padx=20, pady=20)

searchEntry = ctk.CTkEntry(topFrame, font=FUTURA_FONT, width=450, height=40, corner_radius=15, fg_color="#E0E0E0", text_color="#9C9C9C", border_width=0)
searchEntry.pack(side=tk.LEFT, padx=(0, 10))

# Create buttons with emoji images
bellButton = ctk.CTkButton(topFrame, image=bellImage, text="", corner_radius=15, width=40, height=40, fg_color="#DFDFDF", hover_color="#BEBEBE", border_width=0)
bellButton.pack(side=tk.RIGHT, padx=(10, 0))

gearButton = ctk.CTkButton(topFrame, image=gearImage, text="", corner_radius=15, width=40, height=40, fg_color="#DFDFDF", hover_color="#BEBEBE", border_width=0)
gearButton.pack(side=tk.RIGHT, padx=(10, 0))

usernameButton = ctk.CTkButton(topFrame, image=userImage, text="giovi", corner_radius=15, font=FUTURA_FONT, text_color="#9C9C9C", fg_color="#DFDFDF", hover_color="#BEBEBE", height=40, border_width=0)
usernameButton.pack(side=tk.RIGHT, padx=(10, 0))

mainApp.mainloop()
