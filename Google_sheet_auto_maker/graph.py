# -*- coding: cp1251 -*-
from datetime import datetime
from rw_sheet import read_sheets, write_final_result
import time
import datetime
from pprint import pprint
import yaml
from pprint import pprint
# py -3 -m pip install matplotlib
import matplotlib.pyplot as plt
real_date = time.strftime('%d.%m.%Y')
#real_date = '22.05.2021'
day_calendar = datetime.datetime.today().isoweekday()
with open ("C:\python_data\personal.yml") as f:
    day_of_week = (yaml.safe_load(f))["calendar"][day_calendar]
def auto_script():
    with open ("C:\python_data\personal.yml") as f:
        id_sheets = (yaml.safe_load(f))["sheets_id"]
    table_WORK_TIME = f"WORK_TIME!1:1000"
    data_from_WORK_TIME = read_sheets(table_WORK_TIME, id_sheets)
    new_table = []
    for one_line in data_from_WORK_TIME:
        new_table.append(one_line[1])
    my_dict = {i:new_table.count(i) for i in new_table}

    x = [i for i in my_dict.keys()]
    y = [i for i in my_dict.values()]

        # plot
    plt.plot(x,y)
    plt.gcf().autofmt_xdate(rotation=90,bottom=0.3)
    plt.show()



if __name__ == "__main__":
    auto_script()
