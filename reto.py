#Reto
#Función create_padawan para registrar una padawan
def create_padawan():
    padawan = {"nombre": '', "edad": 0, "temas": "", "estado": ''}
    for key in padawan.keys():
        if(key=="temas"):
          padawan[key] = input(f'¿Cuáles son tus {key} de interés?: ')
        elif(key=="estado"):
            if(int(padawan["edad"]) > 18):
                padawan['estado'] = 'Es mayor de edad'
            else:
                padawan['estado'] = 'Es menor de edad'
        else:
            padawan[key] = input(f'Escriba su {key}: ')
    return padawan

#Función print_padawans para imprimir la lista padawans
def print_padawans(padawans):
    for padawan in padawans:
        #print('\n')
        print('*'*40)
        for key in padawan:
            print(f'{key}: {padawan[key]}')
        

padawans = []
while(True):
    print('_'*50)
    print("1. Añadir una padawan a SFWIT")
    print("2. Lista de participantes en SFWIT")
    print("3. Salir")
    opcion = int(input("Elige una opción:  "))

    if opcion == 1:
        padawan = create_padawan()
        padawans.append(padawan)
    elif opcion == 2:
        print_padawans(padawans)
    elif opcion == 3:
        break
    else:
        print("Error, opción inválida")

#Que el código te acompañe!