clientes = [
    {
        "name": "agustin",
        "age": 24,
        "email":"agus@gmail.com"
    },
    {
        "name": "lucia",
        "age": 26,
        "email":"lucia@gmail.com"
    }
]

def list_clients():
    for client in clientes:
        print("----")
        for key, value in client.items():
            print(key, ":", value)

def create_client(client):
    global clientes
    
    clientes.append(client)
    print("Cliente creado")
    list_clients()
    
def update_client(name, new_name):
    global clientes
    for client in clientes:
        if name == client["name"]:
            client['name'] = new_name
            print("Cliente actualizado")
            list_clients()
    else:
        print("No existe el cliente")

def delete_client(name):
    global clientes
    for client in clientes:
        if name == client["name"]:
            clientes.remove(client)
            print(f"Cliente {name} eliminado.")
            return
    print(f"Cliente {name} no encontrado en la lista.")



def search_client(name):
    for client in clientes:
        if name == client["name"]:
            return client
        
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
        name = input("Escriba su nombre: ")
        age = input("Escriba su edad: ")
        email = input("Escriba su email: ")
        client = {
            "name": name,
            "age": age,
            "email": email
        }
        create_client(client)
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
            print(f"Cliente: {found['name']} | {found['age']} | {found['email']}")
        
    else:
        print("No existe el comando")
        
    