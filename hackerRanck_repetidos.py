"""
 Function that returns how many letter are repeted in the string 
"""

def print_repetido(name):
    # Use a breakpoint in the code line below to debug your script.
    l = list(name)
    cadena = ''
    c = 1
    for (k, v) in enumerate(name):
        li = l[:k + 1]
        if len(li) == 1:
            cadena += v
        if li[k] == li[k - 1] and len(li) != 1:
            c += 1
        if li[k] == li[k - 1] and len(li) == len(name):
            cadena += str(c)
            break
        if li[k] != li[k - 1] or len(li) == len(name):
            if c > 1:
                cadena += str(c)
                cadena += v
                c = 1
            else:
                cadena += v

print(cadena)

if __name__ == '__main__':
    print_repetido('abbcc')

#example of intput and output
#input abbcc
#output ab2c2