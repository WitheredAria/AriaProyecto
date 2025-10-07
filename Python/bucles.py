# BUCLES FOR X IN RANGE:
# Muestra en pantalla números del 0 al 7.
for num1 in range (8):
    print ("Primer bucle:", num1);
# Muestra en pantalla números del 5 al 8.
for num2 in range (5, 9):
    print ("Segundo bucle:", num2);
# Muestra en pantalla números del 4 al 11 en serie de 2 (4, 6, 8...).
for num3 in range (4, 12, 2):
    print ("Tercer bucle:", num3);
# Muestra en pantalla números del 12 al 3 en serie de 2 hacia atrás (12, 10, 8...).
for num4 in range (12, 4, -2):
    print ("Cuarto bucle:", num4);

# BUCLES WHILE:
# Muestra en pantalla números del 0 al 7.
i = 0
while i < 8:
    print("Primer bucle:", i)
    i = i + 1;
# Muestra en pantalla números del 5 al 8.
i = 5
while i < 9:
    print("Segundo bucle:", i)
    i = i + 1;
# Muestra en pantalla números del 4 al 11 en serie de 2 (4, 6, 8...).
i = 4
while i < 12:
    print("Tercer bucle:", i)
    i = i + 2;
# Muestra en pantalla números del 12 al 3 en serie de 2 hacia atrás (12, 10, 8...).
i = 12
while i > 4:
    print("Cuarto bucle:", i)
    i = i - 2;

# BUCLES FOR X IN RANGE CON BREAK Y CONTINUE:
# Muestra en pantalla números del 0 al 7. Si llega al 4, rompe el bucle.
for i in range(8):
    if i == 4:
        break
    print("Salto break:", i);
# Muestra en pantalla números del 0 al 7. Si llega al 4, continua el bucle saltándoselo.
for i in range(8):
    if i == 4:
        continue
    print ("Salto continue:", i);