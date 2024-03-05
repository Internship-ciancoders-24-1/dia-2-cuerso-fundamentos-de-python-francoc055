import click
from services import ClientService
from cliente import Cliente
import json_manager 
import json

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', required=True, help='nombre del cliente')
@click.option('--age', required=True, help='edad del cliente')
@click.option('--email', required=True, help='email del cliente')
@click.pass_context
def new(ctx, name, age, email):
    if not name or not age or not email:
        print('Error. Verifique los campos.')
    else:
        data = json_manager.read_json()
        new_id = len(data) + 1
        new_client = Cliente(new_id, name, age, email)
        ClientService.create_client(new_client, data)
        
    

@click.option('--id',required=True, help='id del usuario', type=int)
@cli.command()
@click.option('--name', help='nuevo nombre de usuario')
@click.option('--age', help='nueva edad de usuario')
@click.option('--email', help='nuevo email de usuario')
@click.argument('id', type=int)
def update(id, name, age, email):
    data = json_manager.read_json()
    client = next((e for e in data if e['id'] == id), None)
    ClientService.update_client(client, data, name, age, email)
    
        

@cli.command()
@click.argument('id', type=int)
def client(id):
    ClientService.get_client(id)


@cli.command()
@click.argument('id', type=int)
def delete(id):
    ClientService.delete_client(id)


@cli.command()
def clients():
    ClientService.get_all_clients()

if __name__ == '__main__':
    cli()