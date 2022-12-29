import json
import re
from netmiko import ConnectHandler
import time

filename = 'AP Ethernet Stats.txt'
start = time.time()

device1 = {
    "host": "172.16.255.5",
    "username": "tsimmons-a",
    "password": "Memphistenntime23$",
    "device_type": "cisco_ios",
}

net_connect = ConnectHandler(**device1)

start = time.time()

config = net_connect.send_command('show ap ethernet statistics', read_timeout=30)
net_connect.disconnect()

with open(filename, 'wt') as f:
    for line in config:
        f.write(line)


end = time.time()
total_time = int(end-start)
print(total_time)
