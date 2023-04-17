# coding = UTF8
import customtkinter
import time


def time_setting():
    string = time.strftime('%a, %d %b %Y %H:%M:%S')
    label_time.configure(text=string)
    label_time.after(1000, time_setting)


class Footer(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(width=800, height=30)

        self.label = customtkinter.CTkLabel(self, text="Notepad by Tewe")
        self.label.grid(row=0, column=0, padx=(20, 480))
<<<<<<< HEAD
=======

        # self.time_string = time.strftime("%a, %d %b %Y %H:%M:%S")
        # self.label_time = customtkinter.CTkLabel(self, text=f"{self.time_string}")
        # self.label_time.grid(row=0, column=1, padx=20)

        # self.time_string = 0
        # self.label_time = customtkinter.CTkLabel(self, text=f"{self.time_string}")
        # self.label_time.grid(row=0, column=1, padx=20)
>>>>>>> main


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Notepad")
        self.iconbitmap("Notepad.ico")
        self.width = 800
        self.height = 600
        self.geometry(f"{self.width}x{self.height}")
        self.timing = time

        self.footer = Footer(master=self)
        self.footer.pack(side="bottom", pady=5)


# mainloop
app = App()

label_time = customtkinter.CTkLabel(app.footer)
label_time.grid(row=0, column=1, padx=20)
time_setting()

app.mainloop()
