import fichier
import cipher 
import test
text=fichier.lire_fichier("text.txt")
text=cipher.encipher(text,test.cle_de_cryptage)
fichier.ecriture_fichier("textchif.txt",text)