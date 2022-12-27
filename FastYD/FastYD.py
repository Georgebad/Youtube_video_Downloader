from tkinter import END

from pytube import YouTube
import tkinter
import tkinter.messagebox
import customtkinter
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
try:
    f = open("log.txt", "r+")
except IOError:
    f = open("log.txt", "w+")
destination = f.read()
f.close()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("FastYD")
        self.geometry(f"{800}x{400}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="FastYD",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Download Path",
                                                        command=self.open_input_dialog_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Youtube Video URL")

        self.entry.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        print(self.entry.get())
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2,
                                                     text="Download", text_color=("gray10", "#DCE4EE"),
                                                     command=self.download)
        self.main_button_1.grid(row=0, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=250)
        self.textbox.grid(row=2, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.textbox.insert("0.0",
                            "FastYD\n\n" + "Welcome to FastYD a cross-platform desktop application, \nto Download Youtube videos.\nThis App created because i was bored to search on the internet, \nabout websites that could make my life easier")

    def open_input_dialog_event(self):
        file = open("log.txt", "r+")
        destination_load = file.read()
        print(destination_load)
        dialog = customtkinter.CTkInputDialog(
            text=f"Current path is:\n{destination_load}\nSet Up the Download Path you want:", title="Path")
        destination = dialog.get_input()
        if destination:
            file.truncate(0)
            file.seek(0)
            file.write(destination)
            file.close()
        else:
            destination = destination_load

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def download(self, ):
        print(self.entry.get())
        print(destination)
        if (self.entry.get()):
            self.textbox.delete(index1="0.0", index2=END)
            self.textbox.insert(END, "Start Downloading..."),
            youtubeObject = YouTube(self.entry.get())
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            youtubeObject.download(output_path=destination)
            self.textbox.insert(END, "\n\nEverything is Ready!!"),


if __name__ == "__main__":
    app = App()
    app.mainloop()
