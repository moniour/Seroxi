import requests
import base64
import time
import os
import json
from colorama import Fore, Style, init
init(autoreset=True)

webhook = ""

def greenonecuzlazy(rts):
    return(f"\x1b[1;38;2;0;255;0;49m[Soul]\x1b[0m {rts}")

def redonecuzlazy(rts):
    return(f"\x1b[1;38;2;255;0;0;49m[Soul]\x1b[0m {rts}")

def weburl():
    os.system("cls")
    global webhook
    webhook = input(greenonecuzlazy("Webhook Url: "))
    if webhook.startswith("https://discord.com/api/webhooks/"):
        print(greenonecuzlazy("Is A Webhook"))
        time.sleep(2)
        main()
    else:
        print(redonecuzlazy("Not A Webhook"))
        input("Press Enter To Return")
        weburl()

def main():
    os.system("cls")
    global webhook

    print("""
            \x1b[1;38;2;0;255;0;49m  _________                         .__ \x1b[0m
            \x1b[1;38;2;0;255;0;49m /   _____/ ___________  _______  __|__|\x1b[0m
            \x1b[1;38;2;0;255;0;49m \_____  \_/ __ \_  __ \/  _ \  \/  /  |\x1b[0m
            \x1b[1;38;2;0;255;0;49m /        \  ___/|  | \(  <_> >    <|  |\x1b[0m
            \x1b[1;38;2;0;255;0;49m/_______  /\___  >__|   \____/__/\_ \__|\x1b[0m
            \x1b[1;38;2;0;255;0;49m        \/     \/                  \/   \x1b[0m
          
            [1] Spam Webhook    [2] Send Webhook Message
            [3] Rename Webhook  [4] Change Webhook Avatar
            [5] Delete Webhook  [6] Webhook Status
            [7] Webhook Info    [8] Renter Webhook

            Made By oxg, discord.gg/oxg
    """)

    c = int(input(greenonecuzlazy("Your Choice: ")))

    if (c == 1):
        i = input(greenonecuzlazy("Delete Webhook When Done?(y / n): "))
        cont = input(greenonecuzlazy("What Message To Send?: "))

        r = requests.get(webhook)
        if (r.status_code == 200):
            for _ in range(9):
                requests.post(webhook, json={"content": cont})
                time.sleep(0.5)
            print(greenonecuzlazy("Spammed Webhook"))

        elif (r.status_code == 404):
            print(redonecuzlazy("Webhook Doesn't Exist Or You're Rate Limited"))

        if (i == "y"):
            print(greenonecuzlazy("Deleted Webhook"))
            requests.delete(webhook)

        input(greenonecuzlazy("Press Enter To Return"))
        main()

    elif (c == 2):
        i = input(greenonecuzlazy("Delete Webhook When Done?(y / n): "))
        cont = input(greenonecuzlazy("What Message To Send?: "))

        r = requests.get(webhook)
        if (r.status_code == 200):
            requests.post(webhook, json={"content": cont})
            print(greenonecuzlazy("Sent Message"))

        elif (r.status_code == 404):
            print(redonecuzlazy("Webhook Doesn't Exist Or You're Rate Limited"))

        if (i == "y"):
            print(greenonecuzlazy("Deleted Webhook"))
            requests.delete(webhook)

        input(greenonecuzlazy("Press Enter To Return"))
        main()

    elif (c == 3):
        n = input(greenonecuzlazy("Name: "))
        r = requests.get(webhook)
        if (r.status_code == 200):
            print(greenonecuzlazy("Renamed Webhook"))
            requests.patch(webhook, json={"name": n})
        elif (r.status_code == 404):
            print(redonecuzlazy("Webhook Doesn't Exist Or You're Rate Limited"))

        input(greenonecuzlazy("Press Enter To Return"))
        main()

    elif (c == 4):
        file_path = input(greenonecuzlazy("File Path: "))
        try:
            with open(file_path, 'rb') as f:
                idd = base64.b64encode(f.read()).decode('utf-8')
    
            if file_path.lower().endswith('.png'):
                it = 'png'
            elif file_path.lower().endswith('.webp'):
                it = 'webp'
            else:
                it = 'jpeg'
    
            r = requests.patch(webhook, json={'avatar': f'data:image/{it};base64,{idd}'})
            if r.status_code == 200:
                print(greenonecuzlazy("Changed Avatar"))
            else:
               print(redonecuzlazy("Webhook Doesn't Exist Or You're Rate Limited"))
        except FileNotFoundError:
            print(redonecuzlazy("File not found"))

        input(greenonecuzlazy("Press Enter To Return"))
        main()

    elif (c == 5):
        r = requests.get(webhook)
        if (r.status_code == 200):
            requests.delete(webhook)
            print(greenonecuzlazy("Deleted Webhook"))
        elif (r.status_code == 404):
            print(redonecuzlazy("Webhook Doesn't Exist Or You're Rate Limited"))
            
        input(greenonecuzlazy("Press Enter To Return"))
        main()
            
    elif (c == 6):
        r = requests.get(webhook)
        if (r.status_code == 200):
            print(greenonecuzlazy(r.status_code))
            print(greenonecuzlazy("Valid Webhook"))
        elif (r.status_code == 404):
            print(redonecuzlazy(r.status_code))
            print(redonecuzlazy("Webhook Doesn't Exist Or You're Rate Limited"))

        input(greenonecuzlazy("Press Enter To Return"))
        main()

    elif (c == 7):
        r = requests.get(webhook)
        if (r.status_code == 200):
            print(json.dumps(r.json(), indent=4))
        elif (r.status_code == 404):
            print(redonecuzlazy("Webhook Doesn't Exist Or You're Rate Limited"))

        input(greenonecuzlazy("Press Enter To Return"))
        main()


    elif (c == 8):
        weburl()

weburl()