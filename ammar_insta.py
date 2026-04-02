# ===============================================================
# ⚡ BRAND: AMMAR-RAI TECH™ 
# 👤 OWNER: RAI AMMAR (PROFESSOR AMMAR)
# 📞 WHATSAPP: +923018787786
# 🛠️ STATUS: TERMUX VIP STYLISH EDITION
# ===============================================================

import requests
import random
import time
import os
import sys

# رنگوں کے کوڈز (Stylish Look)
G = '\033[1;32m' # Green
R = '\033[1;31m' # Red
W = '\033[1;37m' # White
B = '\033[1;34m' # Blue
Y = '\033[1;33m' # Yellow
C = '\033[1;36m' # Cyan

def clear():
    os.system('clear')

def logo():
    clear()
    print(f"""
{C}   ______   __  __  __  __  ______   ______    
{C}  /\  __ \ /\ \/ / /\ \/ / /\  __ \ /\  == \   
{C}  \ \  __ \ \ \  _"-\ \  _"-\ \  __ \ \  __<   
{C}   \ \_\ \_\ \ \_\ \_\ \_\ \_\ \_\ \_\ \_\ \_\ 
{C}    \/_/\/_/  \/_/\/_/\/_/\/_/\/_/\/_/\/_/ /_/ 
{Y}  ___________________________________________
{W}  | {G}OWNER    {W}: {C}RAI AMMAR (PROFESSOR)       {W}|
{W}  | {G}BRAND    {W}: {C}AMMAR-RAI TECH™             {W}|
{W}  | {G}WHATSAPP {W}: {C}+923018787786               {W}|
{W}  | {G}VERSION  {W}: {C}3.0 (VIP STYLISH)           {W}|
{Y}  -------------------------------------------
    """)

def end_dashboard(status, message):
    print(f"\n{Y}  ===========================================")
    print(f"{W}  |            {G}RESULT DASHBOARD             {W}|")
    print(f"{Y}  ===========================================")
    print(f"{W}  | {G}STATUS  {W}: {C}{status}                 ")
    print(f"{W}  | {G}MESSAGE {W}: {W}{message}               ")
    print(f"{Y}  -------------------------------------------")
    print(f"{G}   DEVELOPED BY: {W}AMMAR-RAI TECH™")
    print(f"{G}   CONTACT     : {W}+923018787786")
    print(f"{Y}  ===========================================\n")

def run_script():
    logo()
    print(f"{G}[+]{W} Enter Instagram Post Details Below:")
    post_url = input(f"{G}[+]{C} Post URL {W}: ")
    
    try:
        qty = int(input(f"{G}[+]{C} Quantity (Max 31) {W}: "))
        if qty > 31: qty = 31
    except:
        qty = 31

    print(f"\n{Y}[*] Connecting to Ammar Cloud Server...")
    time.sleep(1)
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://leofame.com/free-instagram-likes"
    }

    session = requests.Session()
    
    try:
        # سٹیپ 1: ٹوکن فیچ کرنا
        session.get("https://leofame.com/free-instagram-likes", headers=headers, timeout=15)
        token = session.cookies.get("token")

        if not token:
            end_dashboard("FAILED", "Could Not Get Token! Try VPN.")
            return

        # سٹیپ 2: لائکس ریکوئسٹ
        payload = {
            "token": token,
            "timezone_offset": "5",
            "free_link": post_url,
            "quantity": str(qty)
        }

        print(f"{Y}[*] Injecting Likes to Link...")
        response = session.post("https://leofame.com/free-instagram-likes?api=1", headers=headers, data=payload, timeout=20)
        
        res_data = response.json()
        
        if res_data.get("status") == "success":
            end_dashboard("SUCCESS", "Likes Sent Successfully! ✅")
        else:
            msg = res_data.get('message', 'Invalid Link or Limit Reached')
            end_dashboard("ERROR", msg)

    except Exception as e:
        end_dashboard("CRASHED", str(e))

if __name__ == "__main__":
    while True:
        run_script()
        ask = input(f"{G}[?]{W} Do you want to use again? (y/n): ")
        if ask.lower() != 'y':
            print(f"\n{C}Thank you for using AMMAR-RAI TECH™ Tools!{W}")
            break
