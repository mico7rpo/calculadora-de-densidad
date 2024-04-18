def densidad(masa, volumen):
    return masa / volumen

masa = int(input("escribe el valor de masa:"))
volumen = int(input("escribe el valor de volumen:"))

print("la densidad es:", densidad(masa, volumen))