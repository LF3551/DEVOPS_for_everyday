import yaml
from pprint import pprint
command = " show configuration system ntp"


def send_show_command(device, commands):
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        output = ssh.send_command(commands)
    return output

if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
        for device in devices:
            pprint(send_show_command(device, command))
