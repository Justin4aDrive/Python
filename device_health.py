#/usr/bin/env python3

import shutil
import psutil

hd_usage = shutil.disk_usage("/")
hd_free=(hd_usage.free/hd_usage.total*100)
rounded_hdfree= format(hd_free,".2f")
print ("{}% free disk space on this computer.".format(rounded_hdfree))

utilization = psutil.cpu_percent(1)
print ("{}% processor utilization on this computer.".format(utilization))

def disk_usage(disk):
    hd_usage = shutil.disk_usage(disk)
    free = hd_usage.free / hd_usage.total *100
    return free > 20

def cpu_usage():
    utilization = psutil.cpu_percent(1)
    return utilization < 75

if not disk_usage("/") or not cpu_usage():
    print ("Computer resourses low!!")
else:
    print ("Computer health is OK.")