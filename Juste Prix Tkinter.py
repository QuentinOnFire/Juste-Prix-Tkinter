import random
from tkinter import *

class Jeu(Tk):

    def __init__(self):
        super().__init__()
        self.prix = random.randint(1, 100)
        self.widget()
        self.nbessai = 0


    def widget(self):
        self.label1 = Label(self, text="Entrer un nombre entre 1 et 100", bg='#33E9FF', fg='black', font=("Arial", 20))
        self.label1.place(x=155, y=0)
        self.entry1 = Entry(self, font=("Arial", 20), fg='black', bg='#33E9FF', highlightthickness=1)
        self.entry1.place(x=210, y=40)
        self.button1 = Button(self, font=("Arial", 20), fg='black', bg='#33E9FF', text="Valider", command=self.juste_prix)
        self.button1.place(x=310, y=80)
        self.label2 = Label(self, text="", bg='#33E9FF', fg='black', font=("Arial", 20))
        self.label2.place(x=290, y=140)
        self.label3 = Label(self, text="", bg='#33E9FF', fg='black', font=("Arial", 20))
        self.label3.place(x=100, y=180)
        self.button2 = Button(self, text="Abandonner", bg='#33E9FF', fg='black', font=("Arial", 20), command=self.abandonner)
        self.button2.place(x=50, y=80)
        self.label4 = Label(self, text="", bg='#33E9FF', fg='black', font=("Arial", 20))
        self.label4.place(x=500, y=90)

    def juste_prix(self):
        prix_pense = self.entry1.get()
        self.nbessai += 1
        self.label4['text'] = "{} essai(s)".format(self.nbessai)
        self.label3['text'] = ""
        self.entry1.delete(0, END)
        if self.prix == int(prix_pense):
            self.label2['text'] = "Bravo, tu as trouvé le bon nombre qui etait {}".format(self.prix)
            self.label2.place(x=90, y=140)
            self.prix = random.randint(1, 100)
            self.label3['text'] = "On recommence, le nombre a changé !!!"
            self.nbessai = 0

        elif int(prix_pense) > self.prix:
            self.label2['text'] = "Plus petit !!!"
            self.label2.place(x=290, y=140)
        elif int(prix_pense) < self.prix:
            self.label2['text'] = "Plus grand !!!"
            self.label2.place(x=290, y=140)

    def abandonner(self):
        self.label2['text'] = "Le nombre était {}, on recommence !!!".format(self.prix)
        self.label2.place(x=110, y=140)
        self.prix = random.randint(1, 100)
        self.nbessai = 0

a = True
if a:
    fen = Jeu()
    fen.title("Jeu du juste prix")
    fen.geometry("720x250")
    fen.minsize(720, 250)
    fen.maxsize(720, 250)
    fen.config(bg='#33E9FF')
    fen.mainloop()