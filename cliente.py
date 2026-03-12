import socket
import threading

host = "127.0.0.1"
port = 12345

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host, port))

print("Conectado al servidor")

def recibir():
    while True:
        try:
            mensaje = cliente.recv(1024).decode()
            print(mensaje)
        except:
            print("Conexión cerrada")
            break

def enviar():
    while True:
        mensaje = input("")
        cliente.send(mensaje.encode())

threading.Thread(target=recibir).start()
threading.Thread(target=enviar).start()