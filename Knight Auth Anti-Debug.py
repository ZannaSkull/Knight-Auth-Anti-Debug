from colorama import Fore, Style
import win32process
import win32api
import requests
import datetime
import psutil
import ctypes
import os

Cipolle = "https://discord.com/api/webhooks/1121222983860633631/0eersHuJ0IiApDabBnbjK4HTbSUufXMWcx9I1E7_99fdiDVk8dl25VDamm0hS6L_sqlF"

# Put the link of the accounts here
Pikachu = "https:/"
Zekrom = "/pas"
Tits = "tebin"
Boobs = ".com/"
Breats = "raw/"
Dick = ""

Knight = Pikachu + Zekrom + Tits + Boobs + Breats + Dick 

ImNotAFullStackDev = 3

ascii_knight = r"""
  _  __     _      _   _       _       _   _    
 | |/ /_ _ (_)__ _| |_| |_    /_\ _  _| |_| |_  
 | ' <| ' \| / _` | ' \  _|  / _ \ || |  _| ' \ 
 |_|\_\_||_|_\__, |_||_\__| /_/ \_\_,_|\__|_||_|
             |___/                              
""".format()

title = "Knight Auth"
title_bytes = title.encode('cp1252')
ctypes.windll.kernel32.SetConsoleTitleA(title_bytes)

def check_anti_debug():
    anti_debug_processes = [
        "wireshark.exe",
        "ollydbg.exe",
        "x64dbg.exe",
        "ida64.exe",
        "ida.exe",
        "windbg.exe",
        "x32dbg.exe",
        "ProcessHacker.exe",
        "r2.exe",
        "ghidra.exe",
        "hopper.exe",
        "BinaryNinja.exe",
        "cheatengine.exe",
        "jd-gui.exe",
        "java.exe",
        "ilspy.exe",
        "dnSpy.exe",
        "de4dot.exe",
        "VisualStudioDebuggingHost.exe",
        "pycharm.exe",
        "idea.exe",
        "studio64.exe",
        "gdb.exe",
        "lldb.exe",
        "xcodebuild.exe",
        "ollydbg2.exe",
        "ollydbg64.exe",
        "x64dbg2.exe",
        "idaq.exe",
        "idaw.exe",
        "windbg2.exe",
        "x32dbg2.exe",
        "r2r.exe",
        "ghidra2.exe",
        "hopper2.exe",
        "BinaryNinja2.exe",
        "cheatengine2.exe",
        "jd-gui2.exe",
        "java2.exe",
        "ilspy2.exe",
        "dnSpy2.exe",
        "de4dot2.exe",
        "VisualStudioDebuggingHost2.exe",
        "idea2.exe",
        "studio642.exe",
        "gdb2.exe",
        "lldb2.exe",
        "xcodebuild2.exe",
    ]  

    for proc in psutil.process_iter(["name", "pid"]):
        if proc.info["name"] in anti_debug_processes:
            pid = proc.info["pid"]
            try:
                handle = win32api.OpenProcess(win32con.PROCESS_TERMINATE, 0, pid)
                win32api.TerminateProcess(handle, -1)
                win32api.CloseHandle(handle)
                print(f"{Fore.RED}Anti-debug process detected and terminated: {proc.info['name']}{Style.RESET_ALL}")
            except Exception as e:
                print(f"{Fore.RED}Error terminating process: {e}{Style.RESET_ALL}")

def login():
    username = input(f"{Fore.LIGHTBLACK_EX}Username: {Style.RESET_ALL}")
    QwQ = input(f"{Fore.LIGHTBLACK_EX}Key: {Style.RESET_ALL}")

    response = requests.get(Knight)

    if response.status_code == 200:
        keys = response.text.splitlines()

        for user_key in keys:
            stored_username, stored_key = user_key.split(":")

            if username == stored_username and QwQ == stored_key:
                print(f"{Fore.GREEN}Accesso riuscito!{Style.RESET_ALL}")
                NonHoUnaTipaFissaMaMiStaBene(username, QwQ, "Accesso riuscito")
                return True

    print(f"{Fore.RED}Username o key non validi.{Style.RESET_ALL}")
    return False

def NonHoUnaTipaFissaMaMiStaBene(username, QwQ, status):
    Bocchino = {
        "username": "Access Log",
        "embeds": [
            {
                "title": "Nuovo accesso",
                "color": 0x9932CC, 
                "fields": [
                    {
                        "name": "Username",
                        "value": username,
                        "inline": True
                    },
                    {
                        "name": "Key",
                        "value": QwQ,
                        "inline": True
                    },
                    {
                        "name": "IP",
                        "value": Sussena(),
                        "inline": False
                    }
                ],
                "timestamp": str(datetime.datetime.now())
            }
        ]
    }
    response = requests.post(Cipolle, json=Bocchino)

def Sussena():
    response = requests.get("https://api.ipify.org?format=json")
    if response.status_code == 200:
        ip_data = response.json()
        return ip_data["ip"]

def authenticate():
    attempts = 0

    while attempts < ImNotAFullStackDev:
        if login():
            return True
        attempts += 1

        if attempts < ImNotAFullStackDev:
            print(f"{Fore.RED}Accesso non riuscito. Riprova.{Style.RESET_ALL}")

    print(f"{Fore.RED}Numero massimo di tentativi superato. Riprova più tardi.{Style.RESET_ALL}")
    return False

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.LIGHTBLACK_EX}{ascii_knight}{Style.RESET_ALL}")
    print(f"{Fore.LIGHTBLACK_EX}\n-| Knight Auth Login |-{Style.RESET_ALL}")
    print(f"1. {Fore.LIGHTBLACK_EX}Login{Style.RESET_ALL}")
    print(f"2. {Fore.LIGHTBLACK_EX}Esci{Style.RESET_ALL}")

    choice = input(f"{Fore.LIGHTBLACK_EX}Scelta: {Style.RESET_ALL}")

    if choice == "1":
        if authenticate():
        
            print(f"{Fore.GREEN}Avvio Tool{Style.RESET_ALL}")
            
            break
    elif choice == "2":
        break
    else:
        print(f"{Fore.RED}Scelta non valida. Riprova.{Style.RESET_ALL}")