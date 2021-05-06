import os

def menu():
	os.system('cls')
	print("selecciona una opcion")
	print("\t1 - filtro 1")
	print("\t2 - filtro 2")
	print("\t3 - filtro 3")
	print("\t4 - filtro 4")
	print("\t5 - salir")

while True:
	menu()
	opcion = input("inserta un numero valor >> ")

	if opcion =="1":
		#poner el filtro1
	elif opcion == "2":
		#poner el filtro2
	elif opcion == "3":
		#poner el filtro3
	elif opcion == "4":
		#poner el filtro4
	elif opcion == "5":
		break
	else:
		print("no has seleccionado ninguna opcion correcta")
		break
		