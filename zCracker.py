#!/usr/bin/python3
import zipfile

red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'

def extractFile(zfile, passwd):
	try:
		zfile.extractall(pwd=bytes(passwd, 'utf-8'))
		return True
	except:
		return False	

while True:
	try:
		zfile = input(f'{yellow}[{blue}*{yellow}] Enter Zip File Path Here: {green}')
		open_file = open(zfile)
                open_file.close()
	except FileNotFoundError:
		print(f'{yellow}[{red}-{yellow}] {red}File Not Found, Give Correct Path Of File.')
		continue
	else:
		zfile = zipfile.ZipFile(zfile)
		print(f'{yellow}[{green}✓{yellow}] {green}Zip File Found.')
		while True:
			try:
				passfile = input(f'{yellow}[{blue}*{yellow}] Enter Password File Path Here: {green}')
				pass_file = open(passfile)
                                pass_file.close()
			except FileNotFoundError:
				print(f'{yellow}[{red}-{yellow}] File Not Found, Give Correct Path Of File.')
				continue
			else:
				print(f'{yellow}[{green}✓{yellow}] {green}Password File Found.')
				break
		break

for line in open(passfile).readlines():
	passwd = line.strip('\n')
	if extractFile(zfile, passwd):
		print(f'{yellow}[{green}+{yellow}] Password Found: {green}{passwd}')
		break
	else:
		print(f'{yellow}[{red}-{yellow}]{blue} Password Tried: {red}{passwd}',end='\r')
