# ===============================================================
# Copyright (c) 2025 Karim Elyamani. All rights reserved.
# This script is the intellectual property of Karim Elyamani.
# Unauthorized copying, editing, or distribution of this code,
# via any medium, is strictly prohibited without written permission.
# ===============================================================

import requests
import json
import random
import string

def PolyDev_InstaLikes():
    print("Script by Karim Elyamani - Unauthorized edits are prohibited.")
    instagram_link = input("Enter Instagram post URL: ")
    try:
        quantity = int(input("Enter number of likes (max 31): "))
        if quantity > 31:
            print("Max allowed is 31. Setting quantity to 31.")
            quantity = 31
    except ValueError:
        print("Invalid input. Setting quantity to 31.")
        quantity = 31

    random_text_number = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    session = requests.Session()

    def data_maker():
        headers = {
            "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-platform": '"Android"',
            "upgrade-insecure-requests": "1",
            "user-agent": f"Mozilla/{random_text_number} (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-GB,en;q=0.9",
            "if-modified-since": "Sat, 12 Apr 2025 16:25:47 GMT",
            "priority": "u=0, i",
            "content-length": "0"
        }
        session.get("https://leofame.com/free-instagram-likes", headers=headers)
        cookies = session.cookies.get_dict()
        return cookies.get("token"), cookies.get("ci_session")

    token, ci_session = data_maker()
    if not token or not ci_session:
        print("Failed to get token or ci_session.")
        return

    url = "https://leofame.com/free-instagram-likes?api=1"
    data = {
        "token": token,
        "timezone_offset": "Africa/Casablanca",
        "free_link": instagram_link,
        "quantity": str(quantity)
    }
    length = len(json.dumps(data).encode())

    headers = {
        "content-length": str(length),
        "sec-ch-ua-platform": "Android",
        "user-agent": f"Mozilla/{random_text_number} (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Mobile Safari/537.36",
        "sec-ch-ua": '"Chromium";v="134", "Not:A-Brand";v="24", "Google Chrome";v="134"',
        "content-type": "application/x-www-form-urlencoded",
        "sec-ch-ua-mobile": "?1",
        "accept": "*/*",
        "origin": "https://leofame.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://leofame.com/free-instagram-likes",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "en-GB,en;q=0.9",
        "cookie": f"token={token}; ci_session={ci_session}"
    }

    response = session.post(url, headers=headers, data=data)
    print(f"Status: {response.status_code}")
    print("Response:", response.text)

PolyDev_InstaLikes()
