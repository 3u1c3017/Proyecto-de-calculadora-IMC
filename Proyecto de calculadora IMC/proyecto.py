## Aqui es donde  obtenemos la calculadora de IMC ##  
print("Bienvenidos a la calculadora de IMC")
RESET = '\033[0m'
BOLD = '\033[1m' 
BLUE = '\033[94m'
CYAN = '\033[36m'
UNDERLINE = '\033[4m' 
YELLOW = '\033[33m'
GREEN_LIGHT = '\033[92m'
GREEN = '\033[32m'
RED_LIGHT = '\033[91m'
RED = '\033[31m'

## Saludo al usuario ##
Nombre= input("Ingresar nombre completo: \n")
print("Hola",Nombre,"Espero que te encuentres bien")
print("\tA continuacion necesitare tu Edad,Altura y Peso  para poder continuar")

## Recoleccion de datos ##
Edad= int(input("Ingresa tu edad en años: \n"))
Altura= float(input("Ingresa tu estatura (en metros): \n"))
Peso= float(input("Ingresa tu peso (en kilos): \n"))
IMC= Peso/Altura**2

## Datos recolectados ##
print(f"Tiene {Edad} años")
print(f"Tu nombre completo es: {Nombre}")
print(f"Mides {Altura} metros")
print(f"Pesas {Peso} kilogramos")
print(f"\tCon los datos obtenidos podemos calcular que tu IMC es: { IMC: .2F}")
print("Por lo tanto quiere decir que;\n")


if IMC <= 18.5:
    print("Te encuentras en un peso bajo")
    print("Consumir alimentos nutritivos y ricos en calorias es una buena forma de ganar peso")
    print(f"{GREEN_LIGHT}Consumir alimentos nutritivos y ricos en calorias es una buena forma de ganar peso{RESET}")
elif 18.5 <=IMC <= 24.9:
    print("Te encuentra en forma y en peso ideal")
    print("Exelente, tiene un peso ideal!!")
    print(f"{GREEN} Exelente, tiene un peso ideal!!{RESET}")
elif 25 <= IMC <= 29.9:
    print("Te encuentras en sobre peso,adelgasa un poco")
    print("No hay cambio de peso,sin un cambio de habito alimenticio")
    print(f"{GREEN}No hay cambio de peso,sin un cambio de habito alimenticio{RESET}")
elif 30 <= IMC <= 34.9:
    print("Te encuentras en obesidad fase #1")
    print("No se trata de perder peso, se trata de estar saludable primero")
    print(f"{RED_LIGHT}No se trata de perder peso, se trata de estar saludable primero{RESET}")
elif 35 <= IMC <=39.9:
    print("Te encuentras en obesidad fase #2")
    print("El ejerciocio es una de las maneras de prevenir el rapido crecimiento de la obesidad")
    print(f"{RED_LIGHT}El ejerciocio es una de las maneras de prevenir el rapido crecimiento de la obesidad{RESET}")
elif IMC >= 40:
    print("Te encuentras en obesidad fase #3")
    print("La decisión de perder peso refleja un compromiso contigo mismo y con tu bienestar")
    print(f"{RED} La decisión de perder peso refleja un compromiso contigo mismo y con tu bienestar.{RESET}")

print()
print("Gracias", Nombre, "por usar nuestra calculadora IMC!")
print(f"{YELLOW}Gracias", Nombre, f"{YELLOW}por usar nuestra calculadora IMC!{RESET}")
      
      