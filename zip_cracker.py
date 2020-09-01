#Autor >> AlfonzMx
#Creando con python3
from tqdm import tqdm
from colorama import init, Fore
import zipfile
import sys, random, time

init()
def ClownLogo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

                   _____   ________     ______                __            
                  /__  /  /  _/ __ \   / ____/________ ______/ /_____  _____
                    / /   / // /_/ /  / /   / ___/ __ `/ ___/ //_/ _ \/ ___/
                   / /___/ // ____/  / /___/ /  / /_/ / /__/ ,< /  __/ /    
                  /____/___/_/       \____/_/   \__,_/\___/_/|_|\___/_/     
                                                          

            Nota! : Scanning Port es un escaner 100% funcional, verifique con nmap.       
    """
    for N, line in enumerate(x.split("\n")):
         sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
         time.sleep(0.05)
ClownLogo()
try:
	#Iniciando Lista de contraseñas
    wordlist = sys.argv[2]
    # the zip file you want to crack its password
    zip_file = sys.argv[1]
except:
	exit()

# initialize the Zip File object
zip_file = zipfile.ZipFile(zip_file)
# count the number of words in this wordlist
n_words = len(list(open(wordlist, "rb")))
# print the total number of passwords
print("Total passwords to test:", n_words)
with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
        try:
            zip_file.extractall(pwd=word.strip())
        except:
            continue
        else:
            print("[+] Password found:", word.decode().strip())
            exit(0)
print("[!] Password not found, try other wordlist.")
