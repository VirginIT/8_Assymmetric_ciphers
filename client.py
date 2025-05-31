import socket
import random

def modexp(base, exp, mod):
    return pow(base, exp, mod)

HOST = 'localhost'
PORT = 65432

g = 5
p = 23

a = random.randint(2, p - 2)
A = modexp(g, a, p)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    message = f"{g},{p},{A}"
    s.sendall(message.encode())
    print(f"[КЛИЕНТ] Отправлено: g={g}, p={p}, A={A}")

    data = s.recv(1024).decode()
    B = int(data)
    print(f"[КЛИЕНТ] Получено B={B}")

    K = modexp(B, a, p)
    print(f"[КЛИЕНТ] Вычислен общий ключ: K={K}")

