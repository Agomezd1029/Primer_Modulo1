vuelos = {
    "AV101": ("Bogota", 5, 300),
    "AV202": ("Medellin", 3, 200),
    "AV303": ("Cartagena", 4, 250),
    "AV404": ("Cali", 2, 220)
}

reservas = []

print("Bienvenido a avianca")

opcion = "si"

while opcion == "si":
    numero_vuelo = input("ingrese el id del vuelo\n")
    if numero_vuelo in vuelos:
        destino, asientos_disponibles, precio = vuelos[numero_vuelo]
        print(f"Destino: {destino}, Asientos disponibles: {asientos_disponibles}, Precio: {precio}")
        
        if asientos_disponibles > 0:
            nombre = input("Ingrese su nombre\n")
            reservas.append((nombre, numero_vuelo))
            vuelos[numero_vuelo] = (destino, asientos_disponibles - 1, precio)
            print("Reserva realizada con éxito")
        else:
            print("Lo siento, no hay asientos disponibles para este vuelo.")
    else:
        print("Número de vuelo no válido.")     


