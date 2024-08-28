import unicodedata

def quitar_tildes(cadena):
    cadena_normalizada = unicodedata.normalize('NFD', cadena)
    cadena_sin_tildes = ''.join(c for c in cadena_normalizada if not unicodedata.combining(c))
    return cadena_sin_tildes
palabra = input("Ingrese una palabra. Adivinare si es un Palindromo\n").replace(",", "").replace(".", "").replace(" ","")
palabra =quitar_tildes(palabra)
cont = 1
cont2 =0
palindromo=0

for i in palabra:
        if palabra.lower()[-cont] == palabra.lower()[cont2]:
            cont+=1
            cont2+=1
            palindromo+=1
        else:
            palindromo+=0     
if palindromo == len(palabra):
        print("Si es un Palindromo")
else:
    print("No es un Palidromo")







