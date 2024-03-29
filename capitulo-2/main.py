clientes = ["agustin", "lucia", "lorenzo"]

def list_clients():
    for client in clientes:
        print(f"-{client}")

def create_client(name):
    global clientes
    if len(name) == 0 or name in clientes:
        print("Error.")
        return
    
    clientes.append(name)
    print("Cliente creado")
    list_clients()
    
def update_client(name, new_name):
    global clientes
    if name in clientes:
        index = clientes.index(name) 
        clientes[index] = new_name
        print("Cliente actualizado")
        list_clients()
    else:
        print("No existe el cliente")

def delete_client(name):
    global clientes
    if name in clientes:
        clientes.remove(name)
        print("Cliente eliminado")
        list_clients()
    else:
        print("No existe el cliente")

def search_client(name):
    for client in clientes:
        if client == name:
            return name
        
    return None

if __name__ == '__main__':
    print("Bievenido al programa")
    print("[A] Listar clientes")
    print("[B] Crear cliente")
    print("[C] Actualizar cliente")
    print("[D] Eliminar cliente")
    print("[E] Buscar cliente")

    inp = input()
    inp = inp.upper()

    if inp == "A":
        list_clients()
    elif inp == "B":
        name = input("Escriba un nombre: ")
        create_client(name)
    elif inp == "C":
        name = input("Escriba un nombre: ")
        new_name = input("Nombre actualizado: ")
        update_client(name, new_name)
    elif inp == "D":
        name = input("Escribe un nombre: ")
        delete_client(name)
    elif inp == "E":
        name = input("Escriba un nombre: ")
        found = search_client(name)
        if not found:
            print(f"No existe {name}") 
        else:
            print(f"Cliente: {name}")
        
    else:
        print("No existe el comando")
        
    