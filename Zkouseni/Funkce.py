def zdvojnasob(cisla):
    for i in range(len(cisla)):
        cisla[i] = cisla[i] * 2
    return cisla


teploty = [2,15,3,21,56,22]
print(teploty)         
zdvojnasob (teploty)
print(teploty)