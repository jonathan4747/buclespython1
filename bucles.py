#numeros 1 al 50
for i in range(0,151):
   print(i)

#multiplos de 5
for i in range (5,1001,5):
    print(i)

#conding Dojo

for i in range (1,101):
    if i%10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else:
        print(i) 

#imprime los impares del 0 al 500000
suma = 0        
for i in range (0,500001):
    if i%2 != 0:
        suma = suma + i

print(suma)

#cuenta regresiva
for i in range(2018,-1,-4):
    print(i)

# imprime los valores mltiplo de mult
alto = 9
bajo = 2
mult = 4
for i in range(bajo,(alto+1)):
    if i%mult == 0:
        print(i)