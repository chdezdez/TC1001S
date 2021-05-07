import os
import Filtros
import Camara
def menu():
    os.system('cls')
    print("selecciona una opcion")
    print("\t1 - filtro 1")
    print("\t2 - filtro 2")
    print("\t3 - filtro 3")
    print("\t4 - filtro 4")
    print("\t5 - salir")
foto = Camara.tomarFoto();
while True:
    menu()
    opcion = input("inserta un numero valor >> ")

    if opcion =="1":
        foto = Filtros.filtroBN(foto);
    elif opcion == "2":
        foto = Filtros.filtroDifuminar(foto);
    elif opcion == "3":
        foto = Filtros.filtroEspejo(foto);
    elif opcion == "4":
        foto = Filtros.filtroContraste(foto);
    elif opcion == "5":
        break
    else:
        print("no has seleccionado ninguna opcion correcta")
        break
