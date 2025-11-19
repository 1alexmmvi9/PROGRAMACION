import mysql.connector

conexion = mysql.connector.connect(
    host ="localhost"
    user ="usuario_portafolio"
    password ="662046"
    database ="portafolioexamen"
)
cursor = conexion.cursor()

print("Bienvenidos al CRUD de piezasportafolio!")

while True:
    print("\n1. Crear\n2. Leer\n3. Actualizar\n4. Eliminar\n5. Salir")
    opcion = input("Elige opcion: ")

    if opcion == "1":
        t = input("Título: ")
        d = input("Descripción: ")
        f = input("Fecha: ")
        c = input("ID Categoría: ")

    elif opcion == "2":
        cursor.execute("SELECT * FROM piezasportafolio")
        for x in cursor.fetchall():
            print(x)

    elif opcion == "3":
        i = input("ID a actualizar: ")
        t = input("Nuevo titulo: ")
        d = input("Nueva descripcion: ")
        cursor.execute("UPDATE piezasportafolio SET titulo=%s, descripcion=%s WHERE identificators=%s", (t, d, i))
        conexion.commit()
        print("Registro actualizado")

    elif opcion == "4":
        i = input("ID a eliminar: ")
        cursor.execute("DELETE FROM piezasportafolio WHERE Identificador=%s",(i,))
        conexion.commit()
        print("Registro elimininado")

    elif opcion == "5":
        break
    else:
        print("Opcion invalida")
cursor.close()
conexion.close()


