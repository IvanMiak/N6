with open(inputFileName, 'r') as inputFile, open(outputFileName, 'w') as outputFile:
    c = inputFile.readline()
    while c:
        for i in range(len(c)):
            if 97 <= ord(c[i]) <= 122:
                word += c[i]
                f = 1
            elif 65 <= ord(c[i]) <= 90:
                word += chr(ord(c[i]) + 32)
                f = 1
            elif f == 1:
                text.append(word)
                print(word + "\n", file=outputFile)
                word = ""
                f = 0
        c = inputFile.readline()
    if f == 1:
        # text.append(word)
        print(word + "\n", file=outputFile)
