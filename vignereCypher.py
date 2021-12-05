intDecode=int(input("Decode or encode? -1 to decode, 1 to encode "))
strMessage=str(input("Message ")).upper()
strCode=str(input("Code ")).upper()
strAns=str()
strAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(len(strMessage)):
    if (strMessage[i] in strAlphabet):
        strAns+=strMessage[i]
strMessage=strAns
strAns=str()
for i in range(len(strCode)):
    if (strCode[i] in strAlphabet):
        strAns+=strCode[i]
strCode=strAns
strCode*=len(strMessage)
strAns=str()
charCur=''
for i in range(len(strMessage)):
    charCur=chr(ord(strMessage[i])+((ord(strCode[i])-ord("A"))*intDecode))
    if (charCur>"Z"):
        charCur=chr(ord(charCur)-26)
    elif (charCur<"A"):
        charCur=chr(ord(charCur)+26)
    strAns+=charCur
print(strAns)