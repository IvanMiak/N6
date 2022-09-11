import random
inputFileName = 'model.txt'
text = []
with open(inputFileName, 'r') as inputFile:
    c = inputFile.readline()
    while c:
        text.append(c)
        c = inputFile.readline()
n = 2
k = len(text)
d = {}
textN = []
for i in range(k - n + 1):
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
prefix = input()
word = ""
f = 0
for i in range(len(prefix)):
    if 1072 <= ord(prefix[i]) <= 1103 or 97 <= ord(prefix[i]) <= 122:
        word += prefix[i]
        f = 1
    elif 1040 <= ord(prefix[i]) <= 1071 or 65 <= ord(prefix[i]) <= 90:
        word += chr(ord(prefix[i]) + 32)
        f = 1
    elif f == 1:
        prevWords.append(word)
        word = ""
        f = 0

if f == 1:
    prevWords.append(word)
ans = ""
k = len(prevWords)
if k >= n:
    for i in range(k):
        ans += prevWords[i] + " "
    prevWords = prevWords[k-n:]
    for i in range(n):
        strPrevWords += prevWords[i] + ' '
else:
    strPrevWords = key.pop()
    key.add(strPrevWords)
    f = 0
    word = ""
    for i in range(len(strPrevWords)):
        if 1072 <= ord(strPrevWords[i]) <= 1103 or 97 <= ord(strPrevWords[i]) <= 122:
            word += strPrevWords[i]
            f = 1
        elif f == 1:
            prevWords.append(word)
            word = ""
            f = 0
    ans += strPrevWords

length = int(input())

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
