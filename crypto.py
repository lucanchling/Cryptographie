# Header :
# Cryptage de str
# Créateur : Luc Anchling
# Date de création : 24/01/2021
# To do :


# Cryptage par décalage :

from decalageSimple import cryptoDecalageSimple

def affCryptoDec(phrase,decalage):
    print("Phrase : " + phrase)
    crypt = cryptoDecalageSimple.decaCrypt(cryptoDecalageSimple(phrase,decalage))
    print("Encryptée : "+crypt)
    decrypt = cryptoDecalageSimple.decaDecrypt(cryptoDecalageSimple(crypt,decalage))
    print("Décryptée : "+ decrypt)

#affCryptoDec("Salut je suis Luc",5)

