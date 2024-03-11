from Logica import logica

def main():

    while True:

        opcion = input('Ingrese una opcion: \n 1. Gestionar contraseña. \n 2. Salir. \n \n')
        
        if opcion == '2':
            print('\nHasta luego! \n')
            return

        else:

            plataforma = input('\nDe que plataforma desea hacer gestion la contraseña? \n')

            plataforma_existe, contraseña = logica.reconocimiento_de_existencia(plataforma.lower())

            opcion_gestion = input(f'Ingrese una opcion: \n 1. Ver contraseña de {plataforma}. \n 2. Crear contraseña para {plataforma}. \n 3. Cambiar contraseña de {plataforma}. \n \n')

            if opcion_gestion == '1':
                
                if plataforma_existe:
                    print(f'La contraseña de su {plataforma} es: {contraseña}')
                
                else:
                    print('\nEsa plataforma no esta registrada en la base de datos. \n')
                    
            elif opcion_gestion == '2':

                if not plataforma_existe:
                    logica.guardado_de_datos(plataforma.lower())        
                    print('\nSu contraseña ha sido almacenada en el archivo ´contrseñas.csv´ con exito! \n')

                else:
                    print('\nEsa plataforma ya fue registrada. \n')
            
            elif opcion_gestion == '3':
                
                if plataforma_existe:
                    logica.cambio_de_contraseña(plataforma.lower())
                    print('\nSu contraseña ha sido cambiada correctamente! \n')
                else:
                    print(f'\nNo tiene contraseña para {plataforma} \n')
                

main()