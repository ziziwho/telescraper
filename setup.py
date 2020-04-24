# ziziworks

"""

you can re run setup.py 
if you have added some wrong value

"""


import os, sys
import time
os.system("""
		pip3 install colorama
		""")
from colorama import Fore, init as color_ama
color_ama(autoreset=True)

def banner():
    os.system('cls' if os.name=='nt' else 'clear')
    print(f"""
        {Fore.BLUE}╔╦╗{Fore.CYAN}┌─┐┬  ┌─┐{Fore.BLUE}╔═╗{Fore.CYAN}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
        {Fore.BLUE} ║ {Fore.CYAN}├┤ │  ├┤ {Fore.BLUE}╚═╗{Fore.CYAN}│  ├┬┘├─┤├─┘├┤ ├┬┘
        {Fore.BLUE} ╩ {Fore.CYAN}└─┘┴─┘└─┘{Fore.BLUE}╚═╝{Fore.CYAN}└─┘┴└─┴ ┴┴  └─┘┴└─
    {Fore.RED}╔═╗{Fore.CYAN}┌─┐┌┬┐┬ ┬┌─┐
    {Fore.RED}╚═╗{Fore.CYAN}├┤  │ │ │├─┘
    {Fore.RED}╚═╝{Fore.CYAN}└─┘ ┴ └─┘┴
    """)
    print(Fore.RED + '   -                   TeleScraper v1                 -' + Fore.RESET)
    print('')
    print(Fore.YELLOW + '   -               Channel Youtube :' + Fore.RED +' Zizi' + Fore.WHITE +'works' + Fore.YELLOW +'             -\n')

def requirements():
	banner()
	print(Fore.GREEN+"[+] Installing requierments ...")
	os.system("""
		pip3 install colorama telethon requests configparser
		python3 -m pip install colorama telethon requests configparser
		touch config.data
		""")
	banner()
	print(Fore.GREEN+"[+] requierments Installed.\n")


def config_setup():
	import configparser
	banner()
	cpass = configparser.RawConfigParser()
	cpass.add_section('SETTING')
	xid = input(Fore.GREEN+"[+] enter api ID : "+Fore.RED)
	cpass.set('SETTING', 'id', xid)
	xhash = input(Fore.GREEN+"[+] enter hash ID : "+Fore.RED)
	cpass.set('SETTING', 'hash', xhash)
	xphone = input(Fore.GREEN+"[+] enter phone number : "+Fore.RED)
	cpass.set('SETTING', 'phone', xphone)
	setup = open('config.data', 'w')
	cpass.write(setup)
	setup.close()
	print(Fore.GREEN+"[+] configuration complete !")


try:
	if any ([sys.argv[1] == '--config', sys.argv[1] == '-c']):
		print(Fore.GREEN+'['+Fore.CYAN+'+'+Fore.GREEN+']'+Fore.CYAN+' selected module : '+Fore.RED+sys.argv[1])
		config_setup()
	elif any ([sys.argv[1] == '--install', sys.argv[1] == '-i']):
		requirements()
	elif any ([sys.argv[1] == '--help', sys.argv[1] == '-h']):
		banner()
		print(""" HELP!
			
	( --config  / -c ) API configration
	( --install / -i ) Install requirements
	( --help    / -h ) Show this msg 
			""")
	else:
		print('\n'+Fore.GREEN+'['+Fore.RED+'!'+Fore.GREEN+']'+Fore.CYAN+' unknown argument : '+ sys.argv[1])
		print(Fore.GREEN+'['+Fore.RED+'!'+Fore.GREEN+']'+Fore.CYAN+' for help use : ')
		print(Fore.GREEN+'$ python3 setup.py -h'+'\n')
except IndexError:  
	print('\n'+Fore.GREEN+'['+Fore.RED+'!'+Fore.GREEN+']'+Fore.CYAN+' no argument given : '+ sys.argv[1])
	print(Fore.GREEN+'['+Fore.RED+'!'+Fore.GREEN+']'+Fore.CYAN+' for help use : ')
	print(Fore.GREEN+'$ python3 setup.py -h'+'\n')
