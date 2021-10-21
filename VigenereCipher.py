import string
# Alphabeth characters with index in dictionary (in uppercase)
charIndex = dict(zip(string.ascii_uppercase, range(0,26)))
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():

    print("Q7")
    key = "BAD"
    cipher = "uhhgiyfmrtthgfldihotfzbhsdhgeqeeutaufaquifjpduiroegvcduirodhuefuirorhbcwjoqbngsevjllfnffdrsepfmefrfzbhsshduujtbjspvcknouftkbndoiwuosjc"
    cipher = cipher.upper()

    print("Secret key: " + key)
    print("Ciphertext: \n" + cipher)
    plainText = decrypt(cipher, key)
    print("Plaintext: \n " + plainText)

    

def encrypt(text, key):

    encryptedText = ""

    keystream = createKeystream(key, text)

    for i in range(0, len(text)):
        letterIndex = encryptLetter(text[i], keystream[i])
        letter = alphabet[letterIndex]
        encryptedText += letter
    return encryptedText

def decrypt(text, key):
    
    decryptedText = ""

    keystream = createKeystream(key, text)

    for i in range(0, len(text)):
        letterIndex = decryptLetter(text[i], keystream[i])
        letter = alphabet[letterIndex]
        decryptedText += letter
    return decryptedText

def encryptLetter(letterMsg, letterKeystream):
    """
    Returns index 
    """
    return (charIndex[letterMsg] + charIndex[letterKeystream]) % len(charIndex) 

def decryptLetter(letterMsg, letterKeystream):
    """
    Returns index 
    """
    return (charIndex[letterMsg] - charIndex[letterKeystream]) % len(charIndex) 

def createKeystream(key, message):
    keystream = ""

    keyCopy = key 
    key = key 

    for c in message:
        if len(key) == 0: 
            key = keyCopy 
        keystream += key[0]
        key = key[1:]

    return keystream

if __name__ == "__main__":
    main()

