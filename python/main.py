clients = 'pablo, ricardo, '

def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already is in the Clients List')
    
    
def list_clients():
    global clients
    print(clients)
    
def update_client(client_name, update_client_name):
    global clients
    
    if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name + ',')
    else:
        print('Client is not in Client List')
    
    
def _add_comma():
    global clients
    clients += ','
    
def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 25)
    print('What would you like to do today?:')
    print('[C]reate Client')
    print('[U]pdate Client')
    print('[D]elete Client')
    
def _get_client_name():
    return input('Whta is the client name?')
    
    
if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()
    
    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    elif command == 'U':
        client_name = _get_client_name()
        update_client_name = input('Whta is the update client name?')
        update_client(client_name, update_client_name)
        list_clients()
    else:
        print('Invalid Command')
    
    








