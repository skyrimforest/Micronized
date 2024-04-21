import BaseConfig
import subprocess
from SkyLogger import get_logger

password='111111'
set_rule=[]
remove_rule=[]
cmd=f'echo {password} | sudo -S '

logger=get_logger('net_service')

def get_iptables_rule(max_packet):
    temp_set=[]
    set_command_origin1 = f"iptables -I INPUT -s {BaseConfig.CLOUD_IP} -j DROP;"
    set_command_origin2 = f"iptables -I INPUT -m limit -s {BaseConfig.CLOUD_IP} --limit {max_packet}/s --limit-burst {int(max_packet * 1.1)} -j ACCEPT"
    set_command_origin3 = f"iptables -I INPUT -d {BaseConfig.CLOUD_IP} -j DROP;"
    set_command_origin4 = f"iptables -I INPUT -m limit -d {BaseConfig.CLOUD_IP} --limit {max_packet}/s --limit-burst {int(max_packet * 1.1)} -j ACCEPT"
    temp_set.append(set_command_origin1)
    temp_set.append(set_command_origin2)
    temp_set.append(set_command_origin3)
    temp_set.append(set_command_origin4)
    set_rule.append(temp_set)

    temp_remove=[]
    remove_command_origin1 = f"iptables -D INPUT -s {BaseConfig.CLOUD_IP} -j DROP;"
    remove_command_origin2 = f"iptables -D INPUT -m limit -s {BaseConfig.CLOUD_IP} --limit {max_packet}/s --limit-burst {int(max_packet * 1.1)} -j ACCEPT"
    remove_command_origin3 = f"iptables -D INPUT -d {BaseConfig.CLOUD_IP} -j DROP;"
    remove_command_origin4 = f"iptables -D INPUT -m limit -d {BaseConfig.CLOUD_IP} --limit {max_packet}/s --limit-burst {int(max_packet * 1.1)} -j ACCEPT"
    temp_remove.append(remove_command_origin1)
    temp_remove.append(remove_command_origin2)
    temp_remove.append(remove_command_origin3)
    temp_remove.append(remove_command_origin4)
    remove_rule.append(temp_remove)
        
        
def set_one_iptables_rule(set_item):
    for item in set_item:
        command=cmd+item
        print(command)
        subprocess.run(command,shell=True,text=True)
def remove_one_iptables_rule(remove_item):
    for item in remove_item:
        command=cmd+item
        print(command)
        subprocess.run(command,shell=True,text=True)


def set_bandwidth_limit(bandwidth):
    get_iptables_rule(bandwidth)
    global set_rule
    for item in set_rule:
        set_one_iptables_rule(item)
    logger.info(f'Setting bandwidth to {bandwidth}')

def remove_bandwidth_limit():
    global remove_rule
    for item in remove_rule:
        remove_one_iptables_rule(item)
    logger.info(f'All limits are removed')

