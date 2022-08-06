def new_password(a,b):
    cadena = ''
    c = 0
    for (k, v) in enumerate(a):
        li = b[:k + 1]
        cadena += f"{v}"
        cadena += f"{li[k]}"
        c = len(li)
    if len(a) < len(b):
        aux = b[len(b) - c:]
        cadena += aux
    print(cadena)

if __name__ == '__main__':
    new_password('cat', 'rabbit')

#input a='cat' b='rabbit'
#output craatbbit

#input a='abc' b='def'
#output adbecf