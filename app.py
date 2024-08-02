from colorama import Fore, Style

def main() -> None:
	print(Fore.WHITE + 'Pueba con color blanco')
	print(Fore.BLUE + f'Pueba con color azul al numero {35}')
	print(Style.RESET_ALL + 'Reestablecido el estilode letra or defecto')

if __name__ == '__main__':
	main()