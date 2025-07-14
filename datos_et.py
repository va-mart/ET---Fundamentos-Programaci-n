productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0]}

# *** MENU PRINCIPAL ***
# 1. Stock marca
# 2. Busqueda por precio
# 3. Actualizar precio
# 4. Salir

def stock_codigo(codigo:str):
  for i, j in stock.items():
        if codigo.lower() == i.lower():
            print(f'El stock disponible es: {j[1]}')

def busqueda_precio(p_min, p_max):
  for modelo, marca in productos.items():
        for i, j  in stock.items():
            #print(j[0]) precio
            print(f'MARCA: {marca[0]} - MODELO: {modelo}')

busqueda_precio(300000, 400000)


def actualizar_precio(modelo:str, precio_nuevo:int):
    while True:
       for codigo, precio in stock.items():
               if codigo == modelo:  
                   precio_nuevo = precio
                   print(precio_nuevo)
                   return True
               else:
                   return False


def menu():
    while True:
        print('*** MENU PRINCIPAL ***')
        print('1. Stock código')
        print('2. Búsqueda por precio')
        print('3. Actualizar precio')
        print('4. Salir')

        try:
            opcion = int(input('Ingrese una opción: '))
            if opcion <= 0 and opcion > 4:
                print('Debe ingresar una opción entre 1 y 5.')
                continue
        except TypeError:
            print('Debe ingresar un numero entero.')
            continue

        if opcion == 1:
            codigo = input('Ingrese el código que desea buscar: ')
            stock_codigo(codigo)
        elif opcion == 2:
            print()
        elif opcion == 3:
            modelo = input('Ingrese el modelo a actualizar: ')
            precio_nuevo = int(input('Ingrese el precio nuevo: '))
            actualizar_precio(modelo, precio_nuevo)
            print(f'El precio nuevo es {precio_nuevo}')
        elif opcion == 4:
            print('Programa finalizado.')
            break

menu()