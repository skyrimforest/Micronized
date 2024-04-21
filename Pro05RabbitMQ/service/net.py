import time
import subprocess

target_ip='192.168.137.1'

intervals=[100]
packets=[150]

password='111111'

cmd=f'echo {password} | sudo -S '

# sudo iptables -I INPUT -s 192.168.137.1 -j DROP;sudo iptables -I INPUT -m limit -s 192.168.137.1 --limit 100/s -j ACCEPT
# sudo iptables -I INPUT -d 192.168.137.1 -j DROP;sudo iptables -I INPUT -m limit -d 192.168.137.1 --limit 100/s -j ACCEPT

# sudo iptables -D INPUT -s 192.168.137.123 -j DROP;sudo iptables -D INPUT -m limit -s 192.168.137.123 --limit 5/s -j ACCEPT
# sudo iptables -D INPUT -d 192.168.137.123 -j DROP;sudo iptables -D INPUT -m limit -d 192.168.137.123 --limit 10/s -j ACCEPT

set_commands=[]
remove_commands=[]

def get_iptables_rule(max_packets):
    for max_packet in max_packets:
        temp_set=[]
        set_command_origin1 = f"iptables -I INPUT -s {target_ip} -j DROP;"
        set_command_origin2 = f"iptables -I INPUT -m limit -s {target_ip} --limit {max_packet}/s --limit-burst {int(max_packet * 1.1)} -j ACCEPT"
        set_command_origin3 = f"iptables -I INPUT -d {target_ip} -j DROP;"
        set_command_origin4 = f"iptables -I INPUT -m limit -d {target_ip} --limit {max_packet}/s --limit-burst {int(max_packet * 1.1)} -j ACCEPT"
        temp_set.append(set_command_origin1)
        temp_set.append(set_command_origin2)
        temp_set.append(set_command_origin3)
        temp_set.append(set_command_origin4)
        set_commands.append(temp_set)

        temp_remove=[]
        remove_command_origin1 = f"iptables -D INPUT -s {target_ip} -j DROP;"
        remove_command_origin2 = f"iptables -D INPUT -m limit -s {target_ip} --limit {max_packet}/s --limit-burst {int(max_packet * 1.1)} -j ACCEPT"
        remove_command_origin3 = f"iptables -D INPUT -d {target_ip} -j DROP;"
        remove_command_origin4 = f"iptables -D INPUT -m limit -d {target_ip} --limit {max_packet}/s --limit-burst {int(max_packet * 1.1)} -j ACCEPT"
        temp_remove.append(remove_command_origin1)
        temp_remove.append(remove_command_origin2)
        temp_remove.append(remove_command_origin3)
        temp_remove.append(remove_command_origin4)
        remove_commands.append(temp_remove)

def set_iptables_rule(set_item):
    for item in set_item:
        command=cmd+item
        print(command)
        subprocess.run(command,shell=True,text=True)
def remove_iptables_rule(remove_item):
    for item in remove_item:
        command=cmd+item
        print(command)
        subprocess.run(command,shell=True,text=True)

time_flag=0
def fluctuate_iptables_rule():
    global time_flag
    while True:
        set_iptables_rule(set_commands[time_flag])
        time.sleep(intervals[time_flag])
        remove_iptables_rule(remove_commands[time_flag])

        time_flag+=1
        if time_flag >= len(intervals):
            time_flag=0

if __name__ == '__main__':
    get_iptables_rule(packets)
    fluctuate_iptables_rule()


