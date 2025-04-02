def clasificar_numeros():
    positivos = []
    negativos = []
    
    while True:
        try:
            numero = int(input("Ingrese un número entero (0 para terminar): "))
            if numero == 0:
                break  
            elif numero > 0:
                positivos.append(numero)
            else:
                negativos.append(numero)
        except ValueError:
            print(" Error: Debe ingresar un número entero válido.")
    
    resultado = {
        "positivos": len(positivos),
        "negativos": len(negativos)
    }
    
    return resultado


resultado_final = clasificar_numeros()
print("\n Resultados:")
print(resultado_final)
