import ipaddress
import sys


cidr_list = []
ip_list = []
if ".txt" in sys.argv[1]:
    with open(sys.argv[1], "r") as inf:
        cidr_list = inf.read().splitlines()
else:
    cidr_list.append(sys.argv[1])

for cidr in cidr_list:
    ip_list.extend([str(ip) for ip in ipaddress.IPv4Network(cidr)])

with open ("hosts.txt", "w") as outf:
    for ip in ip_list:
        outf.write(f"{ip}\n")

