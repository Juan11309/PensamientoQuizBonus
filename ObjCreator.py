print("Este programa es para gráficar objetos 3D teniendo definiendo los vertices y las caras")

def menu ():
  print ("""
    ---------------------------------------------------------------------
    1. Ingresar numero de vertices.
    2. Ingrese las coordenadas del vertice.
    3. Ingrese el numero de caras.
    4. Ingrese la cantidad de vertices para las caras.
    5. Ingrese los indices de las caras.
    6. Imprimir el programa.
    7. Salir del programa.
    ---------------------------------------------------------------------- 
         """)

menu()
while True:
    seleccion_usr = int(input("Seleccione un numero para acceder al menu: "))

    if seleccion_usr == 1:   
        while True:
            try:
                vertices_totales = int(input("Ingrese la cantidad de vértices: "))
                break
            except ValueError:
                print("Error: Ingrese un valor numerico entero")
    menu()       
    if seleccion_usr == 2:
        vertices = [] # Guardar todos los vertices
        for i in range(vertices_totales):
            while True:
                coordenadas_vertice = input(f"Ingrese las coordenas del vértice {i+1} (x y z): ")
                try:
                    x, y, z = map(int, coordenadas_vertice.split())
                    vertices.append((x, y, z))
                    break
                except ValueError:
                    print("Error: Ingresa unicamente valores numericos enteros separados por un espacio")
    menu()
    if seleccion_usr == 3: 
        while True:
            try:
                caras_totales = int(input("Ingrese la cantidad de caras: "))
                break
            except ValueError:
                print("Error: Ingrese un valor numerico entero")

    menu()
    if seleccion_usr == 4:
        caras = []
        for i in range(caras_totales):
            while True:
                try:
                    caras_vertices = int(input(f"Ingrese la cantidad de vertices para la cara {i+1}: "))
                    break
                except ValueError:
                    print("Eror: Ingresa un valor numerico entero.")
    menu()
    if seleccion_usr == 5:
        while True:
            caras_indices = input(f"Ingrese los indices de lo vertices a unir para la cara {i+1}: ")
            try:
                indices_lista = list(map(int, caras_indices.split()))
                caras.append(indices_lista)
                break
            except ValueError:
                print(f"Error: Ingrese {caras_vertices} valores numericos separados por espacios")  #caras.append(indices_lista)

# Impresión en formato .obj
    menu ()
    if seleccion_usr == 6:
        print("Salida en formato .obj:")
        for v in vertices:
                print("v", v[0], v[1], v[2])
    
        for cara in caras:
    # Se convierte la lista de índices a cadena
            indices = " ".join(map(str, cara))
            print("f", indices)
    
            print(indices)
    menu ()
    if seleccion_usr >=7:
        break
    
