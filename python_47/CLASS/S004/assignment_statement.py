from sys import getrefcount

n = 812348643125
print(n)
print(type(n))
print(id(n))

print(getrefcount(n))
f = 1934.5678
print(f)
print(type(f))
print(id(f))
print(getrefcount(f))
b = True
print(b)
print(type(b))
print(id(b))
print(getrefcount(b))
