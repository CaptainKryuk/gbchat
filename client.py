from server import receiver
from socket import SOCK_STREAM, socket, AF_INET
import pickle
import time
import threading
import traceback
from utils.dict import MSG_TEMPLATE, PRESENSE, QUIT


def init_sock():
    """ 
    Initializate tcp/id socket
    """
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('', 7777))
    return s

T
def receiver(sock):
    """
    start receiver thread
    """
    while True:
        try:
            message = sock.recv(1024)
            message = pickle.loads(message)
            print('from: ',message)
        except Exception as e:
            print('Client error: ', traceback.format_exc())
            sock.close()
            break

def writer(sock):
    """
    start writer thread
    """
    while True:
        message = f'alie: {input()}'
        sock.send(pickle.dumps(message))


def main(sock):
    """
    Start all threads
    """
    write_thread = threading.Thread(target=receiver, args=(sock,))
    write_thread.start()

    receiver_thread = threading.Thread(target=writer, args=(sock,))
    receiver_thread.start()


if __name__ == '__main__':
    sock = init_sock()



