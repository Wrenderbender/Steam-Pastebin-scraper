#OPTIMIMSE THIS NY USING MULTIPLE CORES 

import random, requests, re, thread
from bs4 import BeautifulSoup
invalid = True
x=1
while invalid:
    charlist = []
    validletters = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i in range(8):
        charlist.append(random.choice(validletters))#ascii table is retarded
    charlist = "".join(charlist)

    url = "https://pastebin.com/" + charlist
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    print(f"attempted {x} amount of times")
    x+=1 
    if soup.textarea != None:
        print("Found valid link")
        invalid = False
        break
print(url)

start=0;end=17
for i in str(soup.textarea):
    if i in validletters:
        retext = (str(soup.textarea)[start:end])
        regexed = re.search("[^@,:,;,\s,a-z]{5}\-[^@,:,;,\s,a-z]{5}\-[^@,:,;,\s,a-z]{5}", retext)
        if regexed:
            start+=17
            end+=17
            file=open("webout.txt","w+")
            file.write(retext)
            file.write("\n")
        else:
            start+=1
            end+=1            

    else:
        start+=1
        end+=1