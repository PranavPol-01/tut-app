import tkinter as tk

class Sidebar(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, bg="#343a40", width=250, **kwargs)
        self.buttons = []

    def add_button(self, text, command):
        button = tk.Button(self, text=text, command=command, bg="#343a40", fg="white", activebackground="#343a40", activeforeground="white", bd=0, padx=10, pady=5, anchor="w", cursor="hand2")
        button.pack(fill=tk.X)
        self.buttons.append(button)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x600")
        self.title("Sidebar Example")
        
        self.sidebar_visible = False

        self.sidebar_button = tk.Button(self, text="Show Sidebar", command=self.toggle_sidebar, bg="#343a40", fg="white", activebackground="#343a40", activeforeground="white", bd=0, padx=10, pady=5, cursor="hand2")
        self.sidebar_button.pack(anchor="nw", padx=10, pady=10)

        self.sidebar = Sidebar(self)
        self.sidebar.add_button("Goal Tracking", lambda: print("Option 1 clicked"))
        self.sidebar.add_button("Test your knowledge", lambda: print("Option 2 clicked"))
        self.sidebar.add_button("Explore", lambda: print("Option 3 clicked"))

    def toggle_sidebar(self):
        if self.sidebar_visible:
            self.sidebar.place_forget()
            self.sidebar_button.config(text="Show Sidebar")
            self.sidebar_visible = False
        else:
            self.sidebar.place(relx=0, rely=0.1, relwidth=0.2, relheight=0.9)
            self.sidebar_button.config(text="Hide Sidebar")
            self.sidebar_visible = True

if __name__ == "__main__":
    app = App()
    app.mainloop()
