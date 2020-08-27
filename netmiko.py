#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

#The username is user, and getpass is asking for the password.
username = "user"
password = getpass()

cisco1 = {
    "host": "192.168.0.1",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

cisco2 = {
    "host": "192.168.0.2",
    "username": username,
    "password": password,
    "device_type": "cisco_ios",
}

#Runnning three commands (command1, 2 and 3) through all devices, and then print the three commands.
for device in (cisco1, cisco2):
    net_connect = Netmiko(**device)
    command1 = "show env power"
    command2 = "show power inline"
    command3 = "show cdp nei | i AP"
    print(net_connect.find_prompt())
    output1 = net_connect.send_command(command1)
    output2 = net_connect.send_command(command2)
    output3 = net_connect.send_command(command3)
    net_connect.disconnect()
    print(output1)
    print(output2)
    print(output3)
