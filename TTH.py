import math
from string import ascii_uppercase
from random import choice

def main():
    
    
    hash = "CQCY"
    msg = "" 
    hashTry = ""
    count = 0 
    chars = ascii_uppercase + " "
    while(True):
        msg = msg.join(choice(chars) for i in range(48))
        print("Try: ", count, " msg: ", msg)
        hashTry = TTH(msg.replace(" ", ""))
        if (hashTry == hash):
            break 
        msg = ""
        count += 1 
    print("msg: \n" + msg + "\n Has hash: " + hashTry + "\n Which equals " + hash)
    

def TTH(text):
    a_Dict = {v:k for k,v in enumerate(ascii_uppercase)}
    a_Dict[0] = '0' 

    # Return hash 
    hash = str()

    # Initial runningtotal 
    runningTotal = [0, 0, 0, 0]

    # Split into block (size 16)
    blocks = list() 
    numBlocks = math.ceil(len(text) / 16)
    
    while(len(blocks) < numBlocks):
        block = list() 
        while(len(block) < 16):
            if(len(text) == 0):
                block.append((0, '0'))
            else:
                letter = (a_Dict[text[0]], text[0],)
                block.append(letter)
                text = text[1:]
        blocks.append(block)

    for block in blocks: 
        runningTotal = findBlockHash(block, runningTotal)

    # Create hash 
    for i in runningTotal:
        letter = list(a_Dict.keys())[list(a_Dict.values()).index(i)]
        hash += letter 

    return hash 


def findBlockHash(block, runningTotal):

    # ROUND 1 
    # Split block into sublists
    splitted = list() 
    for i in range(4):
        start = int(i * len(block) / 4)
        end = int((i+1) * len(block) / 4)
        splitted.append(block[start:end])

    block = splitted

    # Update running total 
    updateRunningTotal(block, runningTotal)
    
    # ROUND 2 
    i = 0
    for row in block:
        if i == 3:
            block[3] = row[::-1]
        else: 
            block[i] = rotate(row, i)
            #print(block[i])
            i += 1 

    updateRunningTotal(block, runningTotal)
    

    return runningTotal 

def updateRunningTotal(lst, runningTotal):

    columns = toColumnList(lst)
    
    runningTotal = runningTotal
    newNumbers = [0, 0, 0, 0]

    # Find new running total 
    index = 0
    for column in columns:
        columnSum = sum([i[0] for i in column])
        newNumbers[index] = columnSum % 26 
        index += 1 

    i = 0 
    for n1, n2 in zip(runningTotal, newNumbers):
        runningTotal[i] = (n1 + n2) % 26 
        i += 1 

def toColumnList(lst):
    columns = list() 
    for i in range(4):
        column = list() 
        for row in lst:
            column.append(row[i])
        columns.append(column)

    return columns 

def rotate(lst, n):
    n += 1 
    return lst[n:] + lst[:n]


if __name__ == "__main__":
    main() 