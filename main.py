import tkinter as tk
import customtkinter as ctk
from PIL import ImageTk, Image
import LockBoxDBManager as dbm
import mysql.connector
from Locker import Locker
from Auth import Auth
from User import User
from HashEncrypter import HashEncrypter
from dotenv import load_dotenv
import platform
import os

if platform.system() == 'Linux' or platform.system() == 'Darwin':
    load_dotenv("envfiles/.env.shared.linux")
elif platform.system() == 'Windows':
    load_dotenv("envfiles/.env.shared.windows")
else:
    print("ENV files not loaded: os undetectable")

global hashencrypter

global sideBarLogoImage
global topContextFrame
global centerContextFrame

global personal_user_string_salt, personal_user_byte_salt

FUTURA_FONT_XS = ("Futura", 12, 'normal')
FUTURA_FONT_S = ("Futura", 18, 'normal')
FUTURA_FONT_M = ("Futura", 24, 'normal')
FUTURA_FONT_L = ("Futura", 32, 'normal')
FUTURA_FONT_XL = ("Futura", 42, 'normal')

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
MYPROFILE_DESCRIPTION = """Benvenuto nella tua area personale! Qui puoi visualizzare e aggiornare tutte le tue informazioni. 
Clicca sull'icona della matita accanto a ciascun campo per modificarlo. 
Dopo aver effettuato le modifiche, assicurati di salvare i tuoi dati per mantenerli aggiornati."""

WINDOW_DIM = "1100x700"

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700

OPTIONSIDEBAR_WIDTH = 237

current_authenticated_user = None
authenticator = Auth()

fieldsdata = []

mainApp = tk.Tk()

# app init settings

mainApp.title("LockBox")
mainApp.iconbitmap(os.getenv("ICO_LOGO_PATH"))
mainApp.geometry(WINDOW_DIM)
mainApp.resizable(False, False)

# frames setup

appFrame = tk.Frame(
    mainApp,
    bg=APP_BACKGROUND_COLOR,
)

appFrame.pack(fill=tk.BOTH, expand=False)

# Load emoji images
keyImage = ctk.CTkImage(Image.open(os.getenv("EMOJI_KEY_PATH")).resize(ICON_SIZE_S))
keyboardImage = ctk.CTkImage(Image.open(os.getenv("EMOJI_PASSWORD_PATH")).resize(ICON_SIZE_S))
testImage = ctk.CTkImage(Image.open(os.getenv("EMOJI_TEST_PATH")).resize(ICON_SIZE_S))
fileImage = ctk.CTkImage(Image.open(os.getenv("EMOJI_FILE_PATH")).resize(ICON_SIZE_S))
permissionsImage = ctk.CTkImage(Image.open(os.getenv("EMOJI_PERMISSIONS_PATH")).resize(ICON_SIZE_S))
signatureImage = ctk.CTkImage(Image.open(os.getenv("EMOJI_SIGNATURE_PATH")).resize(ICON_SIZE_S))
steganographyImage = ctk.CTkImage(Image.open(os.getenv("EMOJI_STEGANOGRAPHY_PATH")).resize(ICON_SIZE_S))
identityImage = ctk.CTkImage(Image.open(os.getenv("EMOJI_IDENTITY_PATH")).resize(ICON_SIZE_S))
creditCardImage = ctk.CTkImage(Image.open(os.getenv("EMOJI_CREDIT_CARD_PATH")).resize(ICON_SIZE_S))
bellImage = ctk.CTkImage(Image.open(os.getenv("EMOJI_BELL_PATH")).resize((25, 25)), size=ICON_SIZE_XS)
gearImage = ctk.CTkImage(Image.open(os.getenv("EMOJI_GEAR_PATH")).resize((25, 25)), size=ICON_SIZE_XS)
userImage = ctk.CTkImage(Image.open(os.getenv("EMOJI_USER_PATH")).resize((25, 25)), size=ICON_SIZE_XS)
lockImage = ctk.CTkImage(Image.open(os.getenv("EMOJI_LOCK_PATH")).resize((25, 25)), size=ICON_SIZE_S)
logoImage = ctk.CTkImage(Image.open(os.getenv("LOGO_PATH")).convert(mode='RGBA'), size=(300, 300))
pencilImage = ctk.CTkImage(Image.open(os.getenv("EMOJI_PENCIL_PATH")).resize((25, 25)), size=ICON_SIZE_XS)


def clearcell(frame, row_index, column_index):
    children = frame.grid_slaves()
    for widget in children:
        info = widget.grid_info()
        if info["row"] == row_index and info["column"] == column_index:
            widget.grid_forget()


def clearcolumn(frame, column_index):
    children = frame.grid_slaves()
    for widget in children:
        if widget.grid_info()["column"] == column_index:
            widget.grid_forget()


def welcomepage():

    def fetchandsendlogindata(usernameEntry, passwordEntry):
        user = User("", "", usernameEntry.get(), passwordEntry.get())
        checklogin(user)
        if current_authenticated_user is None:
            usernameEntry.configure(border_width=2, border_color="red", text_color="red")
            passwordEntry.configure(border_width=2, border_color="red", text_color="red")

    def fetchandsendregisterdata(nameEntry, surnameEntry, usernameEntry, passwordEntry, confirmPasswordEntry, errorLabel, registerButton):
        global hashencrypter, personal_user_string_salt, personal_user_byte_salt
        if passwordEntry.get() != confirmPasswordEntry.get():
            print("Passwords doesnt match")
            passwordEntry.configure(border_width=2, border_color="red", text_color="red")
            confirmPasswordEntry.configure(border_width=2, border_color="red", text_color="red")
        else:
            newuser = User(nameEntry.get(), surnameEntry.get(), usernameEntry.get(), passwordEntry.get())
            accountuserrequest = authenticator.register(newuser, lockboxdbcontroller)
            hashencrypter = HashEncrypter()
            personal_user_string_salt, personal_user_byte_salt = hashencrypter.generate_salt(authenticator, lockboxdbcontroller)
            if accountuserrequest:
                set_current_authenticated_user(user=newuser)
                switchpage(page=homepage)
            else:
                print("User already exists")
                usernameEntry.configure(border_width=2, border_color="red", text_color="red")
                errorLabel.grid(row=8, column=2, pady=(5, 5))
                registerButton.grid(row=9, column=2, pady=(0, 50), sticky="n")

    def showloginform():
        clearcolumn(welcomeFrame, 2)
        loginFrame = tk.Frame(welcomeFrame, bg=APP_BACKGROUND_COLOR)
        loginFrame.grid(row=1, column=2, rowspan=3, sticky="nsew")
        loginFrame.grid_rowconfigure(0, weight=1)
        loginFrame.grid_rowconfigure(5, weight=1)
        loginFrame.grid_columnconfigure(0, weight=1)

        loginpagetitle = ctk.CTkLabel(
            loginFrame,
            text="Accedi",
            font=FUTURA_FONT_XL,
            text_color="#C52A74",
            fg_color=APP_BACKGROUND_COLOR,
            bg_color=APP_BACKGROUND_COLOR
        )
        loginpagetitle.grid(row=1, column=0, pady=(0, 10))

        registerLabel = ctk.CTkLabel(
            loginFrame,
            text="Non hai un account? Registrati",
            font=("Futura", 14, "underline"),
            text_color=APP_SECONDARY_COLOR,
            fg_color=APP_BACKGROUND_COLOR,
            bg_color=APP_BACKGROUND_COLOR,
            cursor="hand2"
        )
        registerLabel.grid(row=2, column=0, pady=(0, 10))
        registerLabel.bind("<Button-1>", lambda e: showregistrationform())

        usernameEntry = ctk.CTkEntry(
            loginFrame,
            font=FUTURA_FONT_S,
            width=250,
            height=40,
            corner_radius=10,
            fg_color="#E0E0E0",
            text_color=APP_SECONDARY_COLOR,
            border_width=0,
            placeholder_text="Username (o email)",
            placeholder_text_color=APP_SECONDARY_COLOR,
        )
        usernameEntry.grid(row=3, column=0, pady=(0, 10))

        passwordEntry = ctk.CTkEntry(
            loginFrame,
            font=FUTURA_FONT_S,
            width=250,
            height=40,
            corner_radius=10,
            fg_color="#E0E0E0",
            text_color=APP_SECONDARY_COLOR,
            border_width=0,
            placeholder_text="Password",
            placeholder_text_color=APP_SECONDARY_COLOR
        )
        passwordEntry.grid(row=4, column=0, pady=(0, 10))

        submitButton = ctk.CTkButton(
            loginFrame,
            text="Accedi",
            text_color="white",
            font=FUTURA_FONT_S,
            corner_radius=15,
            width=150,
            height=40,
            fg_color="#FB62AC",
            hover_color="#F1328D",
            border_width=0,
            command=lambda: fetchandsendlogindata(usernameEntry, passwordEntry)
        )
        submitButton.grid(row=5, column=0, pady=(0, 50))

        emptyLabel3 = ctk.CTkLabel(welcomeFrame, text="", bg_color=APP_BACKGROUND_COLOR)
        emptyLabel3.grid(row=4, column=2, sticky="nsew")

    def showregistrationform():
        clearcolumn(welcomeFrame, 2)
        registerFrame = tk.Frame(welcomeFrame, bg=APP_BACKGROUND_COLOR)
        registerFrame.grid(row=1, column=2, rowspan=3, sticky="nsew", padx=(180, 0))
        registerFrame.grid_rowconfigure(0, weight=1)
        registerFrame.grid_rowconfigure(1, weight=1)
        registerFrame.grid_rowconfigure(2, weight=1)
        registerFrame.grid_rowconfigure(3, weight=1)
        registerFrame.grid_rowconfigure(4, weight=1)
        registerFrame.grid_rowconfigure(5, weight=1)
        registerFrame.grid_rowconfigure(6, weight=1)

        emptyLabel1 = ctk.CTkLabel(registerFrame, text="", bg_color=APP_BACKGROUND_COLOR)
        emptyLabel1.grid(row=0, column=2)

        registrationpagetitle = ctk.CTkLabel(
            registerFrame,
            text="Registrati",
            font=FUTURA_FONT_XL,
            text_color="#C52A74",
            fg_color=APP_BACKGROUND_COLOR,
            bg_color=APP_BACKGROUND_COLOR
        )
        registrationpagetitle.grid(row=1, column=2, pady=(20, 0), sticky="n")

        loginLabel = ctk.CTkLabel(
            registerFrame,
            text="Hai gia' un account? Accedi",
            font=("Futura", 14, "underline"),
            text_color=APP_SECONDARY_COLOR,
            fg_color=APP_BACKGROUND_COLOR,
            bg_color=APP_BACKGROUND_COLOR,
            cursor="hand2"
        )
        loginLabel.grid(row=2, column=2, pady=(0, 10))
        loginLabel.bind("<Button-1>", lambda e: showloginform())

        nameEntry = ctk.CTkEntry(
            registerFrame,
            font=FUTURA_FONT_S,
            width=250,
            height=40,
            corner_radius=10,
            fg_color="#E0E0E0",
            text_color=APP_SECONDARY_COLOR,
            border_width=0,
            placeholder_text="Nome",
            placeholder_text_color=APP_SECONDARY_COLOR,
        )
        nameEntry.grid(row=3, column=2, pady=(0, 10), sticky="n")

        surnameEntry = ctk.CTkEntry(
            registerFrame,
            font=FUTURA_FONT_S,
            width=250,
            height=40,
            corner_radius=10,
            fg_color="#E0E0E0",
            text_color=APP_SECONDARY_COLOR,
            border_width=0,
            placeholder_text="Cognome",
            placeholder_text_color=APP_SECONDARY_COLOR,
        )
        surnameEntry.grid(row=4, column=2, pady=(0, 10), sticky="n")

        newUsernameEntry = ctk.CTkEntry(
            registerFrame,
            font=FUTURA_FONT_S,
            width=250,
            height=40,
            corner_radius=10,
            fg_color="#E0E0E0",
            text_color=APP_SECONDARY_COLOR,
            border_width=0,
            placeholder_text="Username (o email) *",
            placeholder_text_color=APP_SECONDARY_COLOR,
        )
        newUsernameEntry.grid(row=5, column=2, pady=(0, 10), sticky="n")

        newPasswordEntry = ctk.CTkEntry(
            registerFrame,
            font=FUTURA_FONT_S,
            width=250,
            height=40,
            corner_radius=10,
            fg_color="#E0E0E0",
            text_color=APP_SECONDARY_COLOR,
            border_width=0,
            placeholder_text="Password *",
            placeholder_text_color=APP_SECONDARY_COLOR,
        )
        newPasswordEntry.grid(row=6, column=2, pady=(0, 10), sticky="n")

        confirmPasswordEntry = ctk.CTkEntry(
            registerFrame,
            font=FUTURA_FONT_S,
            width=250,
            height=40,
            corner_radius=10,
            fg_color="#E0E0E0",
            text_color=APP_SECONDARY_COLOR,
            border_width=0,
            placeholder_text="Conferma password *",
            placeholder_text_color=APP_SECONDARY_COLOR,
        )
        confirmPasswordEntry.grid(row=7, column=2, pady=(0, 20), sticky="n")

        errorLabel = ctk.CTkLabel(
            registerFrame,
            text="Un account con questo username esiste gia'",
            font=("Futura", 14, "normal"),
            text_color="red",
            fg_color=APP_BACKGROUND_COLOR,
            bg_color=APP_BACKGROUND_COLOR,
        )

        registerButton = ctk.CTkButton(
            registerFrame,
            text="Registrati",
            text_color="#FFFFFF",
            font=FUTURA_FONT_S,
            corner_radius=15,
            width=150,
            height=40,
            fg_color="#FB62AC",
            hover_color="#F1328D",
            border_width=0,
            command=lambda: fetchandsendregisterdata(nameEntry, surnameEntry, newUsernameEntry, newPasswordEntry, confirmPasswordEntry, errorLabel, registerButton)
        )
        registerButton.grid(row=8, column=2, pady=(0, 50), sticky="n")

    welcomeFrame = tk.Frame(
        mainApp,
        bg=APP_BACKGROUND_COLOR
    )
    welcomeFrame.pack(fill=tk.BOTH, expand=True)

    welcomeFrame.grid_rowconfigure(0, weight=1)
    welcomeFrame.grid_rowconfigure(1, weight=1)
    welcomeFrame.grid_rowconfigure(2, weight=1)
    welcomeFrame.grid_rowconfigure(3, weight=1)
    welcomeFrame.grid_rowconfigure(4, weight=1)
    welcomeFrame.grid_columnconfigure(0, weight=1)
    welcomeFrame.grid_columnconfigure(1, weight=0)
    welcomeFrame.grid_columnconfigure(2, weight=1)

    titleLabel = ctk.CTkLabel(welcomeFrame, text="LockBox", font=("Futura", 50), text_color="#C52A74", bg_color=APP_BACKGROUND_COLOR)
    titleLabel.grid(row=1, column=0, sticky='nsew', pady=(0, 0))

    subtitleLabel = ctk.CTkLabel(welcomeFrame, text="""
    Stay safe, stay locked

    by Giovanni Desio
    """, font=("Futura", 20), text_color=TITLE_TEXT_COLOR, bg_color=APP_BACKGROUND_COLOR)
    subtitleLabel.grid(row=2, column=0, sticky='n', pady=(0, 0))

    welcomeLogoPanel = ctk.CTkLabel(welcomeFrame, text="", image=logoImage, bg_color=APP_BACKGROUND_COLOR)
    welcomeLogoPanel.grid(row=3, column=0, sticky='nsew', pady=(0, 0))

    emptyLabel0 = ctk.CTkLabel(welcomeFrame, text="", bg_color=APP_BACKGROUND_COLOR)
    emptyLabel0.grid(row=4, column=0, sticky="nsew")

    divider = tk.Frame(welcomeFrame, bg="#C9C9C9", width=1)
    divider.grid(row=0, column=1, rowspan=5, sticky="ns")

    showloginform()


def set_current_authenticated_user(user):
    global current_authenticated_user
    current_authenticated_user = user


def logoutuser():
    authenticator.logout()
    set_current_authenticated_user(None)
    print("User logged out")
    mainApp.destroy()


def checklogin(user: User):
    authuser = authenticator.login(user, lockboxdbcontroller)
    if authuser:
        set_current_authenticated_user(user=authuser)
        switchpage(page=homepage)
    else:
        print("Not logged in (Invalid username or password)")
        return False


def homepage():
    global topContextFrame
    global centerContextFrame
    global sideBarLogoImage

    optionsSideBarFrame = tk.Frame(
        appFrame,
        bg="#F5F5F5"
    )
    optionsSideBarFrame.pack(
        side=tk.LEFT,
        fill=tk.Y
    )
    topContextFrame = tk.Frame(
        appFrame,
        bg=APP_BACKGROUND_COLOR,
        height=100
    )
    topContextFrame.pack(
        side=tk.TOP,
        fill=tk.X
    )
    centerContextFrame = tk.Frame(
        appFrame,
        bg=APP_BACKGROUND_COLOR,
    )
    centerContextFrame.pack(
        side=tk.LEFT,
        fill=tk.X,
        expand=False
    )
    optionsSideBarFrame.pack_propagate(False)
    centerContextFrame.pack_propagate(False)

    optionsSideBarFrame.configure(
        width=OPTIONSIDEBAR_WIDTH,
    )
    centerContextFrame.configure(
        width=WINDOW_WIDTH - OPTIONSIDEBAR_WIDTH,
        height=WINDOW_HEIGHT
    )
    rowCounter = 2
    options = [
        tk.Canvas(optionsSideBarFrame, width=OPTIONSIDEBAR_WIDTH - 35, height=1, bg="#A9A9A9", highlightthickness=0),
        ctk.CTkButton(optionsSideBarFrame, image=keyImage, text=" Le mie password", corner_radius=8, font=FUTURA_FONT_S,
                      text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE",
                      command=lambda: switchpage(page=mypasswordspage)),
        ctk.CTkButton(optionsSideBarFrame, image=keyboardImage, text=" LockGen", corner_radius=8, font=FUTURA_FONT_S,
                      text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32, hover_color="#BEBEBE",
                      command=lambda: switchpage(page=lockgenpage)),
        ctk.CTkButton(optionsSideBarFrame, image=testImage, text=" Test di resistenza", corner_radius=8,
                      font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32,
                      hover_color="#BEBEBE", command=lambda: switchpage(page=testpage)),
        tk.Canvas(optionsSideBarFrame, width=OPTIONSIDEBAR_WIDTH - 35, height=1, bg="#A9A9A9", highlightthickness=0),
        ctk.CTkButton(optionsSideBarFrame, image=fileImage, text=" Criptazione dei file", corner_radius=8,
                      font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32,
                      hover_color="#BEBEBE", command=lambda: switchpage(page=filespage)),
        ctk.CTkButton(optionsSideBarFrame, image=permissionsImage, text=" Permessi di accesso", corner_radius=8,
                      font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32,
                      hover_color="#BEBEBE", command=lambda: switchpage(page=permissionspage)),
        ctk.CTkButton(optionsSideBarFrame, image=signatureImage, text=" Firma digitale", corner_radius=8,
                      font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32,
                      hover_color="#BEBEBE", command=lambda: switchpage(page=signaturepage)),
        ctk.CTkButton(optionsSideBarFrame, image=steganographyImage, text=" Steganografia", corner_radius=8,
                      font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32,
                      hover_color="#BEBEBE", command=lambda: switchpage(page=steganographypage)),
        tk.Canvas(optionsSideBarFrame, width=OPTIONSIDEBAR_WIDTH - 35, height=1, bg="#A9A9A9", highlightthickness=0),
        ctk.CTkButton(optionsSideBarFrame, image=identityImage, text=" La mia identita’", corner_radius=8,
                      font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32,
                      hover_color="#BEBEBE", command=lambda: switchpage(page=identitypage)),
        ctk.CTkButton(optionsSideBarFrame, image=creditCardImage, text=" Carte di credito", corner_radius=8,
                      font=FUTURA_FONT_S, text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", width=200, height=32,
                      hover_color="#BEBEBE", command=lambda: switchpage(page=cardspage)),
        tk.Canvas(optionsSideBarFrame, width=OPTIONSIDEBAR_WIDTH - 35, height=1, bg="#A9A9A9", highlightthickness=0),
        tk.Label(optionsSideBarFrame, text=P_TEXT, font=FUTURA_FONT_XS, fg=APP_SECONDARY_COLOR, background="#F5F5F5"),
        tk.Label(optionsSideBarFrame, text="LockBox® 2024 by Giovanni Desio (amuchina)", font=("Futura", 6),
                 fg=APP_SECONDARY_COLOR, background="#F5F5F5")
    ]

    sideBarLogoImage = ImageTk.PhotoImage((Image.open(os.getenv("PAGELOGO_PATH")).resize((52, 52))).convert(mode="RGBA"))
    sideBarLogoPanel = tk.Label(optionsSideBarFrame, image=sideBarLogoImage, bg="#F5F5F5")
    sideBarLogoPanel.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    sideBarLogoLabel = tk.Label(optionsSideBarFrame, text=TITLE_NAME, font=("Futura", 22), fg="#E52481",
                                background="#F5F5F5")
    sideBarLogoLabel.grid(row=0, column=1, padx=0, pady=0)

    for i in range(len(options)):
        options[i].grid(row=rowCounter, column=0, columnspan=2, pady=10)
        rowCounter += 1

    # frame to hold both search and username frames
    topFrame = tk.Frame(topContextFrame, bg=APP_BACKGROUND_COLOR)
    topFrame.pack(fill=tk.X, padx=20, pady=20)

    searchEntry = ctk.CTkEntry(topFrame, font=FUTURA_FONT_S, width=450, height=40, corner_radius=15, fg_color="#E0E0E0",
                               text_color=APP_SECONDARY_COLOR, border_width=0, placeholder_text="🔎 Cerca in LockBox",
                               placeholder_text_color=APP_SECONDARY_COLOR)
    searchEntry.pack(side=tk.LEFT, padx=(0, 10))

    # Create buttons with emoji images
    bellButton = ctk.CTkButton(topFrame, image=bellImage, text="", corner_radius=15, width=40, height=40,
                               fg_color="#DFDFDF", hover_color="#BEBEBE", border_width=0,
                               command=lambda: switchpage(page=notificationhubpage))
    bellButton.pack(side=tk.RIGHT, padx=(10, 0))

    gearButton = ctk.CTkButton(topFrame, image=gearImage, text="", corner_radius=15, width=40, height=40,
                               fg_color="#DFDFDF", hover_color="#BEBEBE", border_width=0,
                               command=lambda: switchpage(page=settingspage))
    gearButton.pack(side=tk.RIGHT, padx=(10, 0))

    usernameButton = ctk.CTkButton(topFrame, image=userImage, text=authenticator.get_authenticated_user()[3], corner_radius=15, font=FUTURA_FONT_S,
                                   text_color=APP_SECONDARY_COLOR, fg_color="#DFDFDF", hover_color="#BEBEBE", height=40,
                                   border_width=0, command=lambda: switchpage(page=profilepage))
    usernameButton.pack(side=tk.RIGHT, padx=(10, 0))

    dividerLine = tk.Canvas(topContextFrame, width=topFrame.winfo_width(), height=1, bg="#A9A9A9",
                            highlightthickness=0)
    dividerLine.pack(side=tk.TOP, fill=tk.X, padx=20, pady=(0, 20))

    mypasswordspage()


def switchpage(page):
    if page in [homepage, welcomepage]:
        for frame in appFrame.winfo_children():
            frame.destroy()
            mainApp.update()
    else:
        for frame in centerContextFrame.winfo_children():
            frame.destroy()
            mainApp.update()
    page()


# pages functions
def mypasswordspage():
    mypasswordsframe = tk.Frame(centerContextFrame, bg=APP_BACKGROUND_COLOR)
    mypasswordsframe.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    mypasswordspagetitle = ctk.CTkLabel(
        mypasswordsframe,
        image=ctk.CTkImage(Image.open(os.getenv("EMOJI_KEY_PATH")), size=ICON_SIZE_L),
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

    refresh_passwords_grid()


def newlockerpage():
    global personal_user_string_salt

    lockerdata = []

    def fetchandcreatelocker():
        if passwordEntry.get() == confirmPasswordEntry.get():
            lockerdata.append(serviceNameEntry.get())
            lockerdata.append(usernameEntry.get())
            lockerdata.append(passwordEntry.get())
            createnewlocker(lockerdata)
            switchpage(page=mypasswordspage)
        else:
            passwordEntry.configure(border_width=2, border_color="red", text_color="red")
            confirmPasswordEntry.configure(border_width=2, border_color="red", text_color="red")

    def createnewlocker(newlockerdata):
        locker = Locker(service_name=newlockerdata[0], username=newlockerdata[1], password=newlockerdata[2])
        query = "INSERT INTO lockbox.lockers (service_name, username, password, locker_owner_ID) VALUES (%s, %s, %s, %s)"
        try:
            # continue
            encrypted_locker_password_data = locker.save(hashencrypter, personal_user_string_salt)
            lockboxdbcontroller.get_cursor().execute(query, (locker.service_name, locker.username, encrypted_locker_password_data, authenticator.get_authenticated_user_id()))
            lockboxdbcontroller.conn.commit()
            print("Locker created successfully")
        except mysql.connector.Error as err:
            print(f"Error in locker creation: {err}")
        finally:
            lockboxdbcontroller.get_cursor().close()

    newlockerframe = ctk.CTkFrame(centerContextFrame)
    newlockerframe.configure(bg_color=APP_BACKGROUND_COLOR, fg_color=APP_BACKGROUND_COLOR)
    newlockerpagetitle = ctk.CTkLabel(
        newlockerframe,
        text="Salva una nuova password ",
        font=FUTURA_FONT_L,
        text_color=TITLE_TEXT_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    newlockerpagetitle.grid(row=0, column=0, columnspan=4, pady=(0, 20), padx=(20, 0), sticky="w")

    descriptionframe = ctk.CTkFrame(newlockerframe, corner_radius=20, bg_color=APP_BACKGROUND_COLOR,
                                    fg_color="#F4F4F4", width=600, height=100)
    descriptionframe.grid(row=1, column=0, columnspan=4, padx=(20, 0), pady=(0, 20), sticky="w")

    description = ctk.CTkLabel(descriptionframe, text=NEWPASSWORDS_DESCRIPTION, font=FUTURA_FONT_XS,
                               text_color="#C5C5C5", wraplength=600)
    description.pack(padx=20, pady=20)
    serviceNameLabel = ctk.CTkLabel(
        newlockerframe,
        text="Nome Servizio:",
        font=FUTURA_FONT_S,
        text_color=APP_SECONDARY_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    serviceNameLabel.grid(row=2, column=0, padx=(20, 0), pady=(20, 10), sticky="w")

    serviceNameEntry = ctk.CTkEntry(
        newlockerframe,
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
        newlockerframe,
        text="Username (o email):",
        font=FUTURA_FONT_S,
        text_color=APP_SECONDARY_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    usernameLabel.grid(row=3, column=0, padx=(20, 0), pady=10, sticky="w")

    usernameEntry = ctk.CTkEntry(
        newlockerframe,
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
        newlockerframe,
        text="Password:",
        font=FUTURA_FONT_S,
        text_color=APP_SECONDARY_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    passwordLabel.grid(row=4, column=0, padx=(20, 0), pady=10, sticky="w")

    passwordEntry = ctk.CTkEntry(
        newlockerframe,
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
        newlockerframe,
        text="Conferma Password:",
        font=FUTURA_FONT_S,
        text_color=APP_SECONDARY_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    confirmPasswordLabel.grid(row=5, column=0, padx=(20, 0), pady=10, sticky="w")

    confirmPasswordEntry = ctk.CTkEntry(
        newlockerframe,
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
        newlockerframe,
        text="Salva",
        text_color="white",
        font=FUTURA_FONT_S,
        corner_radius=15,
        width=150,
        height=40,
        fg_color="#FB62AC",
        hover_color="#F1328D",
        border_width=0,
        command=lambda: fetchandcreatelocker()
    )
    saveButton.grid(row=6, column=1, pady=(15, 0), padx=(0, 0), sticky="e")

    newlockerframe.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)


def lockgenpage():
    lockgenframe = tk.Frame(centerContextFrame)
    lockgenframe.configure(background=APP_BACKGROUND_COLOR)
    lockgenpagetitle = ctk.CTkLabel(
        lockgenframe,
        image=ctk.CTkImage(Image.open(os.getenv("EMOJI_PASSWORD_PATH")), size=ICON_SIZE_L),
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
    testframe = tk.Frame(centerContextFrame)
    testframe.configure(background=APP_BACKGROUND_COLOR)
    testpagetitle = ctk.CTkLabel(
        testframe,
        image=ctk.CTkImage(Image.open(os.getenv("EMOJI_TEST_PATH")), size=ICON_SIZE_L),
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
    filesframe = tk.Frame(centerContextFrame)
    filesframe.configure(background=APP_BACKGROUND_COLOR)
    filespagetitle = ctk.CTkLabel(
        filesframe,
        image=ctk.CTkImage(Image.open(os.getenv("EMOJI_FILE_PATH")), size=ICON_SIZE_L),
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
    permissionsframe = tk.Frame(centerContextFrame)
    permissionsframe.configure(background=APP_BACKGROUND_COLOR)
    permissionspagetitle = ctk.CTkLabel(
        permissionsframe,
        image=ctk.CTkImage(Image.open(os.getenv("EMOJI_PERMISSIONS_PATH")), size=ICON_SIZE_L),
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
    signatureframe = tk.Frame(centerContextFrame)
    signatureframe.configure(background=APP_BACKGROUND_COLOR)
    signaturepagetitle = ctk.CTkLabel(
        signatureframe,
        image=ctk.CTkImage(Image.open(os.getenv("EMOJI_SIGNATURE_PATH")), size=ICON_SIZE_L),
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
    steganographyframe = tk.Frame(centerContextFrame)
    steganographyframe.configure(background=APP_BACKGROUND_COLOR)
    steganographypagetitle = ctk.CTkLabel(
        steganographyframe,
        image=ctk.CTkImage(Image.open(os.getenv("EMOJI_STEGANOGRAPHY_PATH")), size=ICON_SIZE_L),
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
    identityframe = tk.Frame(centerContextFrame)
    identityframe.configure(background=APP_BACKGROUND_COLOR)
    identitypagetitle = ctk.CTkLabel(
        identityframe,
        image=ctk.CTkImage(Image.open(os.getenv("EMOJI_IDENTITY_PATH")), size=ICON_SIZE_L),
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
    cardsframe = tk.Frame(centerContextFrame)
    cardsframe.configure(background=APP_BACKGROUND_COLOR)
    cardspagetitle = ctk.CTkLabel(
        cardsframe,
        image=ctk.CTkImage(Image.open(os.getenv("EMOJI_CREDIT_CARD_PATH")), size=ICON_SIZE_L),
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
    def fetchandsendupdateddata(updateNameEntry, updateSurnameEntry, updateUsernameEntry, updatePasswordEntry):
        if updateNameEntry is None:
            updatedname = None
        else:
            updatedname = updateNameEntry.get()

        if updateSurnameEntry is None:
            updatedsurname = None
        else:
            updatedsurname = updateSurnameEntry.get()

        if updateUsernameEntry is None:
            updatedusername = None
        else:
            updatedusername = updateUsernameEntry.get()

        if updatePasswordEntry is None:
            updatedpassword = None
        else:
            updatedpassword = updatePasswordEntry.get()

        authenticator.updateuserinfo(updatedname, updatedsurname, updatedusername, updatedpassword, lockboxdbcontroller)

    for widget in centerContextFrame.winfo_children():
        widget.destroy()

    profileframe = tk.Frame(centerContextFrame)
    profileframe.configure(background=APP_BACKGROUND_COLOR)
    profileframe.pack(fill=tk.BOTH, expand=True)

    # Add title to the profile page
    profilepagetitle = ctk.CTkLabel(
        profileframe,
        text="Il mio profilo",
        font=FUTURA_FONT_L,
        text_color=TITLE_TEXT_COLOR,
        fg_color=APP_BACKGROUND_COLOR,
        bg_color=APP_BACKGROUND_COLOR
    )
    profilepagetitle.grid(row=0, column=0, columnspan=4, padx=30, pady=20, sticky="w")

    logoutButton = ctk.CTkButton(
        profileframe,
        text="Esci",
        text_color="white",
        font=FUTURA_FONT_S,
        corner_radius=15,
        width=100,
        height=40,
        fg_color="red",
        hover_color="#FF6347",
        border_width=0,
        command=lambda: logoutuser()
    )
    logoutButton.grid(row=0, column=3, padx=30, pady=20, sticky="e")

    descriptionframe = ctk.CTkFrame(profileframe, corner_radius=20, bg_color=APP_BACKGROUND_COLOR,
                                    fg_color="#F4F4F4", width=600, height=100)
    descriptionframe.grid(row=1, column=0, columnspan=4, padx=(20, 0), pady=(0, 20), sticky="w")
    description = ctk.CTkLabel(descriptionframe, text=MYPROFILE_DESCRIPTION, font=FUTURA_FONT_XS,
                               text_color="#C5C5C5", wraplength=600)
    description.pack(padx=20, pady=20)
    user_info = authenticator.get_authenticated_user_to_dict()

    def toggle_edit(entry_widget):
        if entry_widget.cget('state') == 'normal':
            entry_widget.configure(state='disabled', text_color="#B5B5B5")
            submitUpdatedInfoButton.configure(state="disabled", text_color="#E3E3E3", fg_color="#F4F4F4", hover_color=APP_SECONDARY_COLOR)
        else:
            entry_widget.configure(state='normal', text_color=TITLE_TEXT_COLOR)
            submitUpdatedInfoButton.configure(state="normal", text_color="white", fg_color="#FB62AC", hover_color="#F1328D")

    submitUpdatedInfoButton = ctk.CTkButton(
        profileframe,
        text="Salva",
        text_color="#E3E3E3",
        font=FUTURA_FONT_S,
        corner_radius=15,
        width=150,
        height=40,
        fg_color="#F4F4F4",
        hover_color=APP_SECONDARY_COLOR,
        border_width=0,
        state="disabled",
        command=lambda: fetchandsendupdateddata(
            nameEntry if nameEntry.cget('state') == 'normal' else None,
            surnameEntry if surnameEntry.cget('state') == 'normal' else None,
            usernameEntry if usernameEntry.cget('state') == 'normal' else None,
            passwordEntry if passwordEntry.cget('state') == 'normal' else None,
        ),
    )
    submitUpdatedInfoButton.grid(row=5, column=1, padx=(0, 10), pady=(30, 50))

    def create_entry_with_edit_button(row, column, text):
        entry_frame = tk.Frame(profileframe, bg=APP_BACKGROUND_COLOR)
        entry_frame.grid(row=row, column=column, padx=20, pady=10, sticky="w")

        entry = ctk.CTkEntry(
            entry_frame,
            font=FUTURA_FONT_M,
            width=200,
            height=40,
            corner_radius=10,
            fg_color="#E0E0E0",
            text_color="#B5B5B5",
            border_width=0,
        )
        entry.pack(side=tk.LEFT)
        entry.insert(0, text)
        entry.configure(state='disabled')

        edit_button = ctk.CTkButton(
            entry_frame,
            bg_color=APP_BACKGROUND_COLOR,
            fg_color=APP_BACKGROUND_COLOR,
            image=pencilImage,
            text="",
            width=20,
            height=20,
            hover_color=APP_BACKGROUND_COLOR,
            command=lambda: toggle_edit(entry)
        )
        edit_button.pack(side=tk.RIGHT, padx=5)

        return entry

    if user_info:
        nameEntry = create_entry_with_edit_button(2, 0, user_info['name'])
        surnameEntry = create_entry_with_edit_button(2, 1, user_info['surname'])
        usernameEntry = create_entry_with_edit_button(3, 0, user_info['username'])
        passwordEntry = create_entry_with_edit_button(3, 1, user_info['password'])

    else:
        no_user_label = ctk.CTkLabel(
            profileframe,
            text="[DEBUG] Logic error: No user info (user not authenticated).",
            font=FUTURA_FONT_M,
            text_color=APP_SECONDARY_COLOR,
            fg_color=APP_BACKGROUND_COLOR,
            bg_color=APP_BACKGROUND_COLOR
        )
        no_user_label.grid(row=2, column=0, columnspan=4, padx=30, pady=5, sticky="w")


def settingspage():
    settingsframe = tk.Frame(centerContextFrame)
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
    notificationhubframe = tk.Frame(centerContextFrame)
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


def destroymainframe():
    for frame in mainApp.winfo_children():
        frame.destroy()
        mainApp.update()


welcomepage()
lockboxdbcontroller = dbm.LockBoxDBManager()
mainApp.mainloop()
