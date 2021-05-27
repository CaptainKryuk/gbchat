from socket import SOCK_STREAM, socket, AF_INET
import threading
import time
import pickle
from argparse import ArgumentParser
import traceback


def create_parser():
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=7777)
    parser.add_argument('-a', '--address', default='')
    return parser


def receiver(client, clients: list):
    while True:
        try:
            message = client.recv(1024)
            message = pickle.loads(message)
            broadcast(message, clients, client)
        except:
            clients.remove(client)
            client.close()
            broadcast(f'Client left server: {client}', clients, client)
            break


def broadcast(message, clients, client):
    for cl in clients:
        if cl != client:
            mes = pickle.dumps(message)
            cl.send(mes)


def main():
    print('[ Server Started ]')
    clients = []
    parser = create_parser().parse_args()
    with socket(AF_INET, SOCK_STREAM) as s:
        s.bind((parser.address, parser.port))
        s.listen(10)

        stop = False

        while not stop:
            try:
                client, addr = s.accept()

                broadcast(f'Client join server: {addr}', clients, client)
                
                if client not in clients:
                    clients.append(client)               

                thread = threading.Thread(target=receiver, args=(client, clients))
                thread.start()
                    
            except Exception as e:
                print('Stop server error: ', traceback.format_exc())
                break
            except KeyboardInterrupt:
                print('Stop server')
                break

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('Unhandler error: ', traceback.format_exc())