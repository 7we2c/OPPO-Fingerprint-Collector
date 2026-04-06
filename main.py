import socket

target_ip = input("Enter target IP: ")
target_port = 46888

payloads = [
    b"\n",
    b"HELLO\n",
    b"INFO\n",
    b"GET\n",
    b"STATUS\n",
    b"VERSION\n",
    b"DEVICE\n",
    b"PING\n",
    b"\x00\x00\x00\x00"
]

def receive_all(sock):
    sock.settimeout(2)
    data = b""
    try:
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            data += chunk
    except:
        pass
    return data

def probe():
    for payload in payloads:
        try:
            print(f"\n[*] Trying payload: {payload}")

            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(5)
            client.connect((target_ip, target_port))

            # إرسال payload
            client.send(payload)

            # استقبال كامل البيانات
            response = receive_all(client)

            if response:
                print("[+] Response:")
                print("-" * 40)
                print(response.decode(errors="ignore"))
                print("-" * 40)
            else:
                print("[-] No response")

            client.close()

        except Exception as e:
            print(f"[!] Error: {e}")

if __name__ == "__main__":
    probe()
