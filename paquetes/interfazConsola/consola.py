from colorama import Fore

def menu() -> None:
	print(Fore.WHITE + '\n\t -- Menu --')
	print('1) Suma.')
	print('2) Resta.')
	print('3) Multiplicacion.')
	print('4) Division.')
	print('5) Salir.')


def pedir_int(mensaje: str) -> int:
	try:
		numero = int(input(mensaje))
		return numero
	except ValueError as e:
		raise ValueError('Ingrese una opcion valida')