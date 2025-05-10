lookupTableInstructions = [
    [(0, 0, 0), "CHAR1"],
    [(128, 128, 128), "CHAR2"],
    [(255, 255, 255), "PRINT"],
]
lookupTableCharacters1 = [
    [(255, 0,   0),   "a"],
    [(255, 255, 0),   "b"],
    [(255, 0,   255), "c"],
    [(0,   255, 0),   "d"],
    [(255, 255, 128), "e"],
    [(128, 255, 255), "f"],
    [(0,   0,   255), "g"],
    [(255, 128, 255), "h"],
    [(0,   255, 255), "i"],
    [(128, 255, 0),   "j"],
    [(128, 0,   255), "k"],
    [(128, 255, 128), "l"],
    [(0,   128, 0),   "m"],
    [(255, 128, 0),   "n"],
    [(64,   128, 255), "o"],
    [(255, 128, 128), "p"],
]
lookupTableCharacters2 = [
    [(255, 0,   0),   "q"],
    [(255, 255, 0),   "r"],
    [(255, 0,   255), "s"],
    [(0,   255, 0),   "t"],
    [(255, 255, 128), "u"],
    [(128, 255, 255), "v"],
    [(0,   0,   255), "w"],
    [(255, 128, 255), "x"],
    [(0,   255, 255), "y"],
    [(128, 255, 0),   "z"],
    [(128, 0,   255), " "],
    [(128, 255, 128), "."],
    [(0,   128, 0),   "!"],
    [(255, 128, 0),   "("],
    [(64,   128, 255), ")"],
    [(255, 128, 128), "'"],
]

def encode(code):
    print(code)

    keys = []

    code = code.replace("(", "")
    code = code.replace(" ", " SPACE ")
    words = code.split(" ")
    for word in words:
        if word == "print":
            keys.append(2)
            keys.append(0)
        elif word == "SPACE":
            keys.append(1)
            keys.append(10)
        else:
            for character in word:
                for char in range(len(lookupTableCharacters1)):
                    if lookupTableCharacters1[char][1] == character:
                        keys.append(0)
                        keys.append(char)
                for char in range(len(lookupTableCharacters2)):
                    if lookupTableCharacters2[char][1] == character:
                        keys.append(1)
                        keys.append(char)
    
    print(keys)
    return keys
