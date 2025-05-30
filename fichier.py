import sys
from colorama import Fore, Back #pip install colorama

########################################################################################################

def print_progress_bar(index, total, label):
    
    n_bar = 50  # Progress bar width
    progress = index / total
    sys.stdout.write(Fore.RED +Back.GREEN+'\r')
    sys.stdout.write(f"[{ '=' * int(n_bar * progress):{n_bar}s}] {int(100 * progress)}%  {label}")
    sys.stdout.flush()
    sys.stdout.write(Fore.RESET +Back.RESET)
    
########################################################################################################

def lire_fichier(nomfichier):    
    res=""
    with open(nomfichier, 'r') as fichier:
        for line in fichier:
            res += line
    
    return res

########################################################################################################

def ecriture_fichier(nomfichier,chaine): 
    with open(nomfichier, 'w') as fichier:
        fichier.write(chaine)
    
########################################################################################################
def lire_ngrame(nomfichier):    
    res={}
    with open(nomfichier, 'r', errors='ignore') as fichier:
        for line in fichier:
            split=line.split(" ")
            n=len(split[0])
            res[split[0]]=int(split[1])
    res.update({"-n":n})
     
    return res 

########################################################################################################

def NETTOYER_lire_fichier(nomfichier):
    res=""
    with open(nomfichier, 'r') as fichier:
        for line in fichier:
            for c in line:
                if ord(c.upper()) in range(65,98):
                    res += c.upper()
     
    return res

########################################################################################################<

def nettoyer_texte(text): 
    res = ""
    for i in text: 
        if ord(i.upper()) in range(65,98):
            res += i.upper()
    return res
        