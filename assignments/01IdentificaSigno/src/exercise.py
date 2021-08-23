import math
def main():
    #escribe tu código abajo de esta línea
    print (´Dame un número:´)
    number= int (input())
    
    if (number==0):
        print (`es cero´)
    elif (number<0):
        print (`es negativo´)
    else:
        print (`es positivo´)
    pass
    

if __name__ == '__main__':
    main()
