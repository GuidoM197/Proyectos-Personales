from random import choices

LOWER_K = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

UPPER_K = [x.upper() for x in LOWER_K]

NUMBERS = [str(x) for x in range(0, 10)]

SPECIALS = ['@', '!', '¡', '?', '¿', '&', '$', '#',]

PATH = 'contraseñas.csv'

def generador_de_contraseña(): # Genera una contrseña aleatoria con 3 mayusculas, 3 minusculas, 3 numeros y 3 caracteres especiales.
    password = ''

    for _ in range(3): 
        elegido_1 = choices(UPPER_K)
        elegido_2 = choices(LOWER_K)
        elegido_3 = choices(NUMBERS)
        elegido_4 = choices(SPECIALS)

        password += elegido_1[0] + elegido_2[0] + elegido_3[0] + elegido_4[0]
    
    password = ''.join(password)

    return password

def guardado_de_datos(paltaforma): # Guarda en 'contraseñas.csv' la plataforma con su respectiva contraseña.

    with open(PATH, 'a') as file:
        file.write(f'{paltaforma};{generador_de_contraseña()}\n')

def reconocimiento_de_existencia(plataforma):
    plataforma_existente = False
    contraseña = None

    with open(PATH) as file:

        next(file)

        for linea in file:
            linea = linea.split(';')

            if linea[0] == plataforma:
                plataforma_existente = True
                contraseña = linea[1]
            
    return plataforma_existente, contraseña

def cambio_de_contraseña(plataforma):

    cuentas = {}

    with open(PATH) as viejo:
        next(viejo)

        for linea in viejo:
            linea = linea.split(';')

            cuentas[linea[0]] = cuentas.get(linea[0], linea[1])

        cuentas[plataforma] = generador_de_contraseña()

    with open(PATH, 'w') as nuevo:
        
        nuevo.write('Plataforma;Contraseña \n')

        for key, value in cuentas.items():

            nuevo.write(f'{key};{value} \n')