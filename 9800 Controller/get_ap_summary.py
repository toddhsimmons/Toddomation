from netmiko import ConnectHandler
import json

connect_info = "user_pass.json"

with open(connect_info, 'r') as json_data:
    args = json.load(json_data)



device={
    "host": "10.0.0.11",
    "username": "admin",
    "password": "Pyth0nR0cks!!!",
    "device_type": "cisco_ios"
}


net_connect = ConnectHandler(**device)

output = net_connect.send_command("show ap summary", read_timeout=20, use_textfsm=True, textfsm_template="cisco_ios_show_ap_summary.template")

net_connect.disconnect()

# Write the Python list to a JSON file
with open('ap_summary.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=4)
