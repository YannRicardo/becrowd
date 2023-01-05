A,B,C = map(float,input().split())
r1 = (A*C)/2 
r2 = 3.14159 * C**2
r3 = ((A+B) * C)/2
r4 = B**2
r5 = A * B
print(f'TRIANGULO: {r1:.3f}')
print(f'CIRCULO: {r2:.3f}')
print(f'TRAPEZIO: {r3:.3f}')
print(f'QUADRADO: {r4:.3f}')
print(f'RETANGULO: {r5:.3f}')