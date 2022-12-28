#########################
#  Application Calcul-Energie
# 
# v0.3 - Nouvelle fenetre de menu
# William P
# 29/11/2022
########################

from cProfile import label
from multiprocessing.sharedctypes import Value
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.tix import LabelEntry
from urllib import request
import sqlite3
import os
from datetime import date
from tkcalendar import DateEntry

### INSTANCIATION ET VARIABLES
fen_princ = Tk()
fen_princ.geometry("640x350")
fen_princ.title("Calcul Consommation")
databasefile = "test_bddenergie.db"
vc1 = StringVar()

### FIN INSTANCIATION ET VARIABLES

### FONCTION ## 
def databaseconnection(databasefile):
    print("En cours d'implémentation")
    resultfile = os.path.exists(databasefile)
    if resultfile == 'False':
        print(resultfile,"Base de données introuvable")
    else:
        print(resultfile, "Base de données existante")
        conn = sqlite3.connect(databasefile)
        return True

def databaseinsert():
    conn = sqlite3.connect(databasefile)
    sql = ''' INSERT INTO RELEVE(date_releve,valeur_releve,type_energie,nom_energie)
              VALUES(?,?,?,? ) '''
    #sql = ''' INSERT INTO essaies(col1)
    #          VALUES(?) '''
    cur = conn.cursor()
    argsinsertvalue = (buttondate.get_date(),entryvalue.get(),vc1.get(),energieslistoptionvar.get() )
    cur.execute(sql,argsinsertvalue)
    conn.commit()
    conn.close()


def databasemodify():
    print("Non implémentée")

def databasedelete():
    print("Non implémentée")

def addmettereading():
    #Cette fonction permet d ajouter la valeur d un compteur
    
    try:
        conn = sqlite3.connect(databasefile)
    except Error as e:
        print(e)
    sql = conn.execute('''Select * from COMPTEUR''');
    rows = sql.fetchall()
    print('contenu de la variable:',rows)
    
    for row in rows:
        print(row)
        tree.insert('', 0, 'gallery', text='Applications')

    conn.commit()
    sql.close()
    conn.close()    



def operationrprint():
    conn = sqlite3.connect(databasefile)
    sql = ''' SELECT * FROM RELEVE'''
    cur = conn.cursor()
    argsselectvalue = (buttondate.get_date(),entryvalue.get(),vc1.get(),energieslistoptionvar.get() )
    cur.execute(sql,argsselectvalue)
    conn.commit()
    conn.close()



def sayhello():
    print(vc1.get())

def file_new():
    framelocation.pack(fill="both", expand=1)
    print("fonction file_new appelée")

def menulocation():
    print("menu location")

def menumetter():
    print("menu metter")
    
def menusupplyer():
    print("menu supplyer")

def menuparameter():
    print("menu parameter")

def menuabout():
    print("menu about")

def getenergieslist():
    conn = sqlite3.connect(databasefile)
    sql = ''' Select nom_energie FROM energie'''
    cur = conn.cursor()
    cur.execute(sql)
    energiesdictionnary = []
    for row in cur.fetchall():
        energiesdictionnary.append(row[0] )
    conn.close()
    return energiesdictionnary

def windowmetter():
    newwindow = Toplevel(fen_princ)
    newwindow.title=("Gérer compteur")
    newwindow.geometry("800x300")
    metterlabel = Label(newwindow,text = "Créer un compteur d'énergie")
    metterNamelabel = Label(newwindow,text = "Nom compteur: ")
    metterCommentlabel = Label(newwindow,text = "Description compteur: ")
     
    mettercreateubtton = Button(newwindow, text = "Créer",command = addmettereading)
    mettermanagerquitbutton = Button(newwindow, text = "Exit",command = newwindow.destroy)
    metterNameEntry = Entry(newwindow,textvariable='mettername', width=50)
    metterCommentEntry = Entry(newwindow,textvariable='mettername', width=50)

    # Affichage des widget de la fenêtre windowsmetter (paramétrage des compteurs d'énergie)    
    metterlabel.grid(column=0, row= 0)
    metterNamelabel.grid(column=0,row=1)
    metterNameEntry.grid(column=1, row= 1)
    metterCommentlabel.grid(column=0, row= 2)
    metterCommentEntry.grid(column=1, row= 2)
    mettercreateubtton.grid(column=0, row= 6)
    mettermanagerquitbutton.grid(column=1, row= 7)
    
    tree = ttk.Treeview(newwindow, column=("Num","Commentaire","Nom"), show='headings',selectmode ='browse')
    tree.column("#1", anchor=tk.CENTER)
    tree.heading("#1", text="Num")
    tree.column("#2", anchor=tk.CENTER)
    tree.heading("#2", text="Nom")
    tree.column("#3", anchor=tk.CENTER)
    tree.heading("#3", text="Commentaire")
    
    conn = sqlite3.connect(databasefile)
    sql = conn.execute("SELECT * FROM COMPTEUR");
    rows = sql.fetchall()

    for row in rows:
        print(row)
        tree.insert("",'end',values=(row[0],row[1],row[2]))

    sql.close()
    conn.close()    
    tree.grid(column=0, row=10)
    newwindow.mainloop()

### FIN Fonction ## 



## LES MENUS    
menuFichier = Menubutton(fen_princ, text = "Fichier", relief = "ridge")
menuFichier.menu = Menu(menuFichier)  
menuFichier["menu"]=menuFichier.menu    
menuFichier.menu.add_checkbutton(label = "Importer fichier CSV", variable=IntVar())  
menuFichier.menu.add_checkbutton(label = "Enregistrer", variable=IntVar())  
menuFichier.menu.add_checkbutton(label = "Quitter", variable=IntVar())  
menuFichier.menu = Menu(menuFichier)  
menuAction = Menubutton(fen_princ, text = "Action", relief = "ridge")


# MENU BARRE
menuBarre=Menu(fen_princ)
menuFichier = Menu(menuBarre, tearoff= 0)
menuEdition = Menu(menuBarre, tearoff= 0)
menuParameter = Menu(menuBarre, tearoff= 0)
menuParameter.add_cascade(label="fournisseur")
menuParameter.add_cascade(label="compteur", command=windowmetter )
menuParameter.add_cascade(label="contrat")
menuApropos = Menu(menuBarre, tearoff= 0)
#Ajout menu principaux
menuBarre.add_cascade(label="Fichier", menu= menuFichier)
menuBarre.add_cascade(label="Edition",menu = menuEdition)
menuBarre.add_cascade(label="Paramètre",menu = menuParameter)
menuBarre.add_cascade(label="A propos",menu = menuApropos)

# Ajout de commande au menu principal
menuFichier.add_command(label="Ouvrir", command=file_new)
menuFichier.add_command(label="Quitter", command= quit)


#menuEdition.add_command(label="Compteur")
#menuEdition.add_command(label="Fournisseur")
#menuEdition.add_command(label="Résidence")

menuApropos.add_command(label="about ")
menuApropos.add_command(label="?")
## FIN LES MENUS    




textmessage = StringVar()
monAffichage = Label(fen_princ, textvariable = textmessage)
monAffichage.place(x = 50, y = 100)

## CREATION DE FRAME
framelocation = Frame(fen_princ, width=400, height=400)
framemetter = Frame(fen_princ, width=400, height=400)
framesupplyer = Frame(fen_princ, width=400, height=400)
frameparameter = Frame(fen_princ, width=400, height=400)
## FIN CREATION DE FRAME

## GRILLE
labelpanel1 = Label(fen_princ, text=" Menu: Saisir une relève compteur")
labelernergy = Label(fen_princ, text="Saisir une relève de compteur")
entryvalue = Entry(fen_princ )
buttonadd = Button(fen_princ, text ="Ajouter", command=databaseinsert)
buttondate = DateEntry(fen_princ, text = "Sélectionner date")
buttonproduction = Radiobutton(fen_princ, text="Production", value="Production",command=sayhello, variable= vc1)
buttonconsommation = Radiobutton(fen_princ, text="Consommation", value="Consommation", command=sayhello,variable= vc1)
energiesdictionnary = getenergieslist()

energieslistoptionvar = StringVar()
energieslistoptionvar.set(energiesdictionnary[0])
energieslistoption = OptionMenu(fen_princ,energieslistoptionvar,*energiesdictionnary )

labelpanel1.grid(column=0, row=0, pady=5)
labelernergy.grid(column=0, row=2)
entryvalue.grid(column=0, row= 3)
buttonadd.grid(column=5, row=6, pady=5)
buttonproduction.grid(column=4, row=1)
buttonconsommation.grid(column=5, row=1)
energieslistoption.grid(column=6, row= 5)
buttondate.grid(column=0, row = 1)


#print(buttondate.get_date())
## FIN de GRILLE




## Affichage des fenêtre et objets
#menuAction.pack()
#monAffichage.pack()
## FIN AFFICHAGE

## Pour que la fenetre reste ouverte durant fonctionnement
fen_princ.config(menu=menuBarre)
fen_princ.mainloop()

