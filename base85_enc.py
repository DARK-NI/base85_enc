import random
import base64
import os
import sys
import time

os.system("clear")
os.system("lolcat logo.txt")
file = input("\n\n\033[1;37m   Enter File Path : \033[1;32m")
try:
	ar = open(file).read()
except:
	print("\033[1;31mFile Not Found\033[1;37m")
	sys.exit()
sn = repr(base64.b85encode(ar.encode()))
out = input("\n\033[1;37m   Enter Output File Name : \033[1;32m")
try:
	ni = open(out,"w")
except:
	err = "\n\n\033[1;31m   This Name Is Not Available !\n   Trying To Save File With Random Name\n\033[1;37m"
	for c in err:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.06)
	nmbr = random.randint(111,999)
	out = "dark_ni_" + str(nmbr) + (".dark_ni")
	ni = open(out,"w")
ni.write(f"# Compiled By Md Nazmul Islam (DARK-NI)\n# Github: github.com/DARK-NI\n# Facebook: fb.com/link.copy.koro.kno.babu\n# Teligram: t.me/md_nazmulislam\n# Note: Don\'t Try To Decrypt This Tool\n\n\nimport base64\nexec(base64.b85decode({sn}))")
ni.close()
time.sleep(2)
print("\n\033[1;32m      ════════════════════════════     \033[1;37m")
print("\n\033[1;37m   File Successfully Encrypted !")
print("\n   Encrypted File Name :\033[1;32m " + out)
print("\n\033[1;37m   Encrypted File Path :\033[1;32m $HOME/base85_enc")
print("\n\033[1;32m      ════════════════════════════     \033[1;37m")
os.system("xdg-open https://facebook.com/groups/spamming.termux.learning.point/")
