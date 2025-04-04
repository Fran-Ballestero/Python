
from math import pi, factorial, sqrt, exp, sinh, sin, cos, radians

#5  Compute the area of a triangle with base 10 and height 12. 

b = 10
h = 12

S = b*h/2
print(f'Respuesta del ejercicio 5: El área del triángulo es de {S} unidades cuadradas.')

#6. Compute the surface area and volume of a cylinder with radius 5 and height 3.

r = 5
h = 3
base = pi*r**2
face = 2*pi*r*h

S = 2*base + face
V = base*h
print(f'Respuesta del ejercicio 6: El área del cilindro es de {S} unidades cuadradas.\n'
      f'El volumen es de {V} unidades cúbicas.')

#7. Compute the slope between the points (3, 4) and (5, 9).

x1 = 3
y1 = 4
x2 = 5
y2 = 9 

slope = (y2-y1)/(x2-x1)
print(f'Respuesta del ejercicio 7: La pendiente es de {slope}.')

#8. Compute the distance between the points (3, 4) and (5, 9). 

modulo = ((x2-x1)**2+(y2-y1)**2)**0.5
print(f'Respuesta del ejercicio 8: La distancia es de {modulo}.')

#9. Use Python’s factorial function to compute 6!

f = factorial(6)
print(f'Respuesta del ejercicio 9: {f}.')

#10. Compute the number of leap years between the years 1500 and 2010

i = 1500
f = 2010
b4 = (f//4)-(i//4)
b100 = (f//100)-(i//100)
b400 = (f//400)-(i//400)

bt = b4 - b100 + b400
print(f'Respuesta del ejercicio 10: Existen {bt} años bisiestos.')

#11. Use Ramanujan’s formula for N = 0 and N = 1 to approximate π. Compare your approximation
# with Python’s stored value for π.

N = 0 
term0 = (factorial(4*0) * (1103 + 26390*0)) / ((factorial(0)**4) * (396**(4*0)))
c = (2 * sqrt(2)) / 9801

aprox0 = 1 / (c * term0)

N = 1
term1 = (factorial(4*1) * (1103 + 26390*1)) / ((factorial(1)**4) * (396**(4*1)))
sum = term0 + term1
c = (2 * sqrt(2)) / 9801
aprox1 = 1 / (c * sum)

print(f'Respuesta del ejercicio 11: Las aproximaciones con N igual 0 y 1 son {aprox0} y {aprox1} respectivamente.')

error0 = abs((pi-aprox0)/pi)*100
error1 = abs((pi-aprox1)/pi)*100
print(f'El error entre Pi y las aproximaciones calculadas son {error0}% y {error1}% para N igual 0 y 1 respectivamente.')

#12. Compute sinh for x = 2 using exponentials. 

shc = (exp(2)-exp(-2))/2
error = abs((sinh(2)-shc)/sinh(2))*100
print(f'Respuesta del ejercicio 12: El valor de sinh(2) = {sinh(2)} mientras que el calculado\
 es {shc}. El error es de {error}%.')

#13. Verify that sin2(x) + cos2(x) = 1 for x = π, π/2 , π/4 , π/6.

def propiedad_trigonométrica(x):
    return (sin(x))**2+(cos(x)**2)

valor1 = propiedad_trigonométrica(pi)
valor2 = propiedad_trigonométrica(pi/2)
valor3 = propiedad_trigonométrica(pi/4)
valor4 = propiedad_trigonométrica(pi/6)
print(f'Respuesta del ejercicio 13: Los resultados son: para Pi es {valor1}, para Pi/2 es {valor2}\
, para Pi/4 es {valor3} y para Pi/6 es {valor4}.')

#14. Compute the sin 87°.

r = sin(radians(87))
print(f'Respuesta del ejercicio 14: {r}.')