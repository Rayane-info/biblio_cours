from tkinter import Tk
from tkinter import ttk

root = Tk()
root.title("Mon projet")
root.geometry("1280x720")

menu = ttk.Frame(root,padding=10)
clickl2= ttk.Frame(root,padding=10)

menu.grid(row=0,column= 0, sticky="nsew")
clickl2.grid(row=0,column= 0, sticky="nsew")

#region Création des fonctions

def on_click_l2():
    clickl2.tkraise()

def retour_menu():
    menu.tkraise()
#endregion 

ttk.Label(menu,text="Veuillez choisir votre année!").grid(column=0,row=0)
#region Création des boutons du menu

ttk.Button(menu,text="L1").grid(column=0,row=1)
ttk.Button(menu,text="L2 mono Informatique", command= on_click_l2).grid(column=0,row=2)
ttk.Button(menu,text="L3 mono Informatique").grid(column=0,row=3)
ttk.Button(menu,text="Fermer l'application!", command=root.destroy).grid(column=4,row=4)
#endregion

ttk.Label(clickl2,text="Bienvenue en L2 mono Informatique, veuillez sélectionner la matière que vous voulez réviser !").grid(column=0,row=0)
#region Création des boutons de la frame l2
ttk.Button(clickl2,text="Algorithmique (6 ECTS - Bloc Majeur)").grid(column = 0, row =1)
ttk.Button(clickl2,text="Maths Discrètes (6 ECTS - Bloc Majeur)").grid(column = 0, row = 2)
ttk.Button(clickl2,text="Sciences des données (6 ECTS - Bloc Majeur)").grid(column = 0, row = 3)
ttk.Button(clickl2,text="Bases de données relationnelles (6 ECTS - Bloc Majeur)").grid(column = 0, row = 4)
ttk.Button(clickl2,text="Java (6 ECTS - Bloc Majeur)").grid(column = 0, row = 5)
ttk.Button(clickl2,text="Logique (6 ECTS - Bloc Majeur)").grid(column = 0, row = 6)
ttk.Button(clickl2,text="Anglais (3 ECTS - Bloc Mineur)").grid(column = 0, row = 7)
ttk.Button(clickl2,text="Revenir au menu", command= retour_menu).grid(column=2,row=8)
#endregion
menu.tkraise()

root.mainloop()









#Toutes les fonctions
