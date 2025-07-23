import json
import os

def menu():
    print('---Menu de contactos---')
    print('1. Listar todos los contactos')
    print('2. Crear nuevo contacto')
    print('3. Buscar contacto por ID')
    print('4. Actualizar contacto')
    print('5. Eliminar contacto')

    try:
        opcion = int(input(' : '))
        if (opcion == 1):
            leer_contacto()
            input('Presione Enter para continuar...')
            return menu()
        
        elif (opcion == 2):
            crear_contacto()
            input('Presione Enter para continuar...')
            return menu()
        
        elif (opcion == 3):
            busca_contacto()
            input('Presione Enter para continuar...')
            pass
        elif (opcion == 4):
            pass
        elif (opcion == 5):
            pass
        
    except ValueError:
        print('valor no valido')
        input('Enter para continuar...')

def leer_contacto():
       
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        with open('telefono.json', "r") as file:
            contactos = json.load(file)
            print(contactos)

    except FileNotFoundError as fn:
        print('dato no encontrado')
        return menu()
    except Exception as e:
        print('dato no encontrado')
        return menu()
    
def crear_contacto(fileName: str) -> bool:
    
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        with open('telefono.json', "w") as file:
            json.dump('telefono.json', file, indent=4)
            return True
    except Exception as e:
        return False

    except Exception:
        print('Error desconocido...')
        return menu()

def busca_contacto():

    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        with open('telefono.json', "r") as file:
            search = json.load(file)
            id = int(input('Ingrese ID: '))
            idC = search['ID']
            name = search['Nombre']

            if (id == idC):
                print(f'El contacto encontrado es: {name}')
            
            else:
                print('ID no existe')
                

    except Exception:
        print('Error desconocido')
        return menu()

def del_contacto():

    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        with open('telefono.json', "r") as file:
            usu = json.load(file)
            dele = int(input('Ingrese el ID: '))
            contacto = usu['ID']
            eliminar = usu['']


    except Exception:
        print('Error desconocido')
        return menu()
    

if __name__ == "__main__":
    menu()