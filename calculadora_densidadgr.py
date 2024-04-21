def densidad(masa, volumen):
    return masa / volumen


masa = int(input("escribe el valor de masa:"))

while masa < 0:
    print("ERROR escribe de nuevo la masa")
    masa = int(input("escribe el valor de masa:"))

volumen = int(input("escribe el valor de volumen:"))

while volumen < 0:
    print("ERROR escribe de nuevo el volumen")
    volumen = int(input("escribe el valor de volumen:"))


resultado_densidad = densidad(masa, volumen)


print("la densidad es:", resultado_densidad, "g/cm3")
