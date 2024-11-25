def split_int(num,parts):
    to_add=num%parts
    result=[num//parts]*(parts-to_add)+[num//parts+1]*(to_add)
    
    
    return result
    
print(split_int(7,3))