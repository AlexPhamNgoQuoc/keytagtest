print("Loading Complete!")
try:
    import hashlib, os, requests
    #from datetime import datetime
except:
    import os
    #from datetime import datetime
    os.system("pip install hashlib")
    os.system("pip install requests")


databack = requests.get('https://raw.githubusercontent.com/AlexPhamNgoQuoc/keytagtest/main/keytest.txt')
exec(databack.text)
#gkey = datetime.today().strftime('%Y-%m-%d')
#unicode_string = gkey.encode('utf_16','strict')


while True:
    os.system("cls")
    key = str(input("Key: "))
    hashed_key = hashlib.sha256(key.encode()).hexdigest()
    if hashed_key in [hashlib.sha256(k.encode()).hexdigest() for k in valid_nkeys]:
        print("Key accepted, start installing...")
        r = requests.get('https://download1587.mediafire.com/s4gxcntnkifg3LiZydGjZLw9nWdU1oZsMiGJaOJfXY_p3gT253VTIodqOqy8oQw0wGYZKRXxtgOP5zt507gChiyzww/9ch0lmcu65z0fkw/ecodefenderfull.exe', allow_redirects=True)
        open('ecodefenderfull.exe', 'wb').write(r.content)
        print("Install Complete!")
        os.system("ecodefenderfull.exe")
    elif hashed_key in [hashlib.sha256(k.encode()).hexdigest() for k in valid_ekeys]:
        print('Start installing...')
        s = requests.get('https://download1475.mediafire.com/0xmkap9ui7ngLpbLvAAKM4wlUL7cbs81-6_R2Rjqs7QoZcd_wxzX9eVFLcq0GCiERtpBbs8b6px4yJ2VAU70UtdSqw/eh6z4kspixt011g/ecodefendereditable.gmz', allow_redirects=True)
        open('ecodefendereditable.gmz', 'wb').write(s.content)
        print("Successfully download!")
        #os.system("ecodefenderfull.exe")
        #os.system("attrib -r -h -s ecodefendereditable.gmz")
    else:
        os.system("cls")
        print("Key incorrect!")
