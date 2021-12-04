def reverse(s): 
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 

s = "Hello World" 
print ("String awal : ",end="") 
print (s) 

print ("String yang sudah dibalik: ",end="") 
print (reverse(s)) 
