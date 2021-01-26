# Header :
# Cryptage - Version Graphique
# Créateur : Luc Anchling
# Date de création : 26/01/2021
# To do : Faire toute la partie grapique

from tkinter import Tk, Canvas, Label, Entry, Menu, Button, Listbox, END

# Partie Graphique :

# Fentetre Graphique:
fen = Tk()
fen.title('Cryptographie')
fen.geometry('500x300')

cnv = Canvas(fen)

cryptoType = Label(cnv,text='Type de Cryptage :')
cryptoType.pack(side='top')

# Selection du type de cryptage :
typeOfCrypto = ["Décalage Simple", "Décalage Complexe", "Code de César", "Carrée de Polybe", "Vigenère"]
selec = Listbox(cnv,height = 5)
selec.pack(side='top')
for element in typeOfCrypto:
    selec.insert(END, element)

drt = Label(cnv,text='Texte à Encrypté :')
drt.pack(side='left')
gch = Label(cnv,text='Text Décrypté')
gch.pack(side='right')
cnv.pack()

fen.mainloop()
