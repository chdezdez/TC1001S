import os
import filtros
import camara

def menu():
    os.system('cls')
    print("Selecciona una opcion:")
    print("\t1 - blanco y negro")
    print("\t2 - difuminar")
    print("\t3 - espejo horizontal")
    print("\t4 - subir contraste")
    print("\t5 - salir")

# Con ENTER se captura la foto, y con otro ENTER se guarda.
foto = camara.tomarFoto();

while True:
    menu()
    opcion = input("Inserta un numero valor >> ")
    if opcion =="1":
        foto = filtros.filtroBN(foto);
    elif opcion == "2":
        foto = filtros.filtroDifuminar(foto);
    elif opcion == "3":
        foto = filtros.filtroEspejo(foto);
    elif opcion == "4":
        foto = filtros.filtroContraste(foto);
    elif opcion == "5":
        break
    else:
        print("No has seleccionado ninguna opcion correcta.")
