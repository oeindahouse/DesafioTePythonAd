from te import Te

# if __name__ == "__main__":
#     # te_instancia = Te()
#     # sabor_elegido = input("ingrese el sabor de te (te negro, te verde, agua de hierbas): ")
#     # formato_elegido = input("ingrese el formato de té (300gr o 500gr): ")

#     # resultado = te_instancia.obtener_datos_tea(sabor_elegido, formato_elegido)
#     te_instancia = Te()
    
#     # Solicitar al usuario que ingrese el número de sabor (1, 2 o 3)
#     sabor_numero = int(input("Ingrese el número de sabor (1: te negro, 2:te verde, 3: Agua de hierbas): "))

#     resultado = Te.obtener_datos_por_sabor(sabor_numero)
#     print(resultado)

if __name__ == "__main__":
    te_instancia = Te()

    #ingresar el num de formato (0-1)
    formato_numero = int(input("ingrese el num de formato (0: 300gr, 1: 500gr): "))

    resultado = Te.precio_formato(formato_numero)
    print(resultado)