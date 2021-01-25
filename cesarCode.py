# Header :
# Cryptage par décalage - Code de César
# Créateur : Luc Anchling
# Date de création : 25/01/2021
# To do : All

class cryptoCesar:
    def __init__(self,phrase,key):
        self.phrase = phrase
        self.key = key

    # Encryptage par décalage Cesar :
    def Crypt(self):
        code = []
        for i in self.phrase:
            # Pour les majuscules
            if ord(i)>=65 and ord(i)<=90:
                code.append((ord(i)+self.key-65)%26+65)
            # Pour les minuscules
            if ord(i)>=97 and ord(i)<=122:
                code.append((ord(i)+self.key-97)%26+97)
            # Pour le reste
            if i in [" ",",","é","è","à","ç","'","(",")","?","!",".",":"]:
                code.append(ord(i))
        crypt = ""
        for i in code:
            crypt += chr(i)
        return crypt
    
    # Decryptage par decalage Cesar :
    def Decrypt(self):
        code = []
        for i in self.phrase:
            # Pour les majuscules
            if ord(i)>=65 and ord(i)<=90:
                code.append((ord(i)-self.key-65)%26+65)
            # Pour les minuscules
            if ord(i)>=97 and ord(i)<=122:
                code.append((ord(i)-self.key-97)%26+97)
            # Pour le reste
            if i in [" ",",","é","è","à","ç","'","(",")","?","!",".",":"]:
                code.append(ord(i))
        decrypt = ""
        for i in code:
            decrypt += chr(i)
        return decrypt

print(ord(" "))