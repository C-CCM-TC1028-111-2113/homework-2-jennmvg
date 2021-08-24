import math
peso = float(input("Peso en kg: "))
altura = float(input("Altura en m: "))

IMC= peso/(altura**2)

if (IMC<20):
    print ("PESO BAJO")
elif(20<=IMC<25):
    print ("NORMAL")
elif (25<=IMC<30):
    print ("SOBREPESO")
elif (30<=IMC<40):
    print ("OBESIDAD")
elif (IMC>=40):
    print ("OBESIDAD MORBIDA")
    