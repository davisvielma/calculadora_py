from colorama import Fore, Style
from paquetes.interfazConsola.consola import menu, pedir_int, pedir_float, mostrar_resultado
from paquetes.operacionesBasicas.operaciones import sumar, restar, multiplicar, dividir

def main() -> None:
	opcion = 0
	rango_inferior = 1
	rango_superior = 5

	print(Fore.WHITE + '\n\t\tBienvenido a la calculadora')

	while opcion != rango_superior:
		try:
			menu()
			opcion = pedir_int('*Elija una opcion: ')

			if opcion < rango_inferior or opcion > rango_superior:
				raise ValueError(f'Ingrese una opcion entre {rango_inferior} y {rango_superior}')

			if opcion == 1:
				num1 = pedir_float('\n*Escriba el primer numero a sumar: ')
				num2 = pedir_float('*Escriba el segundo numero a sumar: ')
				resultado = sumar(num1, num2)

				mostrar_resultado(resultado)
			elif opcion == 2:
				num1 = pedir_float('\n*Escriba el primer numero a restar: ')
				num2 = pedir_float('*Escriba el segundo numero a restar: ')
				resultado = restar(num1, num2)

				mostrar_resultado(resultado)
			elif opcion == 3:
				num1 = pedir_float('\n*Escriba el primer numero a multiplicar: ')
				num2 = pedir_float('*Escriba el segundo numero a multiplicar: ')
				resultado = multiplicar(num1, num2)

				mostrar_resultado(resultado)
			elif opcion == 4:
				num1 = pedir_float('\n*Escriba el numerador: ')
				num2 = pedir_float('*Escriba el denominador: ')
				resultado = dividir(num1, num2)

				mostrar_resultado(resultado)
		except ValueError as e:
			print(Fore.RED)
			print(f'Error!!! {e}.')


if __name__ == '__main__':
	main()