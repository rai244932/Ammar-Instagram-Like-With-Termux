import requests
import random
import time
import os

# --- COLORS ---
G = '\033[1;32m'
R = '\033[1;31m'
W = '\033[1;37m'
C = '\033[1;36m'
Y = '\033[1;33m'

def logo():
    os.system('clear')
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
{W}  | {G}VERSION  {W}: {C}3.1 (STABLE FIX)            {W}|
{Y}  -------------------------------------------
    """)

def end_dashboard(status, message):
    print(f"\n{Y}  ===========================================")
    print(f"{W}  |            {G}RESULT DASHBOARD             {W}|")
    print(f"{Y}  ===========================================")
    print(f"{W}  | {G}STATUS  {W}: {C}{status}")
    print(f"{W}  | {G}MESSAGE {W}: {W}{message}")
    print(f"{Y}  -------------------------------------------")
    print(f"{G}   DEVELOPED BY: {W}AMMAR-RAI TECH™")
    print(f"{Y}  ===========================================\n")

def run_script():
    logo()
    post_url = input(f"{G}[+]{C} Post URL {W}: ")
    qty = input(f"{G}[+]{C} Quantity (Max 31) {W}: ")
    
    print(f"\n{Y}[*] Bypassing Security & Getting Token...")
    
    # بہتر ہیڈرز تاکہ ویب سائٹ کو لگے کہ یہ موبائل براؤزر ہے
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    session = requests.Session()
    
    try:
        # سٹیپ 1: ٹوکن حاصل کرنا (With Timeout)
        res = session.get("https://leofame.com/free-instagram-likes", headers=headers, timeout=20)
        token = session.cookies.get("token")
        
        if not token:
            # متبادل طریقہ اگر کوکیز سے ٹوکن نہ ملے
            if 'name="token" value="' in res.text:
                token = res.text.split('name="token" value="')[1].split('"')[0]

        if not token:
            end_dashboard("FAILED", "IP Blocked! Please Switch to Mobile Data or Use VPN.")
            return

        # سٹیپ 2: لائکس بھیجنا
        payload = {
            "token": token,
            "timezone_offset": "5",
            "free_link": post_url,
            "quantity": str(qty)
        }

        print(f"{Y}[*] Submitting Request...")
        api_headers = headers.copy()
        api_headers.update({"X-Requested-With": "XMLHttpRequest", "Referer": "https://leofame.com/free-instagram-likes"})
        
        response = session.post("https://leofame.com/free-instagram-likes?api=1", headers=api_headers, data=payload, timeout=20)
        
        if response.status_code == 200:
            res_json = response.json()
            if res_json.get("status") == "success":
                end_dashboard("SUCCESS", "Likes Sent Successfully! ✅")
            else:
                end_dashboard("ERROR", res_json.get("message", "Unknown Error"))
        else:
            end_dashboard("ERROR", "Server Rejected Request")

    except Exception as e:
        end_dashboard("CRASHED", "Connection Timeout - Try Again")

if __name__ == "__main__":
    run_script()
