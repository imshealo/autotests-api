import socket
from utils.log import log


def client_send():
    client_socket = None

    try:
        log("INFO", "Создание TCP сокета...")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        log("INFO", "Подключение к серверу...")
        client_address = ('localhost', 12345)
        client_socket.connect(client_address)

        message = input()
        log("INFO", f"Отправка данных на сервер: {message}")
        client_socket.send(message.encode())

        response = client_socket.recv(1024).decode()
        print(response)

    except socket.error as e:
        log("ERROR", f"Ошибка сокета: {e}")

    finally:
        if client_socket:
            client_socket.close()
            log("INFO", "Закрытие соединения")


if __name__ == "__main__":
    client_send()