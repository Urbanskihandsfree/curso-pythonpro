"""

9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    C = 5 * ((F-32) / 9).

"""
import math

F = float(input('Informe a temperatura em graus Fahrenheit: '))

C = 5 * ((F-32) / 9) 

print(f'Temperatura em graus Celsius: {math.floor(C)}')
