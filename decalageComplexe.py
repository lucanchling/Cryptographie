# Header :
# Cryptage par décalage complexe (random ?)
# Créateur : Luc Anchling
# Date de création : 25/01/2021
# To do : Nothing

from random import randint

class cryptoDecalageComplexe:

    def __init__(self,phrase):
        self.phrase = phrase

    # Encryptage par décalage Complexe :
    def Crypt(self):
        global key
        key = [randint(0,50) for i in range(len(self.phrase))]
        code = [ord(self.phrase[i])+key[i] for i in range(len(self.phrase))]
        crypt = ""
        for i in code:
            crypt += chr(i)
        return crypt
    
    # Decryptage par decalage Complexe :
    def Decrypt(self):
        code = [ord(self.phrase[i])-key[i] for i in range(len(self.phrase))]
        decrypt = ""
        for i in code:
            decrypt += chr(i)
        return decrypt

