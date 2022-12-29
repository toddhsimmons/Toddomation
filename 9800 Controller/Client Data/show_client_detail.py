from netmiko import ConnectHandler
import re
from time import time, sleep
import json

device1 = {
    "host": "172.16.255.5",
    "username": "tsimmons-a",
    "password": "Memphistenntime23$",
    "device_type": "cisco_ios",
}
MAC = ["56d3.c6b0.5e3b","1ac2.b560.edee","a672.3073.9e09"] # Steve-56d3.c6b0.5e3b | Keenan-1ac2.b560.edee
filename = "client_detail.txt"
outfile = "client_detail.json"
detail_template = "show_client_detail.template"
results = []
net_connect = ConnectHandler(**device1)


def status():
    for device in MAC:
        client_detail = net_connect.send_command(f"show wireless client mac-address {device} detail", read_timeout=60, use_textfsm=True, textfsm_template=detail_template)
        results.append(client_detail)
    return(results)

while True:
    sleep(60 - time() % 60)
    response = status()
    # print(response)
    with open(outfile, 'a') as f:
        json.dump(response, f, indent=4)
        f.writelines("\n")
    
