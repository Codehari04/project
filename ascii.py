def ASCII(x):
    if type(x)==str:
        return ord(x)
    return x
l=["A",-20,"a",89,45]
l.sort(key=ASCII)
print(l)