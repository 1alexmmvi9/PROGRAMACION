# Programa del piano
# v0.1 Alex Sytnyk
# Representa un piano con objetos predeterminados de Python

# Creamos el objeto
piano = {
    "marca": "Yamaha",
    "color": "negro",
    "precio": 1200,
    "melodia_actual": None
}

# Función para tocar una melodía
def tocarMelodia(piano_objeto, melodia):
    duracion = 5  # variable local
    print(f"El piano está tocando la melodía: {melodia} durante {duracion} segundos.")
    piano_objeto["melodia_actual"] = melodia

# Función para mostrar detalles
def mostrarDetalles(piano_objeto):
    print("=== Detalles del Piano ===")
    print("Marca:", piano_objeto["marca"])
    print("Color:", piano_objeto["color"])
    print("Precio:", piano_objeto["precio"], "€")
    print("Melodía actual:", piano_objeto["melodia_actual"])

# Ejemplo de uso
mostrarDetalles(piano)
tocarMelodia(piano, "Drowning love")
mostrarDetalles(piano)
