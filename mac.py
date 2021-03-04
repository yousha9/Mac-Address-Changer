import subprocess
import re

# Call() and check_output() are important subprocess

interface = input("Enter interface name: ")
mac = input("Enter your New Mac_Address: ")

# Put the interface down
subprocess.call(["ifconfig", interface, "down"])

# Modify the interface to accept the new Mac_Address
subprocess.call(["ifconfig", interface, "hw", "ether", mac])

# Put the interface up again after changing its Mac_Address
subprocess.call(["ifconfig", interface, "up"])

# To check the output
output = str(subprocess.check_output(["ifconfig", interface]))
changed_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)

# Check if Mac_Address has changed
if mac == changed_mac.group(0):
    print("The Mac_Address has changed successfully!!")

