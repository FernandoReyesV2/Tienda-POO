class Producto:
    def __init__(self, nombre, tipo, cantidad_actual, cantidad_minima, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad_actual = cantidad_actual
        self.cantidad_minima = cantidad_minima
        self.precio = precio

class Tienda:
    def __init__(self):
        self.productos = []
        self.ventas = [] 
        self.cantidad_ventas = []
        self.dinero_ventas = []

    def abastecer_productos(self, producto):
        for p in self.productos:
            if p.nombre == producto.nombre:
                print("Producto ya ingresado:", producto.nombre)
                print("--------------------------")
                return
        self.productos.append(producto)
        print("Producto agregado:", producto.nombre)
        print("--------------------------")

    def visualizar_productos(self):
        for producto in self.productos:
            print("Nombre:", producto.nombre)
            print("Tipo:", producto.tipo)
            print("Cantidad Actual:", producto.cantidad_actual)
            print("Cantidad Mínima:", producto.cantidad_minima)
            print("Precio:", producto.precio)
            print("--------------------------")

    def vender_producto(self, nombre_producto, cantidad):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                if producto.cantidad_actual >= cantidad:
                    iva = 0.0
                    if producto.tipo == "Papelería":
                        iva = 0.16
                    elif producto.tipo == "Supermercado":
                        iva = 0.04
                    elif producto.tipo == "Droguería":
                        iva = 0.12

                    precio_final = producto.precio * (1 + iva)
                    producto.cantidad_actual -= cantidad
                    total_final_precio = precio_final * cantidad

                    # Guardar la venta en la lista de ventas
                    self.ventas.append({"Producto": producto.nombre, "Cantidad": cantidad})
                    self.dinero_ventas.append({"Producto": producto.nombre, "Dinero": total_final_precio})

                    print("Producto vendido:", producto.nombre)
                    print("Tipo:", producto.tipo)
                    print("Precio de venta:", total_final_precio)
                    print("--------------------------")

                    return precio_final

                else:
                    print("No hay suficientes unidades del producto:", producto.nombre)
                    return 0

        print("No existe el producto:", nombre_producto)
        return 0

    def cambiar_producto(self, nombre_producto, nuevo_nombre, nuevo_tipo, nueva_cantidad_actual, nueva_cantidad_minima, nuevo_precio):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                nombre_anterior = producto.nombre  # Guardamos el nombre anterior antes de cambiarlo
                producto.nombre = nuevo_nombre
                producto.tipo = nuevo_tipo
                producto.cantidad_actual = nueva_cantidad_actual
                producto.cantidad_minima = nueva_cantidad_minima
                producto.precio = nuevo_precio
                print("Producto cambiado:", nombre_anterior) 
                print("Nuevo nombre:", producto.nombre)
                print("Nuevo tipo:", producto.tipo)
                print("Nueva cantidad actual:", producto.cantidad_actual)
                print("Nueva cantidad mínima:", producto.cantidad_minima)
                print("Nuevo precio:", producto.precio)
                print("--------------------------")
                return

        print("No existe el producto:", nombre_producto)

    def estadisticas_venta(self):
        ventas_por_producto = {}
        for venta in self.ventas:
            producto = venta["Producto"]
            cantidad = venta["Cantidad"]
            if producto in ventas_por_producto:
                ventas_por_producto[producto] += cantidad
            else:
                ventas_por_producto[producto] = cantidad

        # Encontrar producto más vendido y menos vendido
        productos_vendidos = list(ventas_por_producto.keys())
        productos_vendidos.sort(key=lambda p: ventas_por_producto[p])
        producto_mas_vendido = productos_vendidos[-1]
        producto_menos_vendido = productos_vendidos[0]
        cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]
        cantidad_menos_vendida = ventas_por_producto[producto_menos_vendido]

        # Total ventas y cantidad
        for i in ventas_por_producto:
            self.cantidad_ventas.append(ventas_por_producto[i])
        
        valor_final = 0
        for elemento in self.dinero_ventas:
            valor = elemento['Dinero']
            if isinstance(valor, (int, float)):  # Verificar que el valor sea numérico
                valor_final += valor
        
        total_cantidad_ventas=sum(self.cantidad_ventas)
        print("Total dinero vendido", valor_final)
        print("Total cantidad vendida:", total_cantidad_ventas)
        print("Producto más vendido:", producto_mas_vendido)
        print("Cantidad vendida:", cantidad_mas_vendida)
        print("Producto menos vendido:", producto_menos_vendido)
        print("Cantidad vendida:", cantidad_menos_vendida)

print("--------------------------")
# Crear una instancia de Producto
producto1 = Producto("Lápiz", "Papelería", 50, 10, 10)
producto2 = Producto("Arroz", "Supermercado", 50, 10, 10)
producto3 = Producto("Paracetamol", "Droguería", 50, 10, 10)

# Crear una instancia de Tienda
tienda = Tienda()

# Agregar los productos a la tienda
tienda.abastecer_productos(producto1)
tienda.abastecer_productos(producto2)
tienda.abastecer_productos(producto3)

# Mostrar los productos de la tienda
tienda.visualizar_productos()

# Vender productos
tienda.vender_producto("Lápiz", 3)
tienda.vender_producto("Paracetamol", 6)

# Cambiar un producto
tienda.cambiar_producto("Lápiz", "Bolígrafo", "Papelería", 30, 5, 5)

# Mostrar las estadísticas de venta
tienda.estadisticas_venta()
