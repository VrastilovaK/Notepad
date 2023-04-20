# coding = UTF8
import tkinter
import customtkinter
import time
import json


# function for timing
def time_setting():
    string = time.strftime('%a, %d %b %Y %H:%M:%S')
    label_time.configure(text=string)
    label_time.after(1000, time_setting)


# save notes
def save_note(title, text):
    title_save = title.get()
    content = text.get("0.0", tkinter.END)
    notes[title_save] = content.strip()

    with open("notes.json", "w") as file:
        json.dump(notes, file)

    load_notes()


def load_notes():
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)

        for title, content in notes.items():
            try:
                app.note_view.add(f"{title}")
                app.note_view.label = customtkinter.CTkLabel(master=app.note_view.tab(f"{title}"), text=content)
                app.note_view.label.grid(row=0, column=0, padx=20, pady=10)

            except ValueError:
                pass

    except FileNotFoundError:
        pass


# new note
class NewNote(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("400x340+250+250")
        self.title("New note")
        self.resizable(False, False)

        self.title_label = customtkinter.CTkLabel(self, text="Title: ")
        self.title_label.grid(row=0, column=0, pady=10)

        self.title = customtkinter.CTkEntry(self)
        self.title.grid(row=0, column=1, pady=10)

        self.content_label = customtkinter.CTkLabel(self, text="Content: ")
        self.content_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))

        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.configure(width=380)
        self.textbox.grid(row=2, column=0, columnspan=2, pady=(0, 10), padx=10)

        self.save_button = customtkinter.CTkButton(self, text="Save", command=self.save)
        self.save_button.grid(row=3, column=0, columnspan=2, pady=(0, 10))

    def save(self):
        save_note(self.title, self.textbox)
        self.destroy()


# menu with buttons
class Menu(customtkinter.CTkFrame):
    def __init__(self, master, width):
        super().__init__(master, width)
        self.master_width = width
        self.configure(width=self.master_width, height=50)

        self.new_note_button = customtkinter.CTkButton(self, text="New note", command=self.new_note)
        self.new_note_button.grid(row=0, column=0)

        self.new_note_window = None

        self.edit_note_button = customtkinter.CTkButton(self, text="Edit note")
        self.edit_note_button.grid(row=0, column=1, padx=(5, 0))

        self.edit_note_window = None

        self.delete_button = customtkinter.CTkButton(self, text="Delete note")
        self.delete_button.grid(row=0, column=2, padx=5)

        self.delete_all_button = customtkinter.CTkButton(self, text="Delete all")
        self.delete_all_button.grid(row=0, column=3)

    def new_note(self):
        if self.new_note_window is None or not self.new_note_window.winfo_exists():
            self.new_note_window = NewNote(self)
            self.new_note_window.grab_set()
        else:
            self.new_note_window.focus()

    def edit_note(self):
        pass


# frame for saved notes
class NoteView(customtkinter.CTkTabview):
    def __init__(self, master, width):
        super().__init__(master, width)
        self.master_width = width
        self.configure(width=self.master_width - 10, height=400)


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
        self.height = 515
        self.geometry(f"{self.width}x{self.height}+100+100")
        self.resizable(False, False)
        self.timing = time

        self.menu = Menu(master=self, width=self.width)
        self.menu.grid(row=0, column=0, pady=15, padx=5)

        self.note_view = NoteView(master=self, width=self.width)
        self.note_view.grid(row=1, column=0, columnspan=15, padx=5)

        self.footer = Footer(master=self, width=self.width)
        self.footer.place(y=self.height - 40, x=400)


# mainloop
notes = {}
app = App()

label_time = customtkinter.CTkLabel(app.footer)
label_time.grid(row=0, column=1, padx=(0, 15))
time_setting()

try:
    with open("notes.json", "r") as file:
        notes = json.load(file)

except FileNotFoundError:
    pass

load_notes()
app.mainloop()
