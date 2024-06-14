SUBNET_MASK_24 = "255.255.255.0"
INVERSE_MASK_24 = "0.0.0.255"
pcap_file = "test.pcap"
channel_group=1
ETHERCHANNEL_LACP='lacp'

class iosv_0:
  class g0_0:
    name = "GigabitEthernet0/0"
    slot = 0
    ip_addr = "192.168.0.254"
    subnet_mask = SUBNET_MASK_24
  class g0_1:
    name = "GigabitEthernet0/1"
    slot = 1
    ip_addr = "10.0.0.1"
    subnet_mask = SUBNET_MASK_24

class iosv_1:
  class g0_0:
    name = "GigabitEthernet0/0"
    slot = 0
    ip_addr = "192.168.1.254"
    subnet_mask = SUBNET_MASK_24
  class g0_1:
    name = "GigabitEthernet0/1"
    slot = 1
    ip_addr = "10.0.0.2"
    subnet_mask = SUBNET_MASK_24


class server_0:
    class eth0:
      ip_addr = "192.168.0.1"
      subnet_mask = SUBNET_MASK_24
      slot = 0

class server_1:
    class eth0:
      ip_addr = "192.168.1.1"
      subnet_mask = SUBNET_MASK_24
      slot = 0

class server_2:
    class eth0:
      ip_addr = "192.168.0.2"
      subnet_mask = SUBNET_MASK_24
      slot = 0