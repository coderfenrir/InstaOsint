import os
import instaloader
from colorama import Fore, Style
from termcolor import colored

# Renkli çıktılar için renk tanımları
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RED = Fore.RED
BLUE = Fore.BLUE
CYAN = Fore.CYAN
RESET = Style.RESET_ALL

# Ekranı temizle
os.system('clear' if os.name == 'posix' else 'cls')

# Banner
def banner():
    banner = r"""

██╗ ██████╗      ██████╗ ███████╗██╗███╗   ██╗████████╗
██║██╔════╝     ██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
██║██║  ███╗    ██║   ██║███████╗██║██╔██╗ ██║   ██║
██║██║   ██║    ██║   ██║╚════██║██║██║╚██╗██║   ██║
██║╚██████╔╝    ╚██████╔╝███████║██║██║ ╚████║   ██║                                                 ╚═╝ ╚═════╝      ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝
"""
    colored_banner = colored(banner, "green")
    print(colored_banner)

banner()

instagram = colored("Instagram: ", "magenta") + colored("@coderfenrir", "yellow")
github = colored("GitHub: ", "magenta") + colored("coderfenrir", "yellow")
version = colored("Version: ", "magenta") + colored("1.0", "yellow")

print(instagram)
print(github)
print(version)

# Kullanıcı adını kendiniz girebilirsiniz
print("")
username = input("Kullanıcı adını girin: ")
print("")

# Instaloader nesnesi oluşturma
loader = instaloader.Instaloader()

# Profil bilgilerini indirme
try:
    profile = instaloader.Profile.from_username(loader.context, username)
except Exception as e:
    print(f"{RED}Hata: {str(e)}{RESET}", file=sys.stderr)
    sys.exit(1)

# Profil bilgilerini alma
full_name = profile.full_name
username = profile.username
id = profile.userid
bio = profile.biography
profile_pic_url = profile.profile_pic_url
followers_count = profile.followers
following_count = profile.followees
external_url = profile.external_url
is_private = profile.is_private
is_verified = profile.is_verified

# Bilgileri renkli olarak ekrana yazdırma
print(f"{GREEN}Profil Bilgileri{RESET}")
print("---------------")
print(f"{YELLOW}Tam Adı:{RESET} {full_name}")
print(f"{YELLOW}Kullanıcı Adı:{RESET} {username}")
print(f"{YELLOW}ID:{RESET} {id}")
print(f"{YELLOW}Biyografi:{RESET} {bio}")
print(f"{YELLOW}Profil Resmi URL:{RESET} {profile_pic_url}")
print(f"{YELLOW}Takipçiler:{RESET} {followers_count}")
print(f"{YELLOW}Takip Edilen:{RESET} {following_count}")
print(f"{YELLOW}Websitesi:{RESET} {external_url}")
print(f"{YELLOW}Hesap Gizli mi:{RESET} {is_private}")
print(f"{YELLOW}Doğrulanmış Hesap mı:{RESET} {is_verified}")
print("")
