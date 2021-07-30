import tkinter as tk


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widget()

    def create_widget(self):
        text = tk.Label(self, text="DEV EN COURS")
        text.pack(pady=50)

        bouton = tk.Button(self, text="Dis Bonjour", command=self.hello_world, padx=10, pady=10)
        bouton.pack()
        pass

    def hello_world(self):
        print("Hello World !")

if __name__ == "__main__":
    root = tk.Tk()
    main = App(master=root)

    main.master.title("Messenger Statistics")
    main.master.minsize(640, 400)

    menubar = tk.Menu(main)
    main.master.config(menu=menubar)

    menufichier = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Fichier", menu=menufichier)
    menufichier.add_command(label="Ouvrir")
    menufichier.add_command(label="Fermer")

    menuaffichage = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Affichage", menu=menuaffichage)
    menuaffichage.add_command(label="Grille")
    menuaffichage.add_command(label="Rows")
    menuaffichage.add_command(label="Cols")

    menustats = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Stats", menu=menustats)
    sousmenucascade = tk.Menu(menustats, tearoff=0)
    menustats.add_cascade(label="Messages", menu=sousmenucascade)
    sousmenucascade.add_command(label="Nombre de messages")
    sousmenucascade.add_command(label="Messages supprimés")
    menustats.add_command(label="Emojis")
    menustats.add_command(label="Mots")

    main.mainloop()
