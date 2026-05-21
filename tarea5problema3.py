# Nombre: Will Alexander Herrera
# Grupo: 213022_131
# Programa: Ingenieria de Telecomunicaciones
# Código Fuente: Autoría propia

def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        cantidad_pedir = stock_minimo - stock_actual
    else:
        cantidad_pedir = 0
    return cantidad_pedir

inventario = [
    ["001", "Televisor Smart TV 55\"", 0, 12],
    ["002", "Computador Portatil", 0, 10],
    ["003", "Celulares Inteligentes", 0, 30],
    ["004", "Ventilador de Torre", 0, 15],
    ["005", "Aire Acondicionado Inverter", 0, 8]
]


while True:
    print("==========================================")
    print(" SISTEMA DE AUDITORÍA DE INVENTARIO")
    print("==========================================\n")

    
    codigo_buscar = input("Ingrese el código del artículo a auditar (ej: 001 a 005): ")

    
    producto_encontrado = None

    
    for articulo in inventario:
        if articulo[0] == codigo_buscar:
            producto_encontrado = articulo
            break  

    print("\n------------------------------------------")

    
    if producto_encontrado is not None:
        codigo = producto_encontrado[0]
        nombre = producto_encontrado[1]
        stock_minimo = producto_encontrado[3]
        
        print(f"Artículo Encontrado: {nombre}")
        print(f"Stock Mínimo Requerido: {stock_minimo}")
        
     
        stock_actual = int(input("Ingrese el Stock Actual en existencia: "))
        
       
        cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)
        
        print("\n==========================================")
        print(" REPORTE DE REABASTECIMIENTO")
        print("==========================================")
        print("Código:", codigo)
        print("Artículo:", nombre)
        print("Stock actual registrado:", stock_actual)
        print("Stock mínimo requerido:", stock_minimo)
        print("Cantidad a pedir:", cantidad_pedir)
        print("==========================================")

    else:
       
        print("Error: El código ingresado no existe en el inventario.")
        print("==========================================")

    print("\n¿Desea auditar otro producto?")
    respuesta = input("Presione 'S' para continuar o cualquier otra tecla para salir: ").upper()
    
    
    if respuesta != "S":
        print("\n==========================================")
        print("       GRACIAS POR USAR EL SISTEMA")
        print("==========================================")
        break
        
    print("\n" * 2) 