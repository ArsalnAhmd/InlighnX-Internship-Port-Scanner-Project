# 🔍 Python Port Scanner
**Offensive Cybersecurity Internship Project**

This project demonstrates how to build a multithreaded **Port Scanner** in Python.  
The tool scans a target host for open ports within a specified range, identifies services, and attempts to grab banners where possible. It highlights practical skills in **network programming, multithreading, progress tracking, and ethical penetration testing**.

⚠️ **Disclaimer**: This project is for **educational and research purposes only**.  
Do not use it against systems you do not own or have explicit permission to test.

---

## 🚀 Features
- **Port Scanning**: Detects open/closed ports in a given range.
- **Service Identification**: Uses `getservbyport()` to map ports to services.
- **Banner Grabbing**: Attempts to retrieve banners from open ports.
- **Multithreading**: Parallel scanning with `ThreadPoolExecutor` for speed.
- **Progress Tracking**: Real‑time progress updates in the terminal.
- **ANSI Color Output**: Clear, formatted results with colored status indicators.

---

## ⚙️ Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/<your-username>/port-scanner.git
cd port-scanner
pip install -r requirements.txt
