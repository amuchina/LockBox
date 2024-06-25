import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image

FUTURA_FONT_XS = ("Futura", 12, 'normal')
FUTURA_FONT_S = ("Futura", 18, 'normal')
FUTURA_FONT_M = ("Futura", 24, 'normal')
FUTURA_FONT_L = ("Futura", 32, 'normal')

APP_BACKGROUND_COLOR = "#FFFFFF"
APP_SECONDARY_COLOR = "#9C9C9C"
TITLE_TEXT_COLOR = "#848484"

ICON_SIZE_S = (30, 30)
ICON_SIZE_L = (32, 32)

TITLE_NAME = "LockBox"
P_TEXT = "Stay safe, stay locked"

MYPASSWORDS_DESCRIPTION = "Salva qui le tue password e tienile al sicuro nei locker! Utilizziamo il moderno ed efficace algoritmo di hashing crittografico SHA-256 con l’aggiunta del tuo “salt” (codice univoco individuale) per rendere ancora piu’ improbabili le minaccie alla sicurezza delle tue password!"

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
    bg=APP_BACKGROUND_COLOR
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
keyImage = ctk.CTkImage(Image.open(EMOJI_KEY_PATH).resize(ICON_SIZE_S))
keyboardImage = ctk.CTkImage(Image.open(EMOJI_PASSWORD_PATH).resize(ICON_SIZE_S))
testImage = ctk.CTkImage(Image.open(EMOJI_TEST_PATH).resize(ICON_SIZE_S))
fileImage = ctk.CTkImage(Image.open(EMOJI_FILE_PATH).resize(ICON_SIZE_S))
permissionsImage = ctk.CTkImage(Image.open(EMOJI_PERMISSIONS_PATH).resize(ICON_SIZE_S))
signatureImage = ctk.CTkImage(Image.open(EMOJI_SIGNATURE_PATH).resize(ICON_SIZE_S))
steganographyImage = ctk.CTkImage(Image.open(EMOJI_STEGANOGRAPHY_PATH).resize(ICON_SIZE_S))
identityImage = ctk.CTkImage(Image.open(EMOJI_IDENTITY_PATH).resize(ICON_SIZE_S))
creditCardImage = ctk.CTkImage(Image.open(EMOJI_CREDIT_CARD_PATH).resize(ICON_SIZE_S))
bellImage = ctk.CTkImage(Image.open(EMOJI_BELL_PATH).resize((25, 25)))
gearImage = ctk.CTkImage(Image.open(EMOJI_GEAR_PATH).resize((25, 25)))
userImage = ctk.CTkImage(Image.open(EMOJI_USER_PATH).resize((25, 25)))

options = [
    tk.Canvas(optionsSideBarFrame, width=OPTIONSIDEBAR_WIDTH - 35, height=1, bg="#A9A9A9", highlightthickness=0),
    ctk.CTkButton(optionsSideBarFrame, image=keyImage, text=" Le mie password", corner_radius=8, font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE", command=lambda: switchpage(page=mypasswordspage)),
    ctk.CTkButton(optionsSideBarFrame, image=keyboardImage, text=" LockGen", corner_radius=8, font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE", command=lambda: switchpage(page=lockgenpage)),
    ctk.CTkButton(optionsSideBarFrame, image=testImage, text=" Test di resistenza", corner_radius=8, font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE", command=lambda: switchpage(page=testpage)),
    tk.Canvas(optionsSideBarFrame, width=OPTIONSIDEBAR_WIDTH - 35, height=1, bg="#A9A9A9", highlightthickness=0),
    ctk.CTkButton(optionsSideBarFrame, image=fileImage, text=" Criptazione dei file", corner_radius=8, font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE", command=lambda: switchpage(page=filespage)),
    ctk.CTkButton(optionsSideBarFrame, image=permissionsImage, text=" Permessi di accesso", corner_radius=8, font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE", command=lambda: switchpage(page=permissionspage)),
    ctk.CTkButton(optionsSideBarFrame, image=signatureImage, text=" Firma digitale", corner_radius=8, font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE", command=lambda: switchpage(page=signaturepage)),
    ctk.CTkButton(optionsSideBarFrame, image=steganographyImage, text=" Steganografia", corner_radius=8, font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE", command=lambda: switchpage(page=steganographypage)),
    tk.Canvas(optionsSideBarFrame, width=OPTIONSIDEBAR_WIDTH - 35, height=1, bg="#A9A9A9", highlightthickness=0),
    ctk.CTkButton(optionsSideBarFrame, image=identityImage, text=" La mia identita’", corner_radius=8, font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE", command=lambda: switchpage(page=identitypage)),
    ctk.CTkButton(optionsSideBarFrame, image=creditCardImage, text=" Carte di credito", corner_radius=8, font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE", command=lambda: switchpage(page=cardspage)),
    tk.Canvas(optionsSideBarFrame, width=OPTIONSIDEBAR_WIDTH - 35, height=1, bg="#A9A9A9", highlightthickness=0),
    tk.Label(optionsSideBarFrame, text=P_TEXT, font=FUTURA_FONT_XS, fg=APP_SECONDARY_COLOR, background="#F5F5F5"),
    tk.Label(optionsSideBarFrame, text="LockBox® 2024 by Giovanni Desio (amuchina)", font=("Futura", 6), fg=APP_SECONDARY_COLOR, background="#F5F5F5")
]

sideBarLogoImage = ImageTk.PhotoImage((Image.open(PAGELOGO_PATH).resize((52, 52))).convert(mode="RGBA"))
sideBarLogoPanel = tk.Label(optionsSideBarFrame, image=sideBarLogoImage, bg="#F5F5F5")
sideBarLogoPanel.grid(row=0, column=0, padx=10, pady=5, sticky="w")

sideBarLogoLabel = tk.Label(optionsSideBarFrame, text=TITLE_NAME, font=("Futura", 22), fg="#E52481", background="#F5F5F5")
sideBarLogoLabel.grid(row=0, column=1, padx=0, pady=0)

for i in range(len(options)):
    options[i].grid(row=rowCounter, column=0, columnspan=2, pady=10)
    rowCounter += 1

# frame to hold both search and username frames
topFrame = tk.Frame(contextMainFrame, bg=APP_BACKGROUND_COLOR)
topFrame.pack(fill=tk.X, padx=20, pady=20)

searchEntry = ctk.CTkEntry(topFrame, font=FUTURA_FONT_S, width=450, height=40, corner_radius=15, fg_color="#E0E0E0", text_color=APP_SECONDARY_COLOR, border_width=0)
searchEntry.pack(side=tk.LEFT, padx=(0, 10))

# Create buttons with emoji images
bellButton = ctk.CTkButton(topFrame, image=bellImage, text="", corner_radius=15, width=40, height=40, fg_color="#DFDFDF", hover_color="#BEBEBE", border_width=0, command=lambda: switchpage(page=notificationhubpage))
bellButton.pack(side=tk.RIGHT, padx=(10, 0))

gearButton = ctk.CTkButton(topFrame, image=gearImage, text="", corner_radius=15, width=40, height=40, fg_color="#DFDFDF", hover_color="#BEBEBE", border_width=0, command=lambda: switchpage(page=settingspage))
gearButton.pack(side=tk.RIGHT, padx=(10, 0))

usernameButton = ctk.CTkButton(topFrame, image=userImage, text="giovi", corner_radius=15, font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", hover_color="#BEBEBE", height=40, border_width=0, command=lambda: switchpage(page=profilepage))
usernameButton.pack(side=tk.RIGHT, padx=(10, 0))

dividerLine = tk.Canvas(contextMainFrame, width=topFrame.winfo_width(), height=1, bg="#A9A9A9", highlightthickness=0)
dividerLine.pack(side=tk.TOP, fill=tk.X, padx=20, pady=(0, 20))


def switchpage(page):
    for frame in mainFrame.winfo_children():
        frame.destroy()
        mainApp.update()

    page()


# pages functions
def mypasswordspage():
    mypasswordsframe = tk.Frame(mainFrame, bg=APP_BACKGROUND_COLOR)
    mypasswordsframe.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    mypasswordspagetitle = ctk.CTkLabel(
        mypasswordsframe,
        image=ctk.CTkImage(Image.open(EMOJI_KEY_PATH), size=ICON_SIZE_L),
        compound=tk.RIGHT,
        text="Le mie password ",
        font=FUTURA_FONT_L,
        text_color=TITLE_TEXT_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    mypasswordspagetitle.grid(row=0, column=0, columnspan=4, pady=(0, 20), padx=(20, 0), sticky="w")

    descriptionframe = ctk.CTkFrame(mypasswordsframe, corner_radius=20, bg_color=APP_BACKGROUND_COLOR, fg_color="#F4F4F4", width=600, height=100)
    descriptionframe.grid(row=1, column=0, columnspan=4, padx=(20, 0), pady=(0, 20), sticky="w")

    description = ctk.CTkLabel(descriptionframe, text=MYPASSWORDS_DESCRIPTION, font=FUTURA_FONT_XS, text_color="#C5C5C5", wraplength=600)
    description.pack(padx=20, pady=20)

    for passwordsRow in range(3):
        for passwordsCol in range(4):
            passwordObj = ctk.CTkFrame(
                mypasswordsframe,
                corner_radius=20,
                bg_color=APP_BACKGROUND_COLOR,
                fg_color="red",
                width=170,
                height=100,
                border_width=1,
                border_color="#A9A9A9"
            )
            passwordObj.grid(row=passwordsRow + 2, column=passwordsCol, padx=10, pady=10)
            passwordServiceName = ctk.CTkLabel(passwordObj, text="instagram", font=FUTURA_FONT_S)
            passwordServiceName.pack(side=tk.BOTTOM, padx=10, pady=10)


def lockgenpage():
    lockgenframe = tk.Frame(mainFrame)
    lockgenframe.configure(background=APP_BACKGROUND_COLOR)
    lockgenpagetitle = ctk.CTkLabel(
        lockgenframe,
        image=ctk.CTkImage(Image.open(EMOJI_PASSWORD_PATH), size=ICON_SIZE_L),
        compound=tk.RIGHT,
        text="LockGen ",
        font=FUTURA_FONT_L,
        text_color=TITLE_TEXT_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    lockgenpagetitle.pack(padx=30, pady=0, anchor="w")
    lockgenframe.pack(fill=tk.BOTH, expand=True)


def testpage():
    testframe = tk.Frame(mainFrame)
    testframe.configure(background=APP_BACKGROUND_COLOR)
    testpagetitle = ctk.CTkLabel(
        testframe,
        image=ctk.CTkImage(Image.open(EMOJI_TEST_PATH), size=ICON_SIZE_L),
        compound=tk.RIGHT,
        text="Test di resistenza ",
        font=FUTURA_FONT_L,
        text_color=TITLE_TEXT_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    testpagetitle.pack(padx=30, pady=0, anchor="w")
    testframe.pack(fill=tk.BOTH, expand=True)


def filespage():
    filesframe = tk.Frame(mainFrame)
    filesframe.configure(background=APP_BACKGROUND_COLOR)
    filespagetitle = ctk.CTkLabel(
        filesframe,
        image=ctk.CTkImage(Image.open(EMOJI_FILE_PATH), size=ICON_SIZE_L),
        compound=tk.RIGHT,
        text="Criptazione dei file ",
        font=FUTURA_FONT_L,
        text_color=TITLE_TEXT_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    filespagetitle.pack(padx=30, pady=0, anchor="w")
    filesframe.pack(fill=tk.BOTH, expand=True)


def permissionspage():
    permissionsframe = tk.Frame(mainFrame)
    permissionsframe.configure(background=APP_BACKGROUND_COLOR)
    permissionspagetitle = ctk.CTkLabel(
        permissionsframe,
        image=ctk.CTkImage(Image.open(EMOJI_PERMISSIONS_PATH), size=ICON_SIZE_L),
        compound=tk.RIGHT,
        text="Permessi di accesso ",
        font=FUTURA_FONT_L,
        text_color=TITLE_TEXT_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    permissionspagetitle.pack(padx=30, pady=0, anchor="w")
    permissionsframe.pack(fill=tk.BOTH, expand=True)


def signaturepage():
    signatureframe = tk.Frame(mainFrame)
    signatureframe.configure(background=APP_BACKGROUND_COLOR)
    signaturepagetitle = ctk.CTkLabel(
        signatureframe,
        image=ctk.CTkImage(Image.open(EMOJI_SIGNATURE_PATH), size=ICON_SIZE_L),
        compound=tk.RIGHT,
        text="Firma digitale ",
        font=FUTURA_FONT_L,
        text_color=TITLE_TEXT_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    signaturepagetitle.pack(padx=30, pady=0, anchor="w")
    signatureframe.pack(fill=tk.BOTH, expand=True)


def steganographypage():
    steganographyframe = tk.Frame(mainFrame)
    steganographyframe.configure(background=APP_BACKGROUND_COLOR)
    steganographypagetitle = ctk.CTkLabel(
        steganographyframe,
        image=ctk.CTkImage(Image.open(EMOJI_STEGANOGRAPHY_PATH), size=ICON_SIZE_L),
        compound=tk.RIGHT,
        text="Steganografia ",
        font=FUTURA_FONT_L,
        text_color=TITLE_TEXT_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    steganographypagetitle.pack(padx=30, pady=0, anchor="w")
    steganographyframe.pack(fill=tk.BOTH, expand=True)


def identitypage():
    identityframe = tk.Frame(mainFrame)
    identityframe.configure(background=APP_BACKGROUND_COLOR)
    identitypagetitle = ctk.CTkLabel(
        identityframe,
        image=ctk.CTkImage(Image.open(EMOJI_IDENTITY_PATH), size=ICON_SIZE_L),
        compound=tk.RIGHT,
        text="La mia identita’ ",
        font=FUTURA_FONT_L,
        text_color=TITLE_TEXT_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    identitypagetitle.pack(padx=30, pady=0, anchor="w")
    identityframe.pack(fill=tk.BOTH, expand=True)


def cardspage():
    cardsframe = tk.Frame(mainFrame)
    cardsframe.configure(background=APP_BACKGROUND_COLOR)
    cardspagetitle = ctk.CTkLabel(
        cardsframe,
        image=ctk.CTkImage(Image.open(EMOJI_CREDIT_CARD_PATH), size=ICON_SIZE_L),
        compound=tk.RIGHT,
        text="Carte di credito ",
        font=FUTURA_FONT_L,
        text_color=TITLE_TEXT_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    cardspagetitle.pack(padx=30, pady=0, anchor="w")
    cardsframe.pack(fill=tk.BOTH, expand=True)


def profilepage():
    profileframe = tk.Frame(mainFrame)
    profileframe.configure(background=APP_BACKGROUND_COLOR)
    profilepagetitle = ctk.CTkLabel(
        profileframe,
        text="Il mio profilo",
        font=FUTURA_FONT_L,
        text_color=TITLE_TEXT_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    profilepagetitle.pack(padx=30, pady=0, anchor="w")
    profileframe.pack(fill=tk.BOTH, expand=True)


def settingspage():
    settingsframe = tk.Frame(mainFrame)
    settingsframe.configure(background=APP_BACKGROUND_COLOR)
    settingspagetitle = ctk.CTkLabel(
        settingsframe,
        text="Impostazioni app",
        font=FUTURA_FONT_L,
        text_color=TITLE_TEXT_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    settingspagetitle.pack(padx=30, pady=0, anchor="w")
    settingsframe.pack(fill=tk.BOTH, expand=True)


def notificationhubpage():
    notificationhubframe = tk.Frame(mainFrame)
    notificationhubframe.configure(background=APP_BACKGROUND_COLOR)
    notificationhubpagetitle = ctk.CTkLabel(
        notificationhubframe,
        text="Centro notifiche",
        font=FUTURA_FONT_L,
        text_color=TITLE_TEXT_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    notificationhubpagetitle.pack(padx=30, pady=0, anchor="w")
    notificationhubframe.pack(fill=tk.BOTH, expand=True)


# main frame in the center of the page, which will contain pages
mainFrame = tk.Frame(contextMainFrame, bg=APP_BACKGROUND_COLOR)
mainFrame.pack(fill=tk.BOTH, expand=True)

mypasswordspage()
mainApp.mainloop()
