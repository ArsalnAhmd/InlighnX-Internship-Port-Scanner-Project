#!/usr/bin/env python3
"""
Port Scanner Project
Offensive Cybersecurity Internship Demo

Scans a target host for open ports within a specified range,
identifies services, and grabs banners where possible.

⚠️ Disclaimer:
This tool is for EDUCATIONAL and RESEARCH purposes only.
Do not use against systems you do not own or have explicit permission to test.
"""

import socket
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def get_banner(sock):
    """Attempt to grab a banner from an open port."""
    try:
        sock.settimeout(1)
        banner = sock.recv(1024).decode().strip()
        return banner
    except Exception:
        return ""


def scan_port(target_ip, port):
    """Scan a single port and return result."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            service = socket.getservbyport(port, "tcp") if port < 1024 else "unknown"
            banner = get_banner(sock)
            sock.close()
            return (port, True, service, banner)
        else:
            sock.close()
            return (port, False, None, None)
    except Exception:
        return (port, False, None, None)


def format_port_results(results):
    """Format results into a colored table."""
    print(f"\n{YELLOW}{'Port':<8}{'Status':<12}{'Service':<15}{'Banner'}{RESET}")
    print("-" * 60)
    for port, is_open, service, banner in results:
        if is_open:
            print(f"{GREEN}{port:<8}{'OPEN':<12}{service:<15}{banner}{RESET}")
        else:
            print(f"{RED}{port:<8}{'CLOSED':<12}{'':<15}{RESET}")


def port_scan(target_host, start_port, end_port, max_workers=50):
    """Main port scanning function."""
    try:
        target_ip = socket.gethostbyname(target_host)
        print(f"\nScanning host: {target_host} ({target_ip})")
    except socket.gaierror:
        print(f"[-] Could not resolve hostname: {target_host}")
        return

    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(scan_port, target_ip, port): port for port in range(start_port, end_port + 1)}

        total_ports = len(futures)
        completed = 0

        for future in as_completed(futures):
            results.append(future.result())
            completed += 1
            sys.stdout.write(f"\rProgress: {completed}/{total_ports} ports scanned")
            sys.stdout.flush()

    print("\n\nScan complete.")
    format_port_results(results)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Python Port Scanner")
    parser.add_argument("target", help="Target hostname or IP address")
    parser.add_argument("--start", type=int, default=1, help="Start port (default: 1)")
    parser.add_argument("--end", type=int, default=1024, help="End port (default: 1024)")
    parser.add_argument("--threads", type=int, default=50, help="Number of threads (default: 50)")

    args = parser.parse_args()

    port_scan(args.target, args.start, args.end, args.threads)