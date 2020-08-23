#!usr/bin/python
#ZIP Crack 0.1
#Coded By Doddy H
 
import sys,zipfile
 
def head():
 print "\n-- == ZIP Crack 0.1 == --\n"
 
def copyright():
 print "\n(C) Doddy Hackman 2013\n"
 
def sintax():
 print "\n[+] Sintax : "+sys.argv[0]+"<file> <wordlist>"
 
head()
 
if len(sys.argv) != 3 : 
 sintax()
else:
        
 try:
  passwords = open(sys.argv[2], "r").readlines()
 except :
  print "\n[-] Error opening file\n"
 op = 0  
 print "\n[+] Cracking ...\n"
 for password in passwords:
  password = password.replace("\r","").replace("\n","")
  if op==1:
   copyright()          
   sys.exit(0)
  try:
   test = zipfile.ZipFile(sys.argv[1])
   test.extractall(pwd=password)
   print "[+] Zip Cracked : "+sys.argv[1]
   print "[+] Password : "+password
   op = 1
  except:
   pass
   
 print "[-] Password Not Found"
 
copyright()
 
#The End ?
