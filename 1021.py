n = float(input())
cem = cinquenta = vinte = dez = cinco = dois = um = 0
cincents = vintecents = dezcents = cincocents = cents = 0
n = float(f"{n:.2f}")
if int(n/100) >= 1:
    cem = int(n/100)
    n -= cem*100

n = float(f"{n:.2f}")
if int(n/50) >= 1:
    cinquenta = int(n/50)
    n -= cinquenta*50

n = float(f"{n:.2f}")
if int(n/20) >= 1:
    vinte = int(n/20)
    n -= vinte*20

n = float(f"{n:.2f}")
if int(n/10) >= 1:
    dez = int(n/10)
    n -= dez*10

n = float(f"{n:.2f}")
if int(n/5) >= 1:
    cinco = int(n/5)
    n -= cinco*5

n = float(f"{n:.2f}")
if int(n/2) >= 1:
    dois = int(n/2)
    n -= dois*2

n = float(f"{n:.2f}")
if int(n/1) >= 1:
    um = int(n/1)
    n -= um*1

n = float(f"{n:.2f}")
if int(n/0.50) >= 1:
    cincents = int(n/0.50)
    n -= cincents*0.50

n = float(f"{n:.2f}")
if int(n/0.25) >= 1:
    vintecents = int(n/0.25)
    n -= vintecents*0.25

n = float(f"{n:.2f}")
if int(n/0.10) >= 1:
    dezcents = int(n/0.10)
    n -= dezcents*0.10
    
n = float(f"{n:.2f}")
if int(n/0.05) >= 1:
    cincocents = int(n/0.05)
    n -= cincocents*0.05

n = float(f"{n:.2f}")
if int(n/0.01) >= 0.998:
    cents = int(n/0.01)
    n -= cents*0.01

print("NOTAS:")
print(f"%d nota(s) de R$ {cem:.2f}")
print(f"%d nota(s) de R$ {cinquenta:.2f}")
print(f"%d nota(s) de R$ {vinte:.2f}")
print(f"%d nota(s) de R$ {dez:.2f}")
print(f"%d nota(s) de R$ {cinco:.2f}")
print(f"%d nota(s) de R$ {dois:.2f}")

print("MOEDAS:")
print(f"%d nota(s) de R$ {um:.2f}")
print(f"%d nota(s) de R$ {cincents:.2f}")
print(f"%d nota(s) de R$ {vintecents:.2f}")
print(f"%d nota(s) de R$ {dezcents:.2f}")
print(f"%d nota(s) de R$ {cincocents:.2f}")
print(f"%d nota(s) de R$ {cents:.2f}")