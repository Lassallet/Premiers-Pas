'Import de toutes les fonctions Tkinter'
from tkinter import *

'Commande Result'
def Result():
    'Récupération des saisies'
    JJ = int(strj.get())
    MM = int(strm.get())
    AA = stra.get()

    if MM < 11 and int(AA) <= 1582 or int(AA) < 1582 or int(AA) > 2199 or MM < 1 or MM > 12:
        erreur = Tk()
        erreur.geometry("230x130")
        erreur.resizable(width=False, height=False)
        erreur.title("Erreur")
        lblErreur= Label(erreur, text='Saisir une date comprise entre\n\nle 1/11/1582 et le 12/12/2199.')
        lblErreur.place(x=30, y=15)
        btnErreur = Button(erreur, text='Ok', command=erreur.quit)
        btnErreur.place(x=100, y=80)
        erreur.mainloop()

    'Consiqnes de l''exercices'
    '1.On garde les deux derniers chiffres de l''année en question'
    AA1 = AA[2:4]

    '2.On ajoute 1/4 de ce chiffre en ignorant les restes'
    AA1 = int(AA1)
    date = (AA1 + AA1//4)

    '3.On ajoute la journée du mois'
    date = date + JJ

    '4.Selon le mois on ajoute'
    if 2 <= MM <= 3 or MM == 11: date = date + 3
    elif MM == 4 or MM == 7: date = date + 6
    elif MM == 9 or MM == 12: date = date + 5
    elif MM == 5: date = date + 1
    elif MM == 6: date = date + 4
    elif MM == 8: date = date + 2
    else: date = date + 0

    '5.Si l''année est bissextile et le mois est janvier ou février, on ôte 1'
    if int(AA)%400==0 or (int(AA)%4==0 and int(AA)%100!=0) and MM == 1 or MM == 2:
        date = date - 1

    '6.Selon le siècle, on ajoute'
    AA2 = AA[0:2]
    AA2 = int(AA2)
    if AA2 == 16 or AA2 == 20: date = date + 6
    elif AA2 == 17 or AA2 == 21: date = date + 4
    elif AA2 == 18: date = date + 2

    '7.On divise la somme par 7 et on garde le reste'
    date = date % 7

    '8.Le reste représente le jour de la semaine recherché'
    semaine = ['Dimanche', 'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi']
    i = 0
    for i, jr in enumerate(semaine):
        if date == i: Rdate.set(jr)

    #dateR = JJ, '/', MM, '/', AA


'Configuration de la fenêtre'
fnt = Tk()
fnt.geometry("400x300")
fnt.resizable(width=False, height=False)
fnt.title("Jour de la semaine")

'Les différents textes affichés dans la fenêtre "fnt"'
lblTitre = Label(fnt, text='JOUR DE LA SEMAINE', font='Calibri 15 bold')
lblTitre.place(x=110, y=25)
lblInfo = Label(fnt, text='Cet outil permet de savoir quel était le jour de la semaine de la date indiquée.', font='calibri 8')
lblInfo.place(x=20, y=80)
lblIndic = Label(fnt, text='Veuillez indiquer une date (format JJ MM AAAA) :', font='calibri 8')
lblIndic.place(x=10, y=150)
Rdate=StringVar()
lblResultat= Label(fnt, textvariable=Rdate)
lblResultat.place(x=250, y=250)
lblResultat1= Label(fnt, text="Le jour indiqué est un : ")
lblResultat1.place(x=50, y=250)

'Les champs de saisie pour la date'
strj = StringVar()
jour = Entry(fnt, textvariable=strj, justify='center')
jour.place(x=240, y=150, width=20)
strm = StringVar()
mois = Entry(fnt, textvariable=strm, justify='center')
mois.place(x=265, y=150, width=20)
stra = StringVar()
annee = Entry(fnt, textvariable=stra, justify='center')
annee.place(x=290, y=150, width=30)

'Le bouton permettant de calculer le jour de la date indiquée'
btnResult= Button(fnt, text='Résultat', command=Result)
btnResult.place(x=170, y=200)

fnt.mainloop()
