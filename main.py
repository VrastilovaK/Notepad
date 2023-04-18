# coding = UTF8
import customtkinter
import time


# function for timing
def time_setting():
    string = time.strftime('%a, %d %b %Y %H:%M:%S')
    label_time.configure(text=string)
    label_time.after(1000, time_setting)


# new note
class NewNote(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("400x280+250+250")
        self.title("New note")
        self.resizable(False, False)

        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.configure(width=380)
        self.textbox.grid(padx=10, pady=10)

        self.save_button = customtkinter.CTkButton(self, text="Save", command=self.save_note)
        self.save_button.grid(pady=10)

    def save_note(self):
        print("save")


# menu with buttons
class Menu(customtkinter.CTkFrame):
    def __init__(self, master, width):
        super().__init__(master, width)
        self.master_width = width
        self.configure(width=self.master_width, height=50)

        self.new_note_button = customtkinter.CTkButton(self, text="New", command=self.new_note)
        self.new_note_button.grid(row=0, column=0)

        self.new_note_window = None

    def new_note(self):
        if self.new_note_window is None or not self.new_note_window.winfo_exists():
            self.new_note_window = NewNote(self)
            self.new_note_window.grab_set()
        else:
            self.new_note_window.focus()


# frame for saved notes
class MainFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, width):
        super().__init__(master, width)
        self.master_width = width
        self.configure(width=self.master_width - 35, height=470)

        # notes
        self.textbox = customtkinter.CTkLabel(self, text="test")
        self.textbox.grid(row=0)

        self.textbox_2 = customtkinter.CTkLabel(self, text="test2")
        self.textbox_2.grid(row=1)


# footer with date and time
class Footer(customtkinter.CTkFrame):
    def __init__(self, master, width):
        super().__init__(master, width)
        self.master_width = width
        self.configure(width=self.master_width, height=30)

        self.label = customtkinter.CTkLabel(self, text="Notepad by Tewe")
        self.label.grid(row=0, column=0, padx=(30, 100))


# app
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Notepad")
        self.width = 800
        self.height = 600
        self.geometry(f"{self.width}x{self.height}+100+100")
        self.resizable(False, False)
        self.timing = time

        self.menu = Menu(master=self, width=self.width)
        self.menu.grid(row=0, column=0, pady=15, padx=5)

        self.main_frame = MainFrame(master=self, width=self.width)
        self.main_frame.grid(row=1, column=0, padx=5)

        self.footer = Footer(master=self, width=self.width)
        self.footer.grid(row=2, column=0, padx=5, pady=15)


# mainloop
app = App()

label_time = customtkinter.CTkLabel(app.footer)
label_time.grid(row=0, column=1, padx=(0, 15))
time_setting()

app.mainloop()
