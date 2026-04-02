import cloudscraper
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
{W}  | {G}VERSION  {W}: {C}3.5 (ULTRA BYPASS)          {W}|
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
    
    print(f"\n{Y}[*] Bypassing Cloudflare & Getting Token...")
    
    # Cloudscraper استعمال کریں جو خودکار طور پر سکیورٹی بائی پاس کرتا ہے
    scraper = cloudscraper.create_scraper()
    
    try:
        # سٹیپ 1: ٹوکن فیچ کرنا
        res = scraper.get("https://leofame.com/free-instagram-likes", timeout=25)
        
        # کوکیز سے ٹوکن نکالنا
        token = res.cookies.get("token")
        
        # اگر کوکیز میں نہ ملے تو پیج کے اندر سے نکالیں
        if not token and 'name="token" value="' in res.text:
            token = res.text.split('name="token" value="')[1].split('"')[0]

        if not token:
            end_dashboard("FAILED", "Security Too High! Change VPN Location to USA/UK.")
            return

        # سٹیپ 2: لائکس بھیجنا
        payload = {
            "token": token,
            "timezone_offset": "5",
            "free_link": post_url,
            "quantity": str(qty)
        }

        print(f"{Y}[*] Injecting Likes... Please Wait.")
        
        api_url = "https://leofame.com/free-instagram-likes?api=1"
        response = scraper.post(api_url, data=payload, timeout=25)
        
        if response.status_code == 200:
            res_json = response.json()
            if res_json.get("status") == "success":
                end_dashboard("SUCCESS", "Likes Sent Successfully! ✅")
            else:
                end_dashboard("ERROR", res_json.get("message", "Rate Limit Reached"))
        else:
            end_dashboard("ERROR", "Provider Server Denied Access")

    except Exception as e:
        end_dashboard("CRASHED", "Connection Timeout - Use Faster Internet")

if __name__ == "__main__":
    run_script()
