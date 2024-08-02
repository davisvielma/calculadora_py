from colorama import Fore

def menu() -> None:
	print(Fore.WHITE + '\n\t -- Menu --')
	print('1) Suma.')
	print('2) Resta.')
	print('3) Multiplicacion.')
	print('4) Division.')
	print('5) Salir.')


def pedir_numero(mensaje: str) -> int:
	numero = input(mensaje)

	if not numero.isdigit():
		raise ValueError('Ingrese un numero positivo')

	return int(numero)