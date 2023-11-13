#!/usr/bin/env python3

import os
import shutil
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

def check_root_full():  #retuns Trus if the root partition is full
    return check_disk_full(disk = "/", min_gb=2, min_percent=10)

def main():
    checks=[
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root partition full"),
    ]
    for check, msg in checks:
        if check():
            print(msg)
            sys.exit(1)

    print("Everthing ok.")
    sys.exit(0)

main()