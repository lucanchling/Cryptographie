# Header :
# Cryptage par l'approche du carré de Polybe
# Créateur : Luc Anchling
# Date de création : 25/01/2021
# To do : Nothing

class cryptoPolybe:
    def __init__(self,phrase):
        self.phrase = phrase
        global polybe_conv,polybe_key
        polybe_conv = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ",",","é","è",".",":","!","?"]
        polybe_key = [11,12,13,14,15,16,17,21,22,23,24,25,26,27,31,32,33,34,35,36,37,41,42,43,44,45,46,47,51,52,53,54,55,56]

    # Encryptage par décalage Cesar :
    def Crypt(self):
        global code
        code = ""
        for i in self.phrase:
            code += str(polybe_key[polybe_conv.index(i.lower())])
        return code
    
    # Decryptage par decalage Cesar :
    def Decrypt(self):
        decrypt = ""
        for i in range(0,len(code),2):
            decrypt += str(polybe_conv[polybe_key.index(int(code[i]+code[i+1]))])
        return decrypt