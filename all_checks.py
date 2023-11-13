#!/usr/bin/env python3

import os
import psutil
import shutil
import socket
import sys

def check_reboot():         #returns True if computer has a pending reboot
    return os.path.exists("/run/reboot-required")

def check_disk_full(disk, min_gb, min_percent):  #returns True if there isn't enough disk space, False if ok
    du = shutil.disk_usage(disk)    
    percentage_free = 100*du.free / du.total  #calculate percentage of free disk space
    gigabytes_free = du.free/2**30    #calculate free gigabytes
    if gigabytes_free < min_gb or percentage_free < min_percent:
        return True
    return False

def check_root_full():  #returns True if the root partition is full
    return check_disk_full(disk = "/", min_gb=2, min_percent=10)

def check_cpu_constrained():  #returns True if the CPU is 75% or greated under load
    return psutil.cpu_percent(1) > 75

def check_no_network():  #returnts True if unable to resolve Google URL
    try:
        socket.gethostbyname("www.google.com")
        return False
    except:
        return True

def main():
    checks=[
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root partition full"),
        (check_cpu_constrained, "Processor is heavily under load"),
        (check_no_network, "No working network"),
    ]
    for check, msg in checks:
        if check():
            print(msg)
            sys.exit(1)

    print("Everthing ok.")
    sys.exit(0)

main()