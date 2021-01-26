# Header :
# Cryptage par la méthode de Vigenère
# Créateur : Luc Anchling
# Date de création : 25/01/2021
# To do : Nothing

class cryptoVigenere:
    def __init__(self,phrase,key):
        self.phrase = phrase
        self.key = key
        # Initialisation du Tableau
        global tab
        lettre = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        tab = [lettre]
        for i in range(25):
            let = lettre[:]
            lettre = [lettre[i] for i in range(1,len(lettre))]
            lettre.append(let[0])
            tab.append(lettre)
    
    def Crypt(self):
        global key_adjust,crypt
        key_adjust = ""
        for i in range(len(self.phrase)):
            key_adjust += self.key[i%len(self.key)]
        crypt = ""
        for i in range(len(self.phrase)):
        # Pour les caractères
            if self.phrase[i] in [" ",",","é","è","à","ç","'","(",")","?","!",".",":","-"]:
                crypt += self.phrase[i]
        # Pour les lettres
            else:
                # Recherche l'équivalent avec la méthode de Vigenere
                crypt += tab[tab[0].index(self.phrase[i].lower())][tab[0].index(key_adjust[i])]
        return crypt

    def Decrypt(self):
        decrypt = ""
        for i in range(len(self.phrase)):
        # Pour les caractères
            if self.phrase[i] in [" ",",","é","è","à","ç","'","(",")","?","!",".",":","-"]:
                decrypt += self.phrase[i]
        # Pour les lettres
            else:
                # Pour trouver la ligne correspondant au décryptage
                for li in range(26):
                    if tab[li][tab[0].index(key_adjust[i])] == crypt[i]:
                        break
                # Recherche de l'équivalent avec la méthode de Viginere
                decrypt += tab[li][0]
        return decrypt