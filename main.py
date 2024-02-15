import sys 

clients = ['pablo', 'ricardo']

def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Client already is in the Clients List')
    
    
def list_clients():
    for idx, client in enumerate(clients):
        print('{}: {}'.format(idx, client))
    
    
def update_client(client_name, updated_name):
    global clients
    
    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_name
    else:
        print('Client is not in Client List')
        
        
def delete_client(client_name):
    global clients
    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client is not in Client List')
    
        
def search_client(client_name):
        for client in clients:
            if client != client_name:
                continue
            else:
                return True
    
    
def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 25)
    print('What would you like to do today?:')
    print('[C]reate Client')
    print('[L]ist Clients')
    print('[U]pdate Client')
    print('[D]elete Client')
    print('[S]earch Cleint')
    
    print()
    print('Escribe una letra de las opciones:')
    # list_clients()
    
def _get_client_name():
    client_name = None
    
    while not client_name:
        client_name = input('Whta is the client name?').strip()
        
        if client_name == 'exit':
            client_name = None
            break
        
    if not client_name:
            sys.exit()
    
    return client_name
    
    
if __name__ == '__main__':
    
    _print_welcome()
    command = input()
    command = command.upper()
    
    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('Whta is the update client name?')
        update_client(client_name, update_client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('The client is in the client list')
        else:
            print('The client: {} is not in our client list'.format(client_name))
    else:
        print('Invalid Command')
    
    








