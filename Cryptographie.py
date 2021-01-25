# Header :
# Cryptage de str
# Créateur : Luc Anchling
# Date de création : 24/01/2021
# To do :

###########################
# Cryptage par décalage : #
###########################

from decalageSimple import cryptoDecalageSimple

def affCryptoDec(phrase,decalage):
    print("Cryptage par Décalage Simple : ")
    print("Phrase : " + phrase)
    crypt = cryptoDecalageSimple.Crypt(cryptoDecalageSimple(phrase,decalage))
    print("Encryptée : "+crypt)
    decrypt = cryptoDecalageSimple.Decrypt(cryptoDecalageSimple(crypt,decalage))
    print("Décryptée : "+ decrypt)

#affCryptoDec("Salut je suis Luc",5)

################################################
# Cryptage par décalage Complexe (aléatoire) : #
################################################

from decalageComplexe import cryptoDecalageComplexe

def affCryptoDecCplx(phrase):
    print("Cryptage par Décalage Complexe : ")
    print("Phrase : " + phrase)
    crypt = cryptoDecalageComplexe.Crypt(cryptoDecalageComplexe(phrase))
    print("Encryptée : "+crypt)
    decrypt = cryptoDecalageComplexe.Decrypt(cryptoDecalageComplexe(crypt))
    print("Décryptée : "+ decrypt)

#affCryptoDecCplx("Salut je suis Luc")