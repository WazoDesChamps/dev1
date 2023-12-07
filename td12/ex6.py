liste = ['b', 'o', 'n', 'j', 'o', 'u', 'r']
new_liste = []

for element in liste[:]:
    new_liste.append(ord(element) - 97)

print(new_liste)