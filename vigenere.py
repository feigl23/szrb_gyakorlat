#https://www.geeksforgeeks.org/vigenere-cipher/
#https://inventwithpython.com/hacking/chapter21.html
#Szótár: https://inventwithpython.com/dictionary.txt

from rich.console import Console
from rich.theme import Theme
import enchant

custom_theme = Theme(
     {"key": "bold cyan", "text": "bold grey66", "cipher": "bold red"})
console = Console(theme=custom_theme)

def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) - len(key)):
			key.append(key[i % len(key)])
	return key

def coding(imsg,ikey,lkey,minus):
    result = ""
    for i in range(len(imsg)):
        if minus:
            value = (imsg[i] + ikey[i % lkey]) % 26
        else:
            value = (imsg[i] - ikey[i % lkey]) % 26
        result = result + chr(value + 65)
    return result


def encrypt(msg, key):
    lkey = len(key)
    ikey = [ord(i) for i in key]
    imsg = [ord(i) for i in msg]
    return coding(imsg,ikey,lkey, False)

def decrypt(cipher, key):
    lkey = len(key)
    ikey = [ord(i) for i in key]
    imsg = [ord(i) for i in cipher]
    return coding(imsg,ikey,lkey, True)

def hackVigenere(ciphertext):
    fo = open('dictionary.txt')
    words = fo.readlines()
    fo.close()
    i = 0
    for word in words:
        word = word.strip() # remove the newline at the end
        decryptedText = decrypt(ciphertext,word)
        console.print("Key " + str(word) + ":",style="key")
        console.print("Decrypted Message: {} " . format(decryptedText[:100]), style="text")
        i= i +1
        if i >100:
            return decryptedText
        
text = "TO INFINITY AND BEYOND"
keyword = "ABABA"
key = generateKey(text, keyword)
cipher = encrypt(text,key)
decrypted_msg = decrypt(cipher, key)
console.print("ENCRYPT", style="cipher")
console.print("Message: {} " . format(text), style="text")
console.print("Keyword : {} " . format(keyword), style="key")
console.print("Key : {} " . format(key), style="key")
print()
console.print("DECRYPT", style="cipher")
console.print("Cipher: {} " . format(cipher) , style="cipher")
console.print("Decrypted Message: {} " . format(decrypted_msg), style="text")
print()
print()
hackedMessage = hackVigenere(cipher)