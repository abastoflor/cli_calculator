#!/usr/bin/env python
from prettytable import PrettyTable
import os
table0 = PrettyTable()
table0.title = "Calculadora"
table0.add_column("Operador", ["+","-","*","/", "**","s", "l", "a"])
table0.add_column("Acción", ["    Suma", "   Resta", " Multip.", "División", "Potencia","   salir", " limpiar", "ayuda"])
print(table0)
memoria = ""
conta = 0
resultado = 0

while True:
    
    table = PrettyTable()
    table.title = "Calculadora"
    entrada = input("Ingrese la operación: ")
    os.system("clear")
    if entrada == "s":
        print()
        print("Programa terminado.")
        break
    elif entrada == "l":
        memoria = ""
        print(table0)
    elif entrada == "a":
        table0.add_column("Ejemplo", ["45+25", "21-220-5", "254*58*5", "100/54", "9**3", "", "", ""])
        print(table0)
    else:
        if (entrada[0].isdigit() and len(entrada) !=0) and conta > 0:
            memoria = ""
        try:
            cadena = str(memoria) + entrada
            resultado = eval(cadena)
        except:
            table.add_column(f"{entrada}", ["Operación no válida", f"|| En memoria: {resultado}  ||"])
            print(table)
        else:
            table.add_column(f"Resultado de: {cadena}", [resultado])
            memoria = str(resultado)
            print(table)
            conta += 1
            
            



