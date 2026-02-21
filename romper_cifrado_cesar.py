import string

# Alfabeto ampliado: letras minúsculas + mayúsculas + dígitos
ALFABETO = string.ascii_lowercase + string.ascii_uppercase + string.digits

def algoritmo_descifrado(texto_cifrado, clave, direccion):
    texto_plano = ""
    longitud = len(ALFABETO)
    
    for caracter in texto_cifrado:
        if caracter in ALFABETO:
            indice = ALFABETO.index(caracter)
            if direccion == "izquierda":
                nuevo_indice = (indice - clave) % longitud
            else:  # derecha
                nuevo_indice = (indice + clave) % longitud
            texto_plano += ALFABETO[nuevo_indice]
        else:
            texto_plano += caracter
    return texto_plano

if __name__ == "__main__":
    texto_cifrado = input("Ingresa el mensaje cifrado: ")
    clave = int(input("Ingresa la clave de salto (número entero): "))
    
    # Mostrar resultados con ambas direcciones
    for direccion in ["izquierda", "derecha"]:
        texto_descifrado = algoritmo_descifrado(texto_cifrado, clave, direccion)
        print(f"Dirección: {direccion}, Saltos: {clave}, Texto: {texto_descifrado}")
