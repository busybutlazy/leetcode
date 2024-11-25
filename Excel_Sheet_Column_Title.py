def convertToTitle(columnNumber):
    """
    :type columnNumber: int
    :rtype: str
    """
    columnNumber-=1
    if(columnNumber<26):
        return chr(columnNumber+65)
    else:
        return convertToTitle(columnNumber//26)+convertToTitle(columnNumber%26+1)
    
a=convertToTitle(52)
print(a)