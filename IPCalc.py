import sys
import ipaddress

def network_info(ip, suffix):
    try:
        # Create a network object using the given IP and suffix
        network = ipaddress.IPv4Network(ip + '/' + suffix, strict=False)

        # Get the network mask, broadcast address, and number of hosts
        mask = str(network.netmask)
        broadcast = str(network.broadcast_address)
        hosts = network.num_addresses - 2

        # Print the results
        print("Network mask: " + mask)
        print("Broadcast address: " + broadcast)
        print("Number of hosts: " + str(hosts))
    except ValueError:
        print("Invalid IP or suffix")

# Get the IP and suffix from command line arguments
ip = sys.argv[1]
suffix = sys.argv[2]

network_info(ip, suffix)
