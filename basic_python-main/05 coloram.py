'''
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''

from colorama import Fore, Back, Style, init
init(autoreset=True) #para resetear formato despues del texto

texto = 'Este es el texto'

print(Fore.RED + texto) #Texto
print(Back.GREEN + texto) #Fondo
print(Style.DIM + texto) #Estilos
print(Style.RESET_ALL)

#Estilos
print(Style.DIM + 'Estilo DIM -->  ' + texto)
print(Style.RESET_ALL)

print(Back.RED + Style.NORMAL + 'Estilo NORMAL -->  ' + texto + Back.RESET) #reseteo al usarlo
print(Style.RESET_ALL)

print(Fore.RED + Style.BRIGHT + 'Estilo BRIGHT --> ' + texto)
print(Style.RESET_ALL)

