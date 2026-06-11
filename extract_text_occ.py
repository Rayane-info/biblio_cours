import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd
import tkinter.simpledialog as sd
from collections import Counter
import re

class ExtractApp: 
    def __init__(self, root):
        self.root = root
        self.root.title("Compteur d'occurences - Projet Python")
        self.root.geometry("1280x720")

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.menu = ttk.Frame(root, padding=10)
        self.menu.grid(row=0, column=0, sticky="nsew")

        self.menu.grid_rowconfigure(1, weight=1)
        self.menu.grid_columnconfigure(0, weight=1)

        ttk.Label(self.menu, text="Bienvenue dans l'extracteur de mots les plus utilisés").grid(row=0, column=0, pady=10)
        ttk.Button(self.menu, text="Afficher le contenu d'un fichier(txt)", command=self.read_file).grid(row=1, column=0, pady=10)
        ttk.Button(self.menu, text="Afficher les mots les plus communs", command=self.read_occ_file).grid(row=2, column=0 , pady=10)
        ttk.Button(self.menu, text="Quitter l'application", command=root.destroy).grid(row=0, column=2, pady=10)
        
        self.text_zone = tk.Text(self.menu, wrap=tk.WORD)
        self.text_zone.grid(row=3, column=0, sticky="nsew", pady=10)
    
    def read_file(self):
        # Lit fichier et affiche son texte dans la zone de texte
        file=fd.askopenfile(title="Selectionner un fichier texte",mode='r',filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
        if file:
            texte=file.read()
            file.close()
            self.text_zone.delete(1.0,tk.END)
            self.text_zone.insert(tk.END,texte)
        else:
            self.text_zone.delete(1.0,tk.END)
            self.text_zone.insert(tk.END,"Aucun fichier selectionné")
            
    def read_occ_file(self):
        # Lit fichier, compte les mots et affiche ceux dépassant un seuil
        file = fd.askopenfile(mode='r', filetypes=[("Texte", "*.txt")])
        if not file: return
        t = file.read().lower()
        file.close()
        mots = re.findall(r"[a-zàâçéèêëîïôûùüÿæœ]+(?:['-][a-zàâçéèêëîïôûùüÿæœ]+)?", t)
        c = Counter(mots)
        seuil = sd.askinteger("Seuil", "Afficher les mots apparaissant plus de combien de fois ?", minvalue=0)
        if not seuil: return
        res = [(m, n) for m, n in c.items() if n > seuil]
        res.sort(key=lambda x: x[1], reverse=True)
        aff = "\n".join(f"{m} : {n}" for m, n in res) or f"Aucun mot > {seuil}"
        self.text_zone.delete(1.0, "end")
        self.text_zone.insert("end", aff)

root = tk.Tk()
app = ExtractApp(root)
root.mainloop()
