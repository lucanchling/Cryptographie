# Header :
# Cryptage de str
# Créateur : Luc Anchling
# Date de création : 24/01/2021
# To do :


# Cryptage par décalage :

from decalage import cryptoDecalage

def affCryptoDec(phrase,decalage):
    print("Phrase : " + phrase)
    crypt = cryptoDecalage.decaCrypt(cryptoDecalage(phrase,decalage))
    print("Encryptée : "+crypt)
    decrypt = cryptoDecalage.decaDecrypt(cryptoDecalage(crypt,decalage))
    print("Décryptée : "+ decrypt)

#affCryptoDec("Salut je suis Luc",5)

