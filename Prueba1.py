import network
import socket
import time

ssid="JW"
key="@@EdAs02100496@"

# Configuración de la conexión Wi-Fi
wf=network.WLAN(network.STA_IF)
wf.active(True)
wf.connect(ssid,key)
while not wf.isconnected():
    print(".")
    time.sleep(1)
print('Conexión establecida:', wf.ifconfig()[0])

# Configuración del socket del servidor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 80))
s.listen(5)

# Función para manejar las solicitudes HTTP
def procesar_solicitud(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    request_lines = request.split('\r\n')
    method, path, protocol = request_lines[0].split(' ')
    print(protocol)

    if method == 'GET':
        if path == '/':
            
            page = "<html><body><h1>Hola, esta es la pagina principal</h1></body></html>"
        elif path == '/pagina1':
            
            page = "<html><body><h1>Esta es la pagina 1</h1></body></html>"
        elif path == '/pagina2':
            
            page = "<html><body><h1>Esta es la pagina 2</h1></body></html>"
        else:
            
            page = "<html><body><h1>Pagina no encontrada</h1></body></html>"

        
        client_socket.sendall('HTTP/1.1 200 OK\r\n\r\n' + page)
    else:
        
        client_socket.sendall('HTTP/1.1 405 Method Not Allowed\r\n\r\n')
    
    client_socket.close()

# se espera para manejar las solicitudes
while True:
    client, addr = s.accept()
    procesar_solicitud(client)
