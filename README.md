# OPPO-Fingerprint-Collector
A Python-based PoC to extract non-resettable hardware identifiers (Fingerprints) from OPPO A53 devices via port 46888. Reported to OPPO/HackerOne but dismissed as 'Informative'—so here it is for public awareness

# 📱 OPPO-Fingerprint-Collector (A53 Series)

> **"If it's just 'Informative', then why is it so easy to harvest?"**

A Python-based Proof of Concept (PoC) to extract **non-resettable hardware identifiers** (Fingerprints) from OPPO A53 devices via an unauthenticated service on **Port 46888**.

---

### 🛡️ The Backstory
This vulnerability was discovered during a 4-day security audit on the **OPPO A53 (CPH2127)**. The device exposes a service that leaks sensitive hardware metadata (IMEI-based hashes, Model, etc.) to anyone on the same network.

Despite providing clear evidence that this identifier **survives a Factory Reset**, the report was closed by **HackerOne/OPPO** as **"Informative"**. This tool is released to raise public awareness about persistent tracking risks.

---

### ✨ Features
* **Automated Extraction:** No need for manual `nc` or `nmap` commands.
* **Hardware Bound:** Proves the leak of persistent IDs (Hash: `BE87B9869533...`).
* **Zero Authentication:** Works without any user permission or pairing.

---

### 🚀 How to Use
1. **Ensure Python 3 is installed** on your Kali Linux or any terminal.
2. **Clone the repo:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Oppo-Fingerprint-Collector.git](https://github.com/YOUR_USERNAME/Oppo-Fingerprint-Collector.git)
   cd Oppo-Fingerprint-Collector



python3 main.py

   📊 Technical Details (The "Informative" Part)
Target Port: 46888/tcp
Protocol: Plaintext Response.
Leaked Data: Device Model, Hardware Hash, Build Info.
Impact: Allows persistent tracking of users across different accounts and factory resets.
⚖️ Disclaimer
This tool is for educational and research purposes only. The author is not responsible for any misuse. Always perform security testing on devices you own or have explicit permission to test.
Author: [7we2c]
Status: Dismissed by Vendor (WontFix)
