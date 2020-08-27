#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

#Input is asking for username, and getpass is asking for the password.
username = input("Enter your username")
password = getpass()

#Import file and read ip addresses
fhand = open('devices.csv','r').read().split('\n')

#Runnning three commands (command1, 2 and 3) through all devices in for-loop, and then print the three commands.
for fdevice in fhand:
    if "." not in fdevice:
        continue
    net_connect = Netmiko(device_type="cisco_ios", ip=fdevice, username=username,
                             password=password)
                             
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
