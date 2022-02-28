# pyips
Turn a CIDR or list of CIDRs into a list of IP addresses

## Usage
You can pass it a range in CIDR notation
```bash
python3 pyips.py "192.0.2.0/28"
```

</br>

You can pass it a list of ranges in CIDR notation
```bash
python3 pyips.py "cidrs.txt"
```

The IPs will be inside an output file named `hosts.txt`