# Aria Hdez. Negrín
print("Selecciona una opción:");
print("1. Contar > 20.");
print("2. Sumar pares 0 a 100.");
print("3. Calcular múltiplos de 3");
print("0. Salir.");
menu = int(input("Introduce el número de la opción: "));

if(menu == '1'):
    # Ejercicio 1
    # Programa que solicite 10 números por pantalla y cuente
    # cuántos son mayores de 20.

    counter = 0;
    for i in range (10):            # [0,9]
        num = int(input("Introduce un número:"))
        if num > 20:
            counter = counter + 1

    print ("Hay", counter, "números mayores de 20");
elif(menu == '2'):
    # Ejercicio 2
    # Programa que calcule la suma de todos los números pares
    # del 1 al 100.

    suma = 0;                       # variable almacenará la suma
    for num2 in range (0, 101):     # [0, 100]
        if num2 % 2 == 0:           # % es el resto de la división
            suma += num2            # suma = suma + número
    print("La suma de los números pares del 1 al 100 es", suma);
elif(menu == '3'):
    # Ejercicio 3
    # Programa que solicite dos números por pantalla y
    # calcule los múltiplos de 3 entre ellos.

    num3 = int(input("Introduce un número:"))
    num4 = int(input("Introduce otro número:"))
    # Comprobando si num3 > num4, los intercambio.
    if num3 > num4:
        num3, num4 = num4, num3
    counter2 = 0
    print("Múltiplo:")
    for n in range(num3, num4 +1):
        if (n % 3 == 0):            # multiplo de 3
            counter2 += 1           # counter = counter + 1
            print("", n)
    print("En el intervalo [", num3, ",", num4, "] hay", counter2, "múltiplos de 3");