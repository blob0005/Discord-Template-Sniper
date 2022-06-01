try:
    import os
    from os import system
    system("title " + "Discord Template Sniper")
except:
    pass
import random, time
any_error = False
try:
    import requests
    import colorama
except:
    any_error = True
if any_error == True:
    print("Missing Modules, Press Enter To Start Repair Process (May Not Always Work)")
    input("")
    try:
        import os
        os.system("pip install requests")
        os.system("pip install colorama")
        print("")
        print("")
        print("Problem May Be Fixed Now, Restart The Program")
        input("")
        exit()
    except:
        print("Error While Fixing")
        input("")
        exit()
def sniper():
    colorama.init(autoreset=True)
    done = 0
    #Has no threads bc you would get rate limited
    choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    while True:
        done = int(done) + 1
        re = random.choices(choices, k=12)
        url = "https://discord.com/api/v9/guilds/templates/" + "".join(re)
        print_url = "https://discord.new/" + "".join(re)
        r = requests.get(url)
        r = str(r)
        if "200" in r:
            print(colorama.Fore.GREEN + f"[{str(done)}/{str(amount)}] Generated Valid Template! "+print_url)
            if save == "y":
                save_file = open("valid_templates.txt", "a")
                save_file.write(print_url+"\n")
                save_file.close()
        else:
            print(colorama.Fore.RED + f"[{str(done)}/{str(amount)}] Generated Invalid Template! "+print_url)
            if save == "y":
                save1_file = open("invalid_templates.txt", "a")
                save1_file.write(print_url+"\n")
                save1_file.close()
        if int(done) == int(amount):
            print("Done")
            input()
            exit()
        time.sleep(delay)
def valid():
    print("Enter A Valid Choice")
while True:
    try:
        delay = input("Enter Delay (0 For None): ")
        delay = float(delay)
        break
    except:
        valid()
while True:
    save = input("Auto Save (y/n): ")
    if save == "y" or save == "n":
        break
    else:
        valid()
while True:
    try:
        amount = input("Amount To Check: ")
        amount = int(amount)
        break
    except:
        valid()
sniper()
