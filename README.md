# Python3-NmapScanner

Historical Python/Nmap learning fork of [AlexisAhmed/Python3-NmapScanner](https://github.com/AlexisAhmed/Python3-NmapScanner).

This repository records beginner exploration of Python-driven network scanning. It is not a production support tool or evidence of enterprise network administration. Original authorship belongs to the upstream project; this fork should not be presented as an independently developed scanner.

## Current status

The checked-in `Scanner.py` is unfinished and does not run as written. Inspection on 24 September 2026 found:

- A syntax error in the `print` call containing `"nmap version: "sccaner.nmap_version()`.
- A misspelled `sccaner` variable; the scanner object is named `scanner`.
- A host-status condition that compares `scanner.scaninfo()` to the string `"up"`, rather than checking the target host state.
- No robust input validation or handling for missing scan results.

No live scan was performed for this review. These issues are documented here, not fixed in the script.

## What the script explores

The script prompts for an IP address and a scan choice, then attempts to scan ports 1–1024 using Nmap SYN, UDP, or a more extensive set of detection options. Its first menu label says "SYN ACK Scan", but the configured `-sS` option requests a SYN scan.

It imports the `python-nmap` wrapper and requires the separate Nmap executable. Some selected scan options require elevated privileges. Only use scanning tools against systems you own or have explicit permission to assess.

## Professional context

My current focus is IT Support, systems administration, and infrastructure, with Security+ as a foundation. This fork remains part of my earlier learning history. See my [profile](https://github.com/BenjaminChukwu05) for current work and documentation.
