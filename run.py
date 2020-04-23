# ziziworks

from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.errors import SessionPasswordNeededError
import os, sys
import configparser
import csv
import time
from colorama import Fore, init as color_ama
color_ama(autoreset=True)

def banner():
    print(f"""
              {Fore.BLUE}╔╦╗{Fore.CYAN}┌─┐┬  ┌─┐{Fore.BLUE}╔═╗{Fore.CYAN}┌─┐┬─┐┌─┐┌─┐┌─┐┬─┐
              {Fore.BLUE} ║ {Fore.CYAN}├┤ │  ├┤ {Fore.BLUE}╚═╗{Fore.CYAN}│  ├┬┘├─┤├─┘├┤ ├┬┘
              {Fore.BLUE} ╩ {Fore.CYAN}└─┘┴─┘└─┘{Fore.BLUE}╚═╝{Fore.CYAN}└─┘┴└─┴ ┴┴  └─┘┴└─""")
    print(Fore.RED + '   -                   TeleScraper v1                 -' + Fore.RESET)
    print('')
    print(Fore.YELLOW + '   -               Channel Youtube :' + Fore.RED +' Zizi' + Fore.WHITE +'works' + Fore.YELLOW +'             -\n')

config = configparser.RawConfigParser()
config.read('config.data')

try:
    api_id = config['SETTING']['id']
    api_hash = config['SETTING']['hash']
    phone = config['SETTING']['phone']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('cls' if os.name=='nt' else 'clear')
    banner()
    print(Fore.RED+"[!] run 'python setup.py -c' first !!\n")
    sys.exit(1)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    try:
        client.sign_in(phone, input('Enter the code: '))
    except SessionPasswordNeededError:
        pword = input('Enter the 2FA Password: ')
        client.sign_in(password=pword)
    os.system('cls' if os.name=='nt' else 'clear')
    banner()
    client.sign_in(phone, input(Fore.GREEN+'[+] Enter the code: '+Fore.RED))
 
os.system('cls' if os.name=='nt' else 'clear')
banner()
chats = []
last_date = None
chunk_size = 200
groups=[]
 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
 
for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue
 
print(Fore.GREEN+'[+] Choose a group to scrape members :'+Fore.RED)
i=0
for g in groups:
    print(Fore.GREEN+'['+Fore.CYAN+str(i)+Fore.GREEN+']'+Fore.CYAN+' - '+ g.title)
    i+=1
 
print('')
g_index = input(Fore.GREEN+"[+] Enter a Number : "+Fore.RED)
target_group=groups[int(g_index)]
 
print(Fore.GREEN+'[+] Fetching Members...')
time.sleep(1)
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)
 
print(Fore.GREEN+'[+] Saving In file...')
time.sleep(1)
file = input(Fore.GREEN+"[+] Enter file name ("+Fore.RED+"????"+Fore.GREEN+".csv) : "+Fore.RED)
with open(file+".csv","w",encoding='UTF-8') as f:
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['username','phone','group'])
    for user in all_participants:
        if user.username:
            username= user.username
        else:
            username= ""
        if user.first_name:
            first_name= user.first_name
        else:
            first_name= ""
        if user.last_name:
            last_name= user.last_name
        else:
            last_name= ""
        name= (first_name + ' ' + last_name).strip()
        writer.writerow([username,user.phone,target_group.title])      
print(Fore.GREEN+'[+] Members scraped successfully.')
