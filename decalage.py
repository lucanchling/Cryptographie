# Header :
# Cryptage par décalage (peu utile car facilement décryptable)
# Créateur : Luc Anchling
# Date de création : 25/01/2021
# To do : Nothing

class cryptoDecalage :

    def __init__(self,phrase,dec):
        self.dec = dec
        self.phrase = phrase

    def __str__(self):
        return str(self.phrase)
    # Encryptage par décalage :
    def decaCrypt(self):
        code = [ord(i)+self.dec for i in self.phrase]
        crypt = ""
        for i in code:
            crypt += chr(i)
        return crypt
    # Décryptage pa décalage :
    def decaDecrypt(self):
        code = [ord(i)-self.dec for i in self.phrase]
        decrypt = ""
        for i in code:
            decrypt += chr(i)
        return decrypt