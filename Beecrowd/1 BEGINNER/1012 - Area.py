data = input().split(" ")
A = float(data[0])
B = float(data[1])
C = float(data[2])
TRIANGULO = 0.5*A*C
CIRCULO = 3.14159*C**2
TRAPEZIO = ((A+B)/2)*C
QUADRADO = B*B
RETANGULO = A*B
TRIANGULO = "{:.3f}".format(TRIANGULO)
CIRCULO = "{:.3f}".format(CIRCULO)
TRAPEZIO = "{:.3f}".format(TRAPEZIO)
QUADRADO = "{:.3f}".format(QUADRADO)
RETANGULO = "{:.3f}".format(RETANGULO)
print("TRIANGULO:",TRIANGULO)
print("CIRCULO:",CIRCULO)
print("TRAPEZIO:",TRAPEZIO)
print("QUADRADO:",QUADRADO)
print("RETANGULO:",RETANGULO)