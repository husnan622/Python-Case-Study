def reverse(s): 
    str = "" 
    for i in s: 
        str = i + str 
    return str 

s = "Hello World" 
print ("String awal : ",end="") 
print (s) 

print ("String yang sudah dibalik : ",end="") 
print (reverse(s)) 
