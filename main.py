import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image
import LockBoxDBManager as dbm
import mysql.connector
from Locker import Locker
from Auth import Auth
from User import User
import random
import string

FUTURA_FONT_XS = ("Futura", 12, 'normal')
FUTURA_FONT_S = ("Futura", 18, 'normal')
FUTURA_FONT_M = ("Futura", 24, 'normal')
FUTURA_FONT_L = ("Futura", 32, 'normal')

APP_BACKGROUND_COLOR = "#FFFFFF"
APP_SECONDARY_COLOR = "#9C9C9C"
TITLE_TEXT_COLOR = "#848484"

ICON_SIZE_XS = (25, 25)
ICON_SIZE_S = (30, 30)
ICON_SIZE_L = (32, 32)

TITLE_NAME = "LockBox"
P_TEXT = "Stay safe, stay locked"

MYPASSWORDS_DESCRIPTION = "Salva qui le tue password e tienile al sicuro nei locker! Utilizziamo il moderno ed efficace algoritmo di hashing crittografico SHA-256 con l’aggiunta del tuo “salt” (codice univoco individuale) per rendere ancora piu’ improbabili le minaccie alla sicurezza delle tue password!"
NEWPASSWORDS_DESCRIPTION = """In questa pagina puoi salvare le tue password nei tuoi locker
e crittografarle, per rendere piu' difficile il lavoro agli hacker. È facile!
Come Funziona:
Nome del servizio: Scrivi il nome del sito o dell'app.
Username: Inserisci il tuo nome utente.
Password: Digita la tua password segreta.
Conferma Password: Riscrivi la password per sicurezza.
Premi su 'Salva' e voilà, la tua nuova password è al sicuro!"""

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
EMOJI_LOCK_PATH = "./assets/lock.png"

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
bellImage = ctk.CTkImage(Image.open(EMOJI_BELL_PATH).resize((25, 25)), size=ICON_SIZE_XS)
gearImage = ctk.CTkImage(Image.open(EMOJI_GEAR_PATH).resize((25, 25)), size=ICON_SIZE_XS)
userImage = ctk.CTkImage(Image.open(EMOJI_USER_PATH).resize((25, 25)), size=ICON_SIZE_XS)
lockImage = ctk.CTkImage(Image.open(EMOJI_LOCK_PATH).resize((25, 25)), size=ICON_SIZE_S)

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

searchEntry = ctk.CTkEntry(topFrame, font=FUTURA_FONT_S, width=450, height=40, corner_radius=15, fg_color="#E0E0E0", text_color=APP_SECONDARY_COLOR, border_width=0, placeholder_text="🔎 Cerca in LockBox", placeholder_text_color=APP_SECONDARY_COLOR)
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
    if page == newlockerpage:
        for frame in mainFrame.winfo_children():
            frame.destroy()
            mainApp.update()
    else:
        for frame in mainFrame.winfo_children():
            frame.destroy()
            mainApp.update()
    page()


def createnewlocker(lockerdata):
    locker = Locker(service_name=lockerdata[0], username=lockerdata[1], password=lockerdata[2])
    query = "INSERT INTO lockbox.lockers (service_name, username, password, locker_owner_ID) VALUES (%s, %s, %s, %s)"
    try:
        lockboxdbcontroller.get_cursor().execute(query, (locker.service_name, locker.username, locker.password, 1))
        lockboxdbcontroller.conn.commit()
        print("Locker created successfully")
    except mysql.connector.Error as err:
        print(f"Error in locker creation: {err}")
    finally:
        lockboxdbcontroller.get_cursor().close()


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

    # Lista di password vuota iniziale
    passwords_data = []

    def refresh_passwords_grid():
        if 'mypasswordsframe' in globals():
            for widget in mypasswordsframe.winfo_children():
                widget.destroy()

        max_visible_passwords = 11

        # Mostra solo le prime max_visible_passwords password
        for index, saved_password in enumerate(passwords_data[:max_visible_passwords]):
            passwordsRow = index // 4
            passwordsCol = index % 4

            passwordObj = ctk.CTkButton(
                mypasswordsframe,
                corner_radius=20,
                bg_color=APP_BACKGROUND_COLOR,
                fg_color=saved_password.bg_color,
                width=170,
                height=100,
                hover=False
            )
            passwordObj.grid(row=passwordsRow + 2, column=passwordsCol, padx=10, pady=10)
            passwordObj.pack_propagate(False)

            lockerText = ctk.CTkLabel(passwordObj, image=lockImage, compound="left", text=" ..........",
                                      text_color="white",
                                      font=FUTURA_FONT_M, anchor="e", fg_color=saved_password.bg_color,
                                      bg_color=saved_password.bg_color)
            passwordServiceName = ctk.CTkLabel(passwordObj, text=saved_password.service_name, font=FUTURA_FONT_S,
                                               anchor="e", fg_color=saved_password.bg_color,
                                               bg_color=saved_password.bg_color, text_color="white")
            passwordServiceName.pack(padx=5, pady=5)
            lockerText.pack(padx=5, pady=5)

        # Aggiungi il pulsante "+" alla fine della griglia se il numero di password è inferiore a max_visible_passwords
        if len(passwords_data) <= max_visible_passwords:
            addPasswordButton = ctk.CTkButton(
                mypasswordsframe,
                text="+",
                font=FUTURA_FONT_L,
                width=170,
                height=100,
                corner_radius=20,
                command=lambda: switchpage(page=newlockerpage)
            )
            nextRow = len(passwords_data) // 4 + 2
            nextCol = len(passwords_data) % 4
            addPasswordButton.grid(row=nextRow, column=nextCol, padx=10, pady=10)

    # Inizializza la griglia delle password (vuota all'inizio)
    refresh_passwords_grid()


def newlockerpage():
    lockerdata = []

    def fetchandcreate():
        if passwordEntry.get() == confirmPasswordEntry.get():
            lockerdata.append(serviceNameEntry.get())
            lockerdata.append(usernameEntry.get())
            lockerdata.append(passwordEntry.get())
            createnewlocker(lockerdata)
            switchpage(page=mypasswordspage)
        else:
            passwordEntry.configure(border_width=2, border_color="red", text_color="red")
            confirmPasswordEntry.configure(border_width=2, border_color="red", text_color="red")


    newpasswordsframe = ctk.CTkFrame(mainFrame)
    newpasswordsframe.configure(bg_color=APP_BACKGROUND_COLOR, fg_color=APP_BACKGROUND_COLOR)
    newpasswordpagetitle = ctk.CTkLabel(
        newpasswordsframe,
        text="Salva una nuova password ",
        font=FUTURA_FONT_L,
        text_color=TITLE_TEXT_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    newpasswordpagetitle.grid(row=0, column=0, columnspan=4, pady=(0, 20), padx=(20, 0), sticky="w")
    descriptionframe = ctk.CTkFrame(newpasswordsframe, corner_radius=20, bg_color=APP_BACKGROUND_COLOR,
                                    fg_color="#F4F4F4", width=600, height=100)
    descriptionframe.grid(row=1, column=0, columnspan=4, padx=(20, 0), pady=(0, 20), sticky="w")

    description = ctk.CTkLabel(descriptionframe, text=NEWPASSWORDS_DESCRIPTION, font=FUTURA_FONT_XS,
                               text_color="#C5C5C5", wraplength=600)
    description.pack(padx=20, pady=20)
    serviceNameLabel = ctk.CTkLabel(
        newpasswordsframe,
        text="Nome Servizio:",
        font=FUTURA_FONT_S,
        text_color=APP_SECONDARY_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    serviceNameLabel.grid(row=2, column=0, padx=(20, 0), pady=(20, 10), sticky="w")

    serviceNameEntry = ctk.CTkEntry(
        newpasswordsframe,
        font=FUTURA_FONT_S,
        width=400,
        height=40,
        corner_radius=10,
        fg_color="#E0E0E0",
        text_color=APP_SECONDARY_COLOR,
        border_width=0,
        placeholder_text="Inserisci il nome del servizio",
        placeholder_text_color=APP_SECONDARY_COLOR,
    )
    serviceNameEntry.grid(row=2, column=1, padx=(20, 0), pady=(20, 10), sticky="w")

    usernameLabel = ctk.CTkLabel(
        newpasswordsframe,
        text="Username (o email):",
        font=FUTURA_FONT_S,
        text_color=APP_SECONDARY_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    usernameLabel.grid(row=3, column=0, padx=(20, 0), pady=10, sticky="w")

    usernameEntry = ctk.CTkEntry(
        newpasswordsframe,
        font=FUTURA_FONT_S,
        width=400,
        height=40,
        corner_radius=10,
        fg_color="#E0E0E0",
        text_color=APP_SECONDARY_COLOR,
        border_width=0,
        placeholder_text="Inserisci il tuo username",
        placeholder_text_color=APP_SECONDARY_COLOR
    )
    usernameEntry.grid(row=3, column=1, padx=(20, 0), pady=10, sticky="w")

    passwordLabel = ctk.CTkLabel(
        newpasswordsframe,
        text="Password:",
        font=FUTURA_FONT_S,
        text_color=APP_SECONDARY_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    passwordLabel.grid(row=4, column=0, padx=(20, 0), pady=10, sticky="w")

    passwordEntry = ctk.CTkEntry(
        newpasswordsframe,
        font=FUTURA_FONT_S,
        width=400,
        height=40,
        corner_radius=10,
        fg_color="#E0E0E0",
        text_color=APP_SECONDARY_COLOR,
        border_width=0,
        placeholder_text="Inserisci la tua password",
        placeholder_text_color=APP_SECONDARY_COLOR
    )
    passwordEntry.grid(row=4, column=1, padx=(20, 0), pady=10, sticky="w")

    confirmPasswordLabel = ctk.CTkLabel(
        newpasswordsframe,
        text="Conferma Password:",
        font=FUTURA_FONT_S,
        text_color=APP_SECONDARY_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    confirmPasswordLabel.grid(row=5, column=0, padx=(20, 0), pady=10, sticky="w")

    confirmPasswordEntry = ctk.CTkEntry(
        newpasswordsframe,
        font=FUTURA_FONT_S,
        width=400,
        height=40,
        corner_radius=10,
        fg_color="#E0E0E0",
        text_color=APP_SECONDARY_COLOR,
        border_width=0,
        placeholder_text="Riscrivi la tua password",
        placeholder_text_color=APP_SECONDARY_COLOR
    )
    confirmPasswordEntry.grid(row=5, column=1, padx=(20, 0), pady=10, sticky="w")

    saveButton = ctk.CTkButton(
        newpasswordsframe,
        text="Salva",
        text_color="white",
        font=FUTURA_FONT_S,
        corner_radius=15,
        width=150,
        height=40,
        fg_color="#FB62AC",
        hover_color="#F1328D",
        border_width=0,
        command=lambda: fetchandcreate()
    )
    saveButton.grid(row=6, column=1, pady=(15, 0), padx=(0, 0), sticky="e")

    newpasswordsframe.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

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
    user = User("amuchina", "redos")
    authenticator = Auth()
    authenticateduser = authenticator.register(user.to_dict(), lockboxdbcontroller)


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
lockboxdbcontroller = dbm.LockBoxDBManager()
mainApp.mainloop()
