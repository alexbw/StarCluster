network_interfaces_template = \
"""#This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
auto eth0
iface eth0 inet dhcp
  dns-nameservers {master_ip:}
  dns-search {cluster_tag:}
"""
