# Aria Hdez. Negrín

print("Selecciona una opción:");
print("1. Media.");
print("2. Área y perímetro.");
print("3. Concatenar.");
print("0. Salir.");
menu = input("Introduce el número de la opción: ");

if(menu == '1'):
    # Ejercicio 1
    # Muestra una advertencia al usuario de lo que tendrá que introducir
    print("Introduce tres números siguiendo las instrucciones de abajo paso a paso.");
    # Se pide al usuario introducir números que se almacenarán en los respectivos valores
    num1 = int(input("Introduce un número: "));
    num2 = int(input("Introduce un segundo número: "));
    num3 = int(input("Introduce un tercer número: "));
    # Operación que calcula la media entre los tres valores introducidos
    media = (num1 + num2 + num3) / 3;
    # Muestra el resultado de la operación
    print("La media de los números introducidos es de", media);
elif(menu == '2'):
    # Ejercicio 2
    # Muestra una advertencia al usuario de lo que tendrá que introducir
    print("Introduce la base y la altura del rectángulo para calcular su área y perímetro.");
    # Se pide al usuario introducir las medidas de base y altura del rectángulo que se almacenarán en los respectivos valores
    base = float(input("Introduce la base del rectángulo: "));
    altura = float(input("Introduce la altura del rectángulo: "));
    # Operación que calcula el área
    A = base * altura;
    # Operación que calcula el perímetro
    P = 2 * (base + altura);
    # Muestra el resultado de las operaciones
    print("El rectángulo tiene un área de", A, "y un perímetro de", P);
elif(menu == '3'):
    # Ejercicio 3
    # Muestra una advertencia al usuario de lo que tendrá que introducir
    print("Introduce dos frases a concatenar.");
    # Se pide al usuario introducir frases que se almacenarán en los respectivos valores
    frase1 = input("Introduce una frase: ");
    frase2 = input("Introduce otra frase: ");
    # Operación que unirtá las frases
    frase3 = frase1 + " " + frase2;
    # Muestra la frase concatenada
    print(frase3);