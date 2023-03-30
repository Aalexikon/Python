test_str = "Na blbosti mě užije"
 
new_str = ""
 
for i in range(len(test_str)):
    if i != 7:
        new_str = new_str + test_str[i]

print ("Řetězec po odstranění konkrétního znaku : " + new_str)