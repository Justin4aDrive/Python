#!/usr/bin/env python3

import re
import csv
import os
import operator

usage = {}
error = {}

with open("syslog.log") as file:
    for line in file.readlines():
        match = re.search(
            r"ticky: ([\w+]*):? ([\w' ]*)[\[[#0-9]*\]?]? ?\((.*)\)$", line)
        code, error_msg, user = match.group(1), match.group(2), match.group(3)

        if error_msg not in error.keys():
            error[error_msg] = 1
        else:
            error[error_msg] += 1

        if user not in usage.keys():
            usage[user] = {}
            usage[user]["INFO"] = 0
            usage[user]["ERROR"] = 0

        if code == "INFO":
            if user not in usage.keys():
                usage[user] = {}
                usage[user]["INFO"] = 0
            else:
                usage[user]["INFO"] += 1
        elif code == "ERROR":
            if user not in usage.keys():
                usage[user] = {}
                usage[user]["INFO"] = 0
            else:
                usage[user]["ERROR"] += 1

error_list = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
usage_list = sorted(usage.items(), key=operator.itemgetter(0))
file.close()

error_list.insert(0, ("Error", "Count"))

with open("user_statistics.csv", 'w', newline='') as user_csv:
    for key, value in usage_list:
        user_csv.write(str(key) + "," +
                       str(value["INFO"]) + "," + str(value["ERROR"])+"\n")

with open("error_message.csv", 'w', newline='') as error_csv:
    for key, value in error_list:
        error_csv.write(str(key) + " " + str(value))