n = int(input())
h = n//3600
r = n%3600
m = r//60
s = r%60
print(f"{h:.0f}:{m:.0f}:{s:.0f}")