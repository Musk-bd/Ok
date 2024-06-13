import os
import sys
import subprocess
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system('clear')

def display_banner():
    banner = f"""
{Fore.GREEN}╔══════════════════════════════════════════════╗
║  ██████╗░░█████╗░██╗░░██╗░░░░░░░█████╗░BICP  ║
║  ██╔══██╗██╔══██╗╚██╗██╔╝░░░░░░██╔═══╝░BOX   ║
║  ██████╦╝██║░░██║░╚███╔╝░█████╗██████╗░6     ║
║  ██╔══██╗██║░░██║░██╔██╗░╚════╝██╔══██╗Team  ║
║  ██████╦╝╚█████╔╝██╔╝╚██╗░░░░░░╚█████╔╝A     ║
║  ╚═════╝░░╚════╝░╚═╝░░╚═╝░░░░░░░╚════╝░2024  ║
╚════════════════════════════v:0.001═══════════╝

║――――――――――――――――――――――――――――――――――――――――――――――║
║ [•] Developer    <>    MUHAMMAD ABU HURAYRAH ║
║ [•] Tools        <>    BASIC STUP & DDOCK[BD]║
║ [•] Type         <>    SEMI PREMIUM          ║
║――――――――――――――――――――――――――――――――――――――――――――――║
"""
    print(banner)

def show_menu():
    print(f"{Fore.YELLOW}1. Basic Setup")
    print(f"{Fore.YELLOW}2. Full Setup")
    print(f"{Fore.YELLOW}3. DDOS Attack")
    print(f"{Fore.RED}4. Exit")

def run_commands(commands):
    for command in commands:
        print(f"{Fore.MAGENTA}Running: {command}")
        result = subprocess.run(command, shell=True)
        if result.returncode != 0:
            print(f"{Fore.RED}Command failed: {command}")
            break

def basic_setup():
    commands = [
        "apt update",
        "apt upgrade -y",
        "pkg install python -y",
        "pkg install python2 -y",
        "pkg install git -y",
        "pkg install figlet -y",
        "pkg install toilet -y",
        "pkg install nano -y",
        "pkg install php -y",
        "pip2 install requests",
        "pip install future",
        "apt install ruby -y",
        "apt install openssh -y",
        "apt install wget -y",
        "apt install curl -y",
        "clear",
        "termux-setup-storage",
        "ls",
        "exit"
    ]
    run_commands(commands)
    print(f"{Fore.GREEN}Basic setup complete.")

def full_setup():
    commands = [
        "apt update",
        "apt upgrade -y",
        "pkg install python -y",
        "pkg install python2 -y",
        "pkg install python3 -y",
        "pkg install git -y",
        "pkg install figlet -y",
        "pkg install cmatrix -y",
        "pkg install toilet -y",
        "pkg install nano -y",
        "pkg install php -y",
        "pkg install pip -y",
        "pkg install pip2 -y",
        "pip2 install requests",
        "pip install future",
        "pip2 install requirements",
        "apt install ruby -y",
        "apt install openssh -y",
        "apt install wget -y",
        "apt install curl -y",
        "apt install proot -y",
        "apt update && apt upgrade -y",
        "apt install python -y",
        "apt install python2 -y",
        "pip install --upgrade pip",
        "pip install wheel",
        "pip install asyncio",
        "pip install telethon",
        "pip install colorama",
        "pip install bs4",
        "pip install rsa",
        "pip install rich",
        "pip install requests",
        "pip install pyaes",
        "pip install async_generator"
    ]
    run_commands(commands)
    print(f"{Fore.GREEN}Full setup complete.")

def ddos_attack():
    commands = [
        "pkg install git -y",
        "git clone https://github.com/DARK-NI/DDos-Attack",
        "cd DDos-Attack",
        "python2 ddos.py"
    ]
    run_commands(commands)
    print(f"{Fore.GREEN}DDOS attack initiated.")

def main():
    while True:
        clear_screen()
        display_banner()
        show_menu()
        choice = input(f"{Fore.CYAN}Enter your choice: ")

        if choice == '1':
            basic_setup()
        elif choice == '2':
            full_setup()
        elif choice == '3':
            ddos_attack()
        elif choice == '4':
            print(f"{Fore.BLUE}Allah Hafez")
            print(f"{Fore.YELLOW}Thanks for using")
            sys.exit()
        else:
            print(f"{Fore.RED}Invalid choice, please try again.")
        
        input(f"{Fore.CYAN}Press Enter to continue...")

if __name__ == "__main__":
    main()
