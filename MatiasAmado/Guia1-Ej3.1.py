"""
3.1 Ejercicio de programación Obligatorio su entrega: Programe un algoritmo que
resuelva este ejercicio. Contemple la posibilidad de parametrizar si los vínculos son simplex
o duplex. Elabore una nueva versión del algoritmo anterior donde se parametrice la cantidad
de dispositivos.
"""
def topologia_malla():
    print("Elija el tipo de vinculo\n Presione 1 para simplex\n Presione 2 para duplex")
    modo_transmicion = 2

    if modo_transmicion != 1 and modo_transmicion != 2:
        print("Por favor, elija una opcion valida")
        topologia_malla()

    print("Mencione la cantidad de dispositivos")
    cant_disp = 6

    if modo_transmicion == 1:
        calculo = cant_disp - 1
    
    else:
        calculo = cant_disp * (cant_disp - 1) / 2

    print(int(calculo))
topologia_malla()