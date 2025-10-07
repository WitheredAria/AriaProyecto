x= int(input (" Introduce un número: "));
y= int(input ("Introduce otro número: "));
operacion = '1';
while (operacion != '0'):
    print ("Selecciona una operación:");
    print ("1. Suma");
    print ("2. Resta");
    print ("3. Multiplicación");
    print ("4. División");
    print ("0. Salir");
    operacion = input ("Introduce el número de la operación: ");

    if (operacion == '1'):
    # Operación suma
        suma = x + y;
        print ("Total suma = ", suma);
    elif (operacion == '2'):
    # Operación resta
        resta = x - y;
        print ("Total resta = ", resta);
    elif (operacion == '3'):
    # Operación multiplicación
        mult = x * y;
        print ("Total multiplicación = ", mult);
    elif (operacion == '4'):
    # Operación división
        div = x / y;
        print ("Total división = ", div);