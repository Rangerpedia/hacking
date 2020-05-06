# Developer name: "Rangerpedia"
# Company name: "Rangerpedia squad"
# youtube channel name: "Rangerpedia squad"
# Please do it these hacking with yourself only..........
# These code is really for mac address changing

# First import a packages of these three:
import subprocess
import optparse
import re


# Getting a arguments from user:
def arguments_getted():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change it mac address")
    parser.add_option("-m", "--new_mac", dest="new_mac", help="change into a new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options



# Your actual command is here:
def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + "to" + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# And you can see your last mac address and print it:

def get_current_mac(interface, new_mac):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address by rangerpedia.")
options = arguments_getted()
current_mac = get_current_mac(options.interface, options.new_mac)
print("Current MAC =" + str(current_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface, options.new_mac)
if current_mac == options.new_mac:
    print("[+]MAC address was successfully changed by rangerpedia code" + current_mac)
else:
    print("[-]MAC ADDRESS DID NOT GET CHANGED by rangerpedia code..")

# these code is really useful for you to get mac information,  Thank you...
