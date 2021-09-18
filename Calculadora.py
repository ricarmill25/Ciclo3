#Calculadora

n1 = float(input("\n\nNumero 1 : "))
n2 = float(input("\nNumero 2 : "))

print("\n Escoja la Operación\n")
resp = int(input(" 1. Suma \n 2. Multiplicar \n 3. Restar \n 4. División \n\n Opcion : "))

if resp == 1:
    print(f"\nEl resultado de sumar ",n1," + ",n2," es : ",round(n1+n2,2),"\n")

else:
    if resp == 2:
        print(f"\nEl resultado de multiplicar ",n1," * ",n2," es : ",round(n1*n2,2),"\n")

    else:
        if resp == 3:
            print(f"\nEl resultado de restar ",n1," - ",n2," es : ",round(n1-n2,2),"\n")
        
        else:
            if resp == 4:
                if n2 == 0:
                    print("\nNo se puede dividir ",n1," por cero (0)\n")
                else:
                   print(f"\nEl resultado de dividir ",n1," / ",n2," es : ",round(n1/n2,2),"\n")

            else:
                print("\nOpción no Válida\n")



