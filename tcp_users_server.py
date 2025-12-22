import socket
from utils.log import log

def server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 12345)
    server_sock.bind(server_address)

    server_sock.listen(10)
    log("INFO", f"TCP сервер запущен на: {server_address}")

    server_sock.settimeout(5)

    message_history = []
    try:
        while True:
            try:
                client_sock, client_addr = server_sock.accept()
                log("INFO", f"Пользователь с адресом: {client_addr} подключился к серверу")

            except socket.timeout:
                log("DEBUG", "Ожидание подключений...")
                continue

            data = client_sock.recv(1024).decode()
            message_history.append(data)
            log("INFO", f"Пользователь с адресом: {client_addr} отправил сообщение: {data}")

            response = '\n'.join(message_history)
            client_sock.send(response.encode())
            log("INFO", f"Пользователю с адресом: {client_addr} отправлен ответ:\n{response}")

    except KeyboardInterrupt:
        log("INFO", "Сервер остановлен пользователем")


    finally:
        if server_sock:
            log("INFO", "Закрытие сокета сервера")
            server_sock.close()

if __name__ == "__main__":
    server()