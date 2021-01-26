# Header :
# Cryptage de str
# Créateur : Luc Anchling
# Date de création : 24/01/2021
# To do : Vigenère

###########################
# Cryptage par décalage : #
###########################

from TypeOfCrypto.decalageSimple import cryptoDecalageSimple

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

from TypeOfCrypto.decalageComplexe import cryptoDecalageComplexe

def affCryptoDecCplx(phrase):
    print("Cryptage par Décalage Complexe : ")
    print("Phrase : " + phrase)
    crypt = cryptoDecalageComplexe.Crypt(cryptoDecalageComplexe(phrase))
    print("Encryptée : "+crypt)
    decrypt = cryptoDecalageComplexe.Decrypt(cryptoDecalageComplexe(crypt))
    print("Décryptée : "+ decrypt)

#affCryptoDecCplx("Salut je suis Luc")

################################
# Cryptage par Code de César : #
################################

from TypeOfCrypto.cesarCode import cryptoCesar

def affCryptoCesar(phrase,key):
    print("Cryptage par Code César : ")
    print("Phrase : " + phrase)
    crypt = cryptoCesar.Crypt(cryptoCesar(phrase,key))
    print("Encryptée : "+crypt)
    decrypt = cryptoCesar.Decrypt(cryptoCesar(crypt,key))
    print("Décryptée : "+ decrypt)

#affCryptoCesar("Salut je suis Luc",5)

################################################
# Cryptage par l'approche du carré de Polybe : #
################################################

from TypeOfCrypto.carrePolybe import cryptoPolybe

def affCryptoPolybe(phrase):
    print("Cryptage par Code César : ")
    print("Phrase : " + phrase)
    crypt = cryptoPolybe.Crypt(cryptoPolybe(phrase))
    print("Encryptée : "+crypt)
    decrypt = cryptoPolybe.Decrypt(cryptoPolybe(crypt))
    print("Décryptée : "+ decrypt)

#affCryptoPolybe("salut je suis luc")


#########################################
# Cryptage par l'approche de Vigenère : #
#########################################

from TypeOfCrypto.Vigenere import cryptoVigenere

def affCryptoVigenere(phrase,key):
    print("Cryptage par Code César : ")
    print("Phrase : " + phrase)
    crypt = cryptoVigenere.Crypt(cryptoVigenere(phrase,key))
    print("Encryptée : "+crypt)
    decrypt = cryptoVigenere.Decrypt(cryptoVigenere(crypt,key))
    print("Décryptée : "+ decrypt)

#affCryptoVigenere("Salut moi c'est luc","bonjour")