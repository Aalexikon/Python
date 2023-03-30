def nejvetsi(pole, n):

    max = pole[0]

    for i in range(1, n):
        if pole[i] > max:
            max = pole[i]
    return max

arr = [10, 324, 45, 90, 9808]
n = len(arr)
vysledek = nejvetsi(arr, n)
print("Největší v daném poli ", vysledek)

#Najde v seznamu největší číslo a vypíše ho#