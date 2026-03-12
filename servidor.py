import socket
import threading

host = "0.0.0.0"
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clientes = []

print("Servidor iniciado...")
print(f"Escuchando en {host}:{port}")

def broadcast(mensaje, conn):
    for cliente in clientes:
        if cliente != conn:
            cliente.send(mensaje)

def manejar_cliente(conn, addr):
    print(f"Cliente conectado: {addr}")
    clientes.append(conn)

    while True:
        try:
            mensaje = conn.recv(1024)
            if not mensaje:
                break

            broadcast(mensaje, conn)

        except:
            break

    clientes.remove(conn)
    conn.close()

while True:
    conn, addr = server.accept()
    hilo = threading.Thread(target=manejar_cliente, args=(conn, addr))
    hilo.start()