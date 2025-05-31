import socket
import random

def modexp(base, exp, mod):
    return pow(base, exp, mod)

HOST = 'localhost'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("[СЕРВЕР] Ожидание подключения клиента...")
    conn, addr = s.accept()
    with conn:
        print(f"[СЕРВЕР] Подключено к {addr}")

        data = conn.recv(1024).decode()
        g, p, A = map(int, data.split(','))
        print(f"[СЕРВЕР] Получено: g={g}, p={p}, A={A}")

        b = random.randint(2, p - 2)
        B = modexp(g, b, p)
        K = modexp(A, b, p)
        print(f"[СЕРВЕР] Вычислен общий ключ: K={K}")

        conn.sendall(str(B).encode())
