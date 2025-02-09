import os
import time
import random
from colorama import Fore, init

init(autoreset=True)

print("---------------------------------")
print("¡Bienvenido(a) a las adivinanzas!")
print("---------------------------------")

while True:

    num_limit = int(input("Establece el rango númerico limite: "))

    if num_limit <= 0:
        print(f"{Fore.RED}Escribe un valor mayor a cero.")      
    else:
        num_random = random.randint(0,num_limit)
        attemps = 0

        while True:
            attemp_user = int(input("Intenta adivinar el número secreto, ingresa un valor: "))
            attemps += 1

            if attemp_user == num_random:
                os.system("cls")
                print("--------------------------")
                print(f"{Fore.GREEN}¡Lo adivinaste, gooood!")
                break
            elif attemp_user > num_random:
                print(f"{Fore.YELLOW}Estás por encima del número secreto...")
            else:
                print(f"{Fore.YELLOW}Estás por debajo del número secreto...")
        print(f"Necesitaste {attemps} intento(s).")
        print("--------------------------")
        time.sleep(3)
        break