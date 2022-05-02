import linkedList as lista
 
ListaMensajes = lista.LinkedList()
Positivos = lista.LinkedList()
Negativos = lista.LinkedList()
Empresas = lista.LinkedList()

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

print(normalize("¡Hólá, múndó!"))
print(normalize("¡HÓLÁ, MÚNDÓ!"))