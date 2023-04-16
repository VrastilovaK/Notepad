# coding = UTF8
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Notepad")
        self.iconbitmap("Notepad.ico")
        self.geometry("800x600")


# mainloop
app = App()
app.mainloop()
