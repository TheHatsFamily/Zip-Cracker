# About this project
A python based tool which is used for recovering zip file password by dictionary attack.
# Requirements
1) You have any terminal (eg. Linux)
2) Installed python3 on your system. ( In linux type this command on your terminal:- apt install python3 -y ) 
# How to download and run
    git clone https://github.com/TheHatsFamily/zip-cracker.git
    cd zip-cracker
    chmod +x zCracker.py
    ./zCracker.py
## How to download and run in one step
    git clone https://github.com/TheHatsFamily/zip-cracker.git; cd zip-cracker; chmod +x zCracker.py; ./zCracker.py
# How to use
When you start it by ./zCracker.py, it will ask you about Zip file path,
> Note:- Here you must be a valid path of zip file which you want to crack. 

Here you have to give a valid path where your zip file located or your target zip file located (eg. /root/test.zip).
If you entered right path it will show you, "[✓] File Found.".
Then it will ask about Password File,
> Note:- Here you must be a valid path of password file for dictionary attack. And this file password be seprated by ENTER or '\n'.

Here you must be give an path of your fictionary attack's password file which contains password and seperated by ENTER or '\n'. (eg. /usr/share/wordlists/rockyou.txt), if you give correct passfile, it show you "[✓] File Found" message on screen
# Disclamer
this tool made for educational purpose only, if you do any illegal activity by this tool, we are not responsible for that.
Happy Hacking :)
