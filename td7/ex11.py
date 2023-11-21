maximum = float('-inf')  
minimum = float('inf')   

while True:
    val = int(input("Veuillez encoder une valeur: "))   
    if(val == -1):
        break
    else:
        maximum = max(maximum, val)
        minimum = min(minimum, val)

print("Le maximum est ", maximum, "et le minimum est ",minimum)   