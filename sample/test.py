from genie import testbed
from conf import CONFIG_YAML
from lib.device import Device
from lib import wait, ipv4
import ini
import time
#import wait_until, calc

tb = testbed.load(CONFIG_YAML)

# switch
iosv_0 = Device(tb, 'iosv_0')
server_0 = Device(tb, 'server_0')
server_1 = Device(tb, 'server_1')
server_2 = Device(tb, 'server_2')

iosv_0.execs([
  [
    f"interface {ini.iosv_0.g0_0.name}",
    f"ip addr {ini.iosv_0.g0_0.ip_addr} {ini.iosv_0.g0_0.subnet_mask}",
    f"no shutdown",
  ],
])

server_0.execs([
  f"ifconfig eth0",
])

server_2.execs([
  f"show",
  f"ip {ini.server_2.eth0.ip_addr} {ini.server_2.eth0.subnet_mask} {ini.iosv_0.g0_0.ip_addr}",
  f"show",
  f"show arp",
])