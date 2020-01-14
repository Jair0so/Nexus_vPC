# Created by Jairo Osorio January 13 2019
import sys

# Enter the the vPC / Port-Channel
vPC = input('enter the vpc/port-channel number \n')
print('you have entered ', vPC)

# Ask how many interfaces per switch will be in port-channel
switch_interfaces = input(' enter the number of interfaces per switch - between 1 and 8 \n')
if switch_interfaces > '0' or switch_interfaces <= '8':
    print('you have entered', switch_interfaces, 'interfaces per switch')
else:
    sys.exit('aa! errors!... number needs to be > 0 or < 8')


# Ask interfaces
interfaces_to_use = []
dummy_value = 0
while 1:
    dummy_value +=1
    interfaces_2_use = input('Press ENTER to escape ---- Enter the interface number in the following format -- Ex: Ethernet3/1 \n')
    if interfaces_2_use == '':
        break
    interfaces_to_use.append(interfaces_2_use)
print(interfaces_to_use)

def switch_port_access():
    vlan = input('Enter the VLAN ID you want to use \n')
    print('interface port-channel', vPC,'\n'
                                         'description vPC to XXX \n'
                                         'switchport \n'
                                         'switchport access vlan ',vlan,'\n'
                                         'spanning-tree port type edge \n'
                                         'vpc', vPC, '\n'
                                         'shutdown \n')
    for each in interfaces_to_use:
        print('interface ', each, '\n'
                                  'switchport \n'
                                  'description XXXXX \n'
                                  'switchport access vlan ',vlan, '\n'
                                  'channel-group ',vPC, 'mode active \n'
                                  'shutdown \n'
                                  '! \n')


print(switch_port_access())


