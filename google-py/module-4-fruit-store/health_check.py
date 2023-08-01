#!/usr/bin/env python3

import socket, psutil, shutil, emails

user = 'student-00-7c090dc78b5c'

def check_localhost():
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"

def check_disk_usage(disk):
    disk_usage = shutil.disk_usage(disk)
    free = disk_usage.free / disk_usage.total * 100
    return free > 20

def check_memory_usage():
    memory_available = psutil.virtual_memory().available
    total = memory_available / (1024.0 ** 2)
    return total > 500

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 80

def send_email(subject):
    email = emails.generate_error_report("automation@example.com", user+"@example.com",
                                  subject,
                                  "Please check your system and resolve the issue as soon as possible.")
    emails.send(email)

if not check_cpu_usage() :
    subject="Error - CPU usage is over 80%"
    print(subject)
    send_email(subject)

if not check_memory_usage():
    subject = "Error - Available memory is less than 500MB"
    print(subject)
