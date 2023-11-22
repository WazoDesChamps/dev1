txt = str(input("Donnez un mot: "))
txti = txt[::-1]
palindrome = False

for i in range(len(txt)):
    if(txt[i] == txti[i]):
        palindrome = True

if palindrome:
    print("Oui")
else:
    print("Non")
