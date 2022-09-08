import random
inputFileName = 'C:\Temp\model.txt'
text = []
with open(inputFileName, 'r') as inputFile, open(outputFileName, 'w') as outputFile:
    c = inputFile.readline()
    while c:
        text.append(c)
        c = inputFile.readline()
n = int(input())
k = len(text)
d = {}
textN = []
for i in range(k - n+1):
    wordN = ''
    for j in range(i, i + n):
        wordN += text[j] + " "
    textN.append(wordN)
key = set()
for i in range(k - n):
    pref = []
    pref = textN[i]
    post = text[i+n]
    if pref in key:
        post1 = d[pref]
        post1.append(post)
        d[pref] = post1
    else:
        d[pref] = [post]
        key.add(pref)
# print(d)

prevWords = []
strPrevWords = ''
for i in range(n):
    t = input()
    prevWords.append(t)
    strPrevWords += t + ' '
length = int(input())
ans = strPrevWords
for i in range(length):
    if strPrevWords in key:
        len1 = len(d[strPrevWords])
        j = random.randint(0, len1-1)
        ans += (d[strPrevWords])[j] + " "
        # print(len1)
    prevWords1 = []
    for k in range(n-1):
        prevWords1.append(prevWords[k+1])
    prevWords1.append((d[strPrevWords])[j])
    prevWords = prevWords1
    strPrevWords = ''
    for k in range(n):
        strPrevWords += prevWords[k] + ' '
print(ans)
