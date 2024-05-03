# https://teachen.info/cspp/unit4/lab04-02.html

from rich.console import Console
from rich.theme import Theme

custom_theme = Theme(
     {"shift": "bold cyan", "text": "bold grey66", "cipher": "bold red"})
console = Console(theme=custom_theme)

def getLetter(letter, minus):
     letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
     if minus:
         return letters[(letters.find(letter) - shift) % len(letters)]
     return letters[(letters.find(letter) + shift) % len(letters)]
    
def inLetters(letter):
    letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    if letter in letters:
        return True
    return False


def encrypt(text,shift):
    eresult = ""
    for letter in text:
        if inLetters(letter):
            eresult = eresult + getLetter(letter, False)
        else:
            eresult = eresult + letter
    return eresult
    
def decrypt(text, shift):
    deresult = "" 
    for letter in text:
        if inLetters(letter):
            deresult = deresult + getLetter(letter, True)
        else:
            deresult = deresult +  letter
    return deresult
    
def hack(cipher, letters):
    for shift in range(len(letters)):
        hresult = ""
        for letter in cipher:
            hresult = hresult +  letters[(letters.find(letter) - shift) % len(letters)]
        console.print("Shift {}" . format(shift), style="text")
        console.print("Decrypted Message: {} " . format(hresult), style="cipher")


message = "Elementary my dear Watson"
shift = 4
cipher = encrypt(message,shift)
console.print("ENCRYPT", style="cipher")
console.print("Message: {} " . format(message), style="text")
console.print("Shift : {} " . format(shift), style="shift")
console.print("Cipher: {} " . format(cipher) , style="cipher")
print()
console.print("DECRYPT", style="cipher")
decrypted_msg = decrypt(cipher,shift)
console.print("Decrypted Message: {} " . format(decrypted_msg), style="text")
print()
print()

letters1="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
letters2="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "
console.print("TRY 1", style="cipher")
hack(cipher, letters1)
console.print("TRY 2", style="cipher")
hack(cipher, letters2)