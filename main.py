from tkinter import Tk
from tkinter import ttk

root = Tk()
root.title("Mon projet")
root.geometry("1280x720")

menu = ttk.Frame(root,padding=10)
l1= ttk.Frame(root,padding=10)
l2= ttk.Frame(root,padding=10)
l3= ttk.Frame(root,padding=10)

l2_algo = ttk.Frame(root,padding=10)
l2_maths_discretes = ttk.Frame(root,padding=10)
l2_bases_de_donnees = ttk.Frame(root,padding=10)
l2_structure_des_donnees = ttk.Frame(root,padding=10)
l2_java = ttk.Frame(root,padding=10)
l2_logique = ttk.Frame(root,padding=10)
l2_anglais = ttk.Frame(root,padding=10)

menu.grid(row=0,column= 0, sticky="nsew")
l1.grid(row=0,column= 0, sticky="nsew")
l2.grid(row=0,column= 0, sticky="nsew")
l3.grid(row=0,column= 0, sticky="nsew")

l2_algo.grid(row=0,column= 0, sticky="nsew")
l2_maths_discretes.grid(row=0,column= 0, sticky="nsew")
l2_bases_de_donnees.grid(row=0,column= 0, sticky="nsew")
l2_structure_des_donnees.grid(row=0,column= 0, sticky="nsew")
l2_java.grid(row=0,column= 0, sticky="nsew")
l2_logique.grid(row=0,column= 0, sticky="nsew")
l2_anglais.grid(row=0,column= 0, sticky="nsew")

#region Création des fonctions

def on_click_l1():
    l1.tkraise()

def on_click_l2():
    l2.tkraise()

#region fonctions l2

#region fonctions l2_algo
def on_click_algo():
    l2_algo.tkraise()



def on_click_maths_discretes():
    l2_maths_discretes.tkraise()

def on_click_structure_des_donnees():
    l2_structure_des_donnees.tkraise()

#region fonctions l2_bases_de_donnees
def on_click_bases_de_donnees():
    l2_bases_de_donnees.tkraise()

def on_click_bdd_cours():
    l2_bases_de_donnees_cours.tkraise()

def on_click_bdd_td():
    l2_bases_de_donnees_td.tkraise()

def on_click_bdd_tp():
    l2_bases_de_donnees_tp.tkraise()

def on_click_bdd_barème():
    l2_bases_de_donnees_barème.tkraise()

#endregion
def on_click_java():
    l2_java.tkraise()

def on_click_logique():
    l2_logique.tkraise()

def on_click_anglais():
    l2_anglais.tkraise()
#endregion

def on_click_l3():
    l3.tkraise()

def retour_menu():
    menu.tkraise()

def retour_l2():
    l2.tkraise()


#endregion 

#region Création des boutons/labels du menu
ttk.Label(menu,text="Veuillez choisir votre année!").grid(column=0,row=0)
ttk.Button(menu,text="L1", command = on_click_l1).grid(column=0,row=1)
ttk.Button(menu,text="L2 mono Informatique", command= on_click_l2).grid(column=0,row=2)
ttk.Button(menu,text="L3 mono Informatique", command= on_click_l3).grid(column=0,row=3)
ttk.Button(menu,text="Fermer l'application!", command=root.destroy).grid(column=4,row=4)
#endregion

#region Création des boutons/labels de la frame l1
ttk.Label(l1,text="Voici les matières de L1 mono Informatique! (à remplir plus tard)").grid(column=0,row=0)
ttk.Button(l1,text="Revenir au menu", command= retour_menu).grid(column=2,row=8)
#endregion

#region Création des boutons/labels de la frame l2
ttk.Label(l2,text="Voici les matières de L2 mono Informatique!").grid(column=0,row=0)
ttk.Button(l2,text="Algorithmique (6 ECTS - Bloc Majeur)", command = on_click_algo).grid(column = 0, row =1)
ttk.Button(l2,text="Maths Discrètes (6 ECTS - Bloc Majeur)", command = on_click_maths_discretes).grid(column = 0, row = 2)
ttk.Button(l2,text="Structure des données (6 ECTS - Bloc Majeur)", command = on_click_structure_des_donnees).grid(column = 0, row = 3)
ttk.Button(l2,text="Bases de données relationnelles (6 ECTS - Bloc Majeur)", command = on_click_bases_de_donnees).grid(column = 0, row = 4)
ttk.Button(l2,text="Java (6 ECTS - Bloc Majeur)", command = on_click_java).grid(column = 0, row = 5)
ttk.Button(l2,text="Logique (6 ECTS - Bloc Majeur)", command = on_click_logique).grid(column = 0, row = 6)
ttk.Button(l2,text="Anglais (3 ECTS - Bloc Mineur)", command = on_click_anglais).grid(column = 0, row = 7)
ttk.Button(l2,text="Revenir au menu", command= retour_menu).grid(column=2,row=8)
#endregion

#region Création des boutons/labels de l2_bases_de_donnees
ttk.Label(l2_bases_de_donnees,text="Voici les matières de L2 mono Informatique!").grid(column=0,row=0)
ttk.Button(l2_bases_de_donnees,text="Cours", command = on_click_bdd_cours).grid(column = 0, row = 2)
ttk.Button(l2_bases_de_donnees,text="TD", command = on_click_bdd_td).grid(column = 0, row = 3)
ttk.Button(l2_bases_de_donnees,text="TP", command = on_click_bdd_tp).grid(column=2,row=8)
ttk.Button(l2_bases_de_donnees,text="Barème", command = on_click_bdd_barème).grid(column=2,row=9)
ttk.Button(l2_bases_de_donnees,text="Revenir en arrière", command = retour_l2).grid(column=2,row=9)
#endregion

#region Création des boutons/labels de la frame l3
ttk.Label(l3,text="Voici toutes les matières de L3 mono Informatique! (à remplir plus tard)").grid(column=0,row=0)
ttk.Button(l3,text="Revenir au menu", command= retour_menu).grid(column=2,row=8)
#endregion

menu.tkraise()

root.mainloop()









#Toutes les fonctions
