n = int(input())
h = n/3600
r  = n%3600
m = r/60
s = m/60
print("%d:%i:%i",(h,m,s))