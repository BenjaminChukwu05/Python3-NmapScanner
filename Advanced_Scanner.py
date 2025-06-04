#!/usr/bin/python3

import nmap
import datetime

scanner = nmap.PortScanner()

print("\n=== Advanced Nmap Automation Tool ===")
print("------------------------------------\n")

def main():
    try:
        # Get target
        ip_addr = input("Enter IP/hostname to scan: ").strip()
        print(f"\nTarget: {ip_addr}")
        
        # Host discovery
        print("\n[+] Checking if host is reachable...")
        scanner.scan(hosts=ip_addr, arguments='-sn')
        if not scanner[ip_addr].state() == 'up':
            print("[!] Host appears to be down!")
            return
        
        # Scan menu
        print("\nSelect scan type:")
        scan_types = {
            '1': ['-v -sS', 'tcp', 'SYN Stealth Scan'],
            '2': ['-v -sU', 'udp', 'UDP Scan'], 
            '3': ['-v -sS -sV -sC -A -O', 'tcp', 'Comprehensive Scan'],
            '4': ['-v -Pn -T4 -F', 'tcp', 'Fast Scan (No Ping)']
        }
        
        for num, details in scan_types.items():
            print(f"{num}) {details[2]}")
        
        choice = input("\nEnter choice (1-4): ").strip()
        if choice not in scan_types:
            print("[!] Invalid choice")
            return
        
        # Get ports
        ports = input("Enter port range (e.g. 20-80) or 'default': ").strip()
        if not ports:
            ports = '1-1024'
        
        # Run scan
        print(f"\n[+] Starting {scan_types[choice][2]}...")
        start_time = datetime.datetime.now()
        
        scanner.scan(ip_addr, ports, scan_types[choice][0])
        
        # Results
        print("\n=== Scan Results ===")
        print(f"Duration: {datetime.datetime.now() - start_time}")
        print(f"Nmap version: {scanner.nmap_version()}")
        print(f"Scan info: {scanner.scaninfo()}")
        
        if scanner[ip_addr].state() == 'up':
            print(f"\nHost status: {scanner[ip_addr].state()}")
            print(f"Protocols: {scanner[ip_addr].all_protocols()}")
            
            for proto in scanner[ip_addr].all_protocols():
                print(f"\nOpen {proto} ports:")
                for port in scanner[ip_addr][proto].keys():
                    print(f"  {port}: {scanner[ip_addr][proto][port]['state']}")
        
        # Save results
        save = input("\nSave results to file? (y/n): ").lower()
        if save == 'y':
            filename = f"nmap_scan_{ip_addr}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w') as f:
                f.write(str(scanner.scaninfo()))
                f.write("\n\nOpen ports:\n")
                for proto in scanner[ip_addr].all_protocols():
                    for port in scanner[ip_addr][proto].keys():
                        f.write(f"{port}/{proto}: {scanner[ip_addr][proto][port]['state']}\n")
            print(f"[+] Results saved to {filename}")
    
    except nmap.PortScannerError as e:
        print(f"[!] Nmap error: {e}")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    main()
