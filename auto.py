#──────────────{ IMPORT }──────────────#
import os,platform
#──────────────{ COLOR }──────────────#
W = '\x1b[1;37m'
Y = '\x1b[1;33m'
B = '\x1b[1;34m'
P = '\x1b[1;35m'
G = '\x1b[1;32m'
R = '\x1b[1;31m'
J = '\x1b[38;5;208m'
PURPLE ='\x1b[38;5;46m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
CYAN = '\033[1;36m'
BLACK="\033[1;30m"
EXTRA ='\x1b[38;5;208m'
RESET = '\033[0m'
#──────────────{ GIT PULL }──────────────#
os.system("clear")
os.system('git pull --quiet 2>/dev/null')
#──────────────{ JOIN WHATSAPP GROUP }──────────────#
os.system("clear")
print(f'{R}[{G}•{R}]{G} JOIN WHATSAPP GROUP {RESET}')
os.system('xdg-open https://chat.whatsapp.com/JBRMR1OyrxK2tsDlJUgh69')
Tweak=platform.architecture()[0]
if Tweak=="32bit":
    os.system("clear")
    __import__("createfb")
elif Tweak=="64bit":
    os.system("clear");exit(f"{R}[{G}•{R}]{G} SORRY 64BIT DEVICE NOT SUPPORTED")
    __import__("createfb")
#──────────────{ END }──────────────#
