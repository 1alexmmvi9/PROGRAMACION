# Actividad: Uso de aserciones en Python
# Autor: Alex Sytnyk

try:
    numero = int(input("Introduce un número mayor que 10: "))
    assert numero > 10, "El número no es mayor que 10"
    print("La aserción se ha cumplido correctamente. El número es válido.")
except AssertionError as error:
    print("Error:", error)
except ValueError:
    print("Debes introducir un número válido.")
