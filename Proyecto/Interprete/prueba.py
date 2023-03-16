p='y'
p1='clase'
p2='ademas'
p3='falso'
p4='para'
p5='fun'
p6='si'
p7='nulo'
p8='o'
p9='imprimir'
p10='retornar'
p11='super'
p12='este'
p13='verdadero'
p14='var'
p15='mientras'

print("Analizador Lexico")

print("Ingrese cadena")
cadena = input()



for i, caracter in enumerate(cadena):
  if i == 0:
    pass
  else:
    if cadena[i-1] == cadena[i]:
      print ("Caracter ", caracter, " repetido en posiciones", i-1, " y ", i )


if (cadena == p):
    print ("La cadena es: ", cadena, "La palabra reservada es: ", p)
elif (cadena == p1):
    print ("La cadena es: ", cadena, "La palabra reservada es: ", p1)
elif (cadena == p2):
   print ("La cadena es: ", cadena, "La palabra reservada es: ", p2)
elif (cadena == p3):
    print ("La cadena es: ", cadena, "La palabra reservada es: ", p3)
elif (cadena == p4):
    print ("La cadena es: ", cadena, "La palabra reservada es: ", p4)
elif (cadena == p5):
   print ("La cadena es: ", cadena, "La palabra reservada es: ", p5)
elif (cadena == p6):
    print ("La cadena es: ", cadena, "La palabra reservada es: ", p6)
elif (cadena == p7):
    print ("La cadena es: ", cadena, "La palabra reservada es: ", p7)
elif (cadena == p8):
    print ("La cadena es: ", cadena, "La palabra reservada es: ", p8)
elif (cadena == p9):
    print ("La cadena es: ", cadena, "La palabra reservada es: ", p9)
elif (cadena == p10):
    print ("La cadena es: ", cadena, "La palabra reservada es: ", p10)
elif (cadena == p11):
    print ("La cadena es: ", cadena, "La palabra reservada es: ", p11)
elif (cadena == p12):
    print ("La cadena es: ", cadena, "La palabra reservada es: ", p12)
elif (cadena == p13):
    print ("La cadena es: ", cadena, "La palabra reservada es: ", p13)
elif (cadena == p14):
    print ("La cadena es: ", cadena, "La palabra reservada es: ", p14)
elif (cadena == p15):
    print ("La cadena es: ", cadena, "La palabra reservada es: ", p15)

for indice in range(len(cadena)):
    caracter = cadena[indice]
    print("En el índice {} tenemos a '{}'".format(indice, caracter))