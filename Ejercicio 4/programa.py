def generar_tabla(n):
    if n < 1 or n > 10:
        mensaje = 'El numero debe estar entre 1 y 10.'
        return mensaje
    else:
        with open(f'tabla-{n}.txt', 'w') as tabla:
            for i in range(1,11):
                resultado = n * i
                tabla.write(f"{n} x {i} = {resultado}\n")
        print(f"La tabla de multiplicar del número {n} ha sido guardada en el archivo tabla-{n}.txt.")

def mostrar_tabla(n):
    if n < 1 or n > 10:
        mensaje = 'El numero debe estar entre 1 y 10.'
        return mensaje
    else:
        try:
            with open(f'tabla-{n}.txt', 'r') as tabla:
                contenido = tabla.read()
                print(f'La tabla de multiplicar de {n} es: ')
                print(contenido)
        except FileNotFoundError:
            print(f'Tabla de multiplicar no encontrado.')

def mostrar_linea(n, m):
    if n < 1 or n > 10:
        mensaje = 'El numero debe estar entre 1 y 10.'
        return mensaje
    try:
        with open(f'tabla-{n}.txt', 'r') as tabla:
            lineas = tabla.readlines()
            if m < 1 or m > len(lineas):
                mensaje = 'Numero de lineas no es valido.'
                return mensaje
            else:
                print(f"Línea {m} de la tabla de multiplicar del número {n}:")
                print(lineas[m - 1].rstrip())
    except FileNotFoundError:
        print(f"El archivo tabla-{n}.txt no existe.")     

def menu():
    while True:
        print('Bienvenidos al menu')
        print('1. Generar y guardar tabla de multiplicar')
        print('2. Mostrar tabla de multiplicar')
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            numero = int(input("Ingrese un número entre 1 y 10: "))
            generar_tabla(numero)
        elif opcion == 2:
            numero = int(input("Ingrese un número entre 1 y 10: "))
            mostrar_tabla(numero)
        elif opcion == 3:
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea: "))
            mostrar_linea(numero, linea)
        elif opcion == 4:
            print('Gracias por su visita.')
            break
        else:
            print('Error. Por favor, seleccione una opción válida.')


num = menu()
print(menu)








