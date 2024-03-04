clientes = "agustin,lucia"

def list_clients():
    print(clientes)

def create_client():
    global clientes
    name = input("Escriba un nombre: ")
    if len(name) == 0 or name in clientes:
        print("Error.")
        return
    
    clientes += f',{name}'
    print("Usuario creado")
    print(clientes)
    


if __name__ == '__main__':
    print("Bievenido al programa")
    print("[A] Listar")
    print("[B] Crear")

    inp = input()
    if inp == "A":
        list_clients()
    elif inp == "B":
        create_client()
    else:
        print("No existe el comando")
        
    