def pointer_maker(n):
    def pointer():
        try:
            tmp=n
            
        except:
            tmp+=1
        return tmp
    return pointer

p12=pointer_maker(12)
p13=pointer_maker(13)
# hello_p()
# hello_p()
print(p12())
print(p13())