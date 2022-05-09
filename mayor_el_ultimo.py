print("-------------------------------------------------")
print("---------MAYOR DE DOS Y MULTIPLO DEL MENOR-------")
print("-------------------------------------------------")


#INPUT

x= int(input("digite primer numero: "))
y= int(input("digite segundo numero: "))


#processing

if x > y and x % y == 0 :
    msj = (str(x) + " es multiplo de " + str(y) )
else: 
    msj = ("no son multiplos")

if x < y and y % x == 0 :
     msj = (str(y) + " es multiplo de " + str(x) )
else: 
    msj = ("no son multiplos")

print(msj)
