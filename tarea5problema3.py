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

inventario = []

print("==========================================")
print(" SISTEMA DE AUDITORÍA DE INVENTARIO")
print("==========================================\n")

cantidad_articulos = int(input("Ingrese la cantidad de artículos: "))

for i in range(cantidad_articulos):

    print(f"\nArtículo #{i + 1}")

    codigo = input("Ingrese el código del artículo: ")
    nombre = input("Ingrese el nombre del artículo: ")
    stock_actual = int(input("Ingrese el stock actual: "))
    stock_minimo = int(input("Ingrese el stock mínimo: "))

    inventario.append([
        codigo,
        nombre,
        stock_actual,
        stock_minimo
    ])


print("\n==========================================")
print(" REPORTE DE REABASTECIMIENTO")
print("==========================================")

for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad_pedir = calcular_pedido(
        stock_actual,
        stock_minimo
    )

    print("\n------------------------------------------")
    print("Código:", codigo)
    print("Artículo:", nombre)
    print("Stock actual:", stock_actual)
    print("Stock mínimo:", stock_minimo)
    print("Cantidad a pedir:", cantidad_pedir)

print("\n==========================================")
print(" FIN DEL REPORTE")
print("==========================================")

input("\nPresione Enter para finalizar...")