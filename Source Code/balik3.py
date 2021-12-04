def reverse(string): 
    string = "".join(reversed(string)) 
    return string 

s = "Hello World" 
print ("String awal : ",end="") 
print (s) 

print ("String setelah dibalik: ",end="") 
print (reverse(s)) 
