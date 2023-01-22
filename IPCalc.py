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
        first_host = str(network[1])
        last_host = str(network[-2])

        # Print the results
        print("IP:" + "\t\t" + ip)
        print("Network mask:" + "\t" + mask)
        print("Broadcast addr:" + "\t" + broadcast)
        print("First host IP:" + "\t" + first_host)
        print("Last host IP:" + "\t" + last_host)
        print("Hosts:" + "\t\t" + str(hosts))
        print("Binary IP:" + "\t" + '.'.join(format(int(x), '08b') for x in ip.split(".")))
        print("Bin netmask:" + "\t" + '.'.join(format(int(x), '08b') for x in mask.split(".")))

    except ValueError:
        print("Invalid IP or suffix")

# Get the IP and suffix from command line arguments
ip = sys.argv[1]
suffix = sys.argv[2]

network_info(ip, suffix)

