
def main():
    """ 
    print("Round 1 Transposition Cipher")

    key = "3415726"
    msg = "LGTYRFNKMLIGHQKUCGDIDFYQNBWLMVWMVVYGQMOYAXNALFIAT"
    
    print("Text 1: \n " + msg )
    print("Key (k2): \n " + key)
    print("Encypted (Text 1): " + encrypt(msg, key))
    """
    """ print("Round 2 Transposition Cipher")
    key = "3415726"
    msg = "CTUKWZUGAANZXNDEKSVOFLGQKDQCNDMTQRTTVCQPQNOPAQVNJ"
    
    print("Text 2: \n " + msg )
    print("Key (k2): \n " + key)
    print("Encypted (Text 2): " + encrypt(msg, key))
     """

    k2 = "3415726"
    ciphertext = "TLCQWMLYIGNMOFLKKFMGNRGDBVYINQDLYXTGMUYVQAFHIWVAA"

    decryptedCipher = decrypt(ciphertext, k2)
    print("Decryption process (Transposition Cipher)")
    print("Third decryption of final ciphertext: \n " + decryptedCipher)



    
def decrypt(cipher, key):
    
    plainText = ""

    key = [int(c) for c in key]
    n = max(key)

    columnSize = int(len(cipher) / n)

    columnTable = [] 
    cipherCopy = cipher 

    for i in range(0, n):
        column = [] 
        for j in range(0, columnSize):
            column.append(cipherCopy[0])
            cipherCopy = cipherCopy[1:]
        columnTable.append(column)

    d = dict() 
    for (k, i) in zip(key, columnTable):
        d[k] = i 

    orderedColumnTable = [] 

    for k in sorted(key):
        orderedColumnTable.append(d[k])

    for i in range(0, columnSize):
        for c in orderedColumnTable:
            plainText += c[i]

    return plainText

def encrypt(text, key):

    cipher = ""

    key = [int(c) for c in key]
    n = max(key)

    table = [text[i:i+n] for i in range(0, len(text), n)]
    
    lastRow = table[-1]
    if(len(lastRow) < n):    
        lastRow += (len(lastRow) - 1) * "X"
        table[-1] = lastRow
    
    for i in range(len(table)):
        table[i] = [char for char in table[i]]

    columnTable = []
    for i in range(0, n):
        column = [] 
        for row in table:
            column.append(row[i])
        columnTable.append(column)

    reorderedTable = []

    for k in key: 
        reorderedTable.append(columnTable[k - 1])

    for column in reorderedTable:
        for c in column: 
            cipher += c

    return cipher

if __name__ == "__main__":
    main() 