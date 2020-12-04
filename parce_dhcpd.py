# -*- coding: utf-8 -*-
"""
Данный скрипт, фильтрует списки dhcpd.leases,  забирая через шаблон данные ip устройства и имя компьютера, все остальное удаляется включая повторяющиеся элементы
"""
import sys
import textfsm
import yaml
from tabulate import tabulate
from pprint import pprint
from collections import OrderedDict
def parse_command_output(template,command_output):    # парс шаблоном
    with open(template) as temp:
        fsm = textfsm.TextFSM(temp)
        result = fsm.ParseText(command_output)
        a = []
        for line in result:
            if "android" in line[1]:
                pass
            elif "ap7632" in line[1]:
                pass
            elif "HUAWEI" in line[1]:
                pass  
            elif "SIP-" in line[1]:
                pass  
            elif "mywild" in line[1]:
                pass  
            elif "videosrv" in line[1]:
                pass              
            elif "AP94D4" in line[1]:
                pass  
            elif "orangepione" in line[1]:
                pass 
            elif "U2" in line[1]:
                pass
            elif "iPhone" in line[1]:
                pass
            elif "Galaxy" in line[1]:
                pass
            elif "Apple" in line[1]:
                pass
            elif "Honor" in line[1]:
                pass
            elif "Redmi" in line[1]:
                pass
            elif "Huawei AP-AirEngine5760" in line[1]:
                pass             
            else:
                a.append(str(line) + '\n')
            b = list(OrderedDict.fromkeys(a))
        with open("name_of_switch_22.10.2020.txt", "w") as f2:   # конечное имя файла для записи
            f2.writelines((b))   
        return  b
if __name__ == "__main__":
    with open("8.txt") as show:       # меняем dhcpd.leases в файл c расширением txt
        output = show.read()
        
    result = parse_command_output("templates/dhcp_koledino.template", output)
    pprint(result)
    
