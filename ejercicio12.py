secreto = 7 
intento = int(input("Adivina el número (1 al 10): ")) 
while intento != secreto: 
    if intento < secreto: 
        print("muy lejos") 
    else: 
        print("muy cerca") 
    intento = int(input("Intenta de nuevo: ")) 
print("Acertaste") 