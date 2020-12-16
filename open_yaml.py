from netmiko import ConnectHandler
import yaml
from pprint import pprint
command = " show configuration system ntp"


def open_yaml(data):
    new = yaml.safe_load(data)
    return new

if __name__ == "__main__":
    with open("global.yaml") as f:
        pprint(open_yaml(f))
