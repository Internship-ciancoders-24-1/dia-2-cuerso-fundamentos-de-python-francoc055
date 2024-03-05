import json_manager
from cliente import Cliente

class ClientService:
    def __init__(self) -> None:
        pass


    @staticmethod
    def create_client(cliente, data):
        client_dict = cliente.to_dict()
        data.append(client_dict)
        json_manager.write_json(data)
        print("Usuario creado con éxito.")

    @staticmethod
    def update_client(client, data, name, age, email):
        if client:
            if name:
                client['name'] = name
            if age:
                client['age'] = age
            if email:
                client['email'] = email

            print('Cliente actualizado')
            json_manager.write_json(data)
        else:
            print("no existe el usuario")

    @staticmethod
    def delete_client(id):
        data = json_manager.read_json()
        client = next((e for e in data if e['id'] == id), None)
        if not client:
            print("no existe el usuario")
        else:
            data.remove(client)
            json_manager.write_json(data)
            print("usuario eliminado cone exito")

    @staticmethod
    def get_client(id):
        data = json_manager.read_json()
        client = next((e for e in data if e['id'] == id), None)
        if not client:
            print("no existe el usuario")
        else:
            print(client)

    @staticmethod
    def get_all_clients():
        data = json_manager.read_json()
        for client in data:
            print(f"id: {client['id']} - name: {client['name']} - age: {client['age']} - email: {client['email']}")