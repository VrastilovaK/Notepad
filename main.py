# coding = UTF8
import tkinter
import customtkinter
import json


class Menu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.new_note_button = customtkinter.CTkButton(self, text="New note", command=self.new_note)
        self.new_note_button.pack(side="left", padx=5, expand=True)

        self.new_note_window = None

        self.edit_note_button = customtkinter.CTkButton(self, text="Edit note", command=self.edit_note)
        self.edit_note_button.pack(side="left", padx=5, expand=True)

        self.edit_note_window = None

        self.delete_button = customtkinter.CTkButton(self, text="Delete note", command=self.delete_note)
        self.delete_button.pack(side="left", padx=5, expand=True)

        self.delete_all_button = customtkinter.CTkButton(self, text="Delete all", command=self.delete_all)
        self.delete_all_button.pack(side="left", padx=5, expand=True)

    def new_note(self):
        if self.new_note_window is None or not self.new_note_window.winfo_exists():
            self.new_note_window = NewNote(self)
            self.new_note_window.grab_set()
        else:
            self.new_note_window.focus()

    def edit_note(self):
        if self.edit_note_window is None or not self.edit_note_window.winfo_exists():
            self.edit_note_window = EditNote(self)
            self.edit_note_window.grab_set()
        else:
            self.edit_note_window.focus()

    @staticmethod
    def delete_note():
        note = app.note_view.get()
        app.note_view.delete(note)
        notes.pop(note)
        with open("notes.json", "w") as f:
            json.dump(notes, f)
        app.load_notes()

    @staticmethod
    def delete_all():
        notes.clear()
        with open("notes.json", "w") as f:
            json.dump(notes, f)
        app.load_notes()


class NoteView(customtkinter.CTkTabview):
    def __init__(self, master):
        super().__init__(master)
        self.configure(height=400)


class NewNote(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("400x370+250+250")
        self.title("New note")
        self.resizable(False, False)

        self.title_label = customtkinter.CTkLabel(self, text="Title: ")
        self.title_label.pack(pady=5)

        self.title = customtkinter.CTkEntry(self)
        self.title.pack(pady=5)

        self.content_label = customtkinter.CTkLabel(self, text="Content: ")
        self.content_label.pack(pady=5)

        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.configure(width=380)
        self.textbox.pack(pady=5, padx=10)

        self.save_button = customtkinter.CTkButton(self, text="Save", command=self.save_note)
        self.save_button.pack(pady=5)

    def save_note(self):
        title_save = self.title.get()
        content = self.textbox.get(0.0, tkinter.END)
        notes[title_save] = content.strip()

        with open("notes.json", "w") as f:
            json.dump(notes, f)

        app.load_notes()
        self.destroy()


class EditNote(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("400x370+250+250")
        self.title("Edit note")
        self.resizable(False, False)
        self.curent_note = app.note_view.get()
        self.curent_text = self.load_note()

        self.title_label = customtkinter.CTkLabel(self, text="Title:")
        self.title_label.pack(pady=5)

        self.title = customtkinter.CTkLabel(self, text=self.curent_note)
        self.title.pack(pady=5)

        self.content_label = customtkinter.CTkLabel(self, text="Content: ")
        self.content_label.pack(pady=5)

        self.textbox = customtkinter.CTkTextbox(self)
        self.textbox.configure(width=380)
        self.textbox.pack(pady=5, padx=10)
        self.textbox.insert("0.0", f"{self.curent_text}")

        self.save_button = customtkinter.CTkButton(self, text="Save", command=self.save_note)
        self.save_button.pack(pady=5)

    def load_note(self):
        with open("notes.json", "w") as f:
            json.dump(notes, f)
        note_text = notes.get(self.curent_note)
        return note_text

    def save_note(self):
        content = self.textbox.get(0.0, tkinter.END)
        notes[self.curent_note] = content.strip()

        with open("notes.json", "w") as f:
            json.dump(notes, f)

        app.load_notes()
        self.destroy()


class Footer(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(height=30)

        self.label = customtkinter.CTkLabel(self, text="Notepad by Tewe")
        self.label.pack(side="right", padx=10)


class App(customtkinter.CTk):
    def __init__(self, ):
        super().__init__()
        self.title("Notepad")
        self.width = 700
        self.height = 550
        self.geometry(f"{self.width}x{self.height}+100+100")
        self.resizable(False, False)

        self.menu = Menu(master=self)
        self.menu.pack(fill="x", pady=15, padx=5)

        self.note_view = NoteView(master=self)
        self.note_view.pack(padx=20, pady=(0, 20), fill="y", expand=True)

        self.footer = Footer(master=self)
        self.footer.pack(side="bottom", fill="x")

    def load_notes(self):
        try:
            with open("notes.json", "r") as f:
                load_notes = json.load(f)

            self.note_view.destroy()
            self.note_view = NoteView(master=self)
            self.note_view.pack(padx=20, pady=(0, 20), fill="both", expand=True)

            for title, content in load_notes.items():
                try:
                    self.note_view.add(title)
                    self.note_view.label = customtkinter.CTkLabel(master=self.note_view.tab(title), text=content, justify="left")
                    self.note_view.label.pack(pady=15)

                except ValueError:
                    self.note_view.label = customtkinter.CTkLabel(master=self.note_view.tab(title), text=content, justify="left")
                    self.note_view.label.pack(pady=15)

        except FileNotFoundError:
            pass


# mainloop
notes = {}
try:
    with open("notes.json", "r") as file:
        notes = json.load(file)

except FileNotFoundError:
    pass

app = App()
app.load_notes()

app.mainloop()
