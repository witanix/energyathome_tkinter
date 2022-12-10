#########################
#  Application Calcul-Energie
# 
# v0.1 - partie Graphique
# William P
# 29/11/2022
########################

from cProfile import label
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter.tix import LabelEntry
from urllib import request
import sqlite3
import os
from datetime import date
from tkcalendar import Calendar, DateEntry

### INSTANCIATION ET VARIABLES
fen_princ = Tk()
fen_princ.geometry("640x350")  
fen_princ.title("Essaie app GUI")
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
    " Cette fonction permet d'ajouter la valeur d'un compteur"

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
menuApropos = Menu(menuBarre, tearoff= 0)
#Ajout menu principaux
menuBarre.add_cascade(label="Fichier", menu= menuFichier)
menuBarre.add_cascade(label="Edition",menu = menuEdition)
menuBarre.add_cascade(label="Paramètre",menu = menuParameter)
menuBarre.add_cascade(label="A propos",menu = menuApropos)

# Ajout de commande au menu principal
menuFichier.add_command(label="Ouvrir", command=file_new)
menuFichier.add_command(label="Quitter", command= quit)

menuEdition.add_command(label="Compteur")
menuEdition.add_command(label="Fournisseur")
menuEdition.add_command(label="Résidence")

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

