# -*- coding: cp1251 -*-
from datetime import datetime
from rw_sheet import read_sheets, write_final_result
import time
import datetime
from pprint import pprint
import yaml
real_date = time.strftime('%d.%m.%Y')
print("*"*100,"\nPersonal GoogleSheets helper is ready to help, hello Aleksey")
#real_date = '22.05.2021'
day_calendar = datetime.datetime.today().isoweekday()
with open ("C:\python_data\personal.yml") as f:
    day_of_week = (yaml.safe_load(f))["calendar"][day_calendar]
print(f"Today is {real_date}, {day_of_week}")

def auto_script():
    with open ("C:\python_data\personal.yml") as f:
        id_sheets = (yaml.safe_load(f))["sheets_id"]
    table_WORK_TIME = f"WORK TIME!1:1000"
    data_from_WORK_TIME = read_sheets(table_WORK_TIME, id_sheets)
    table_to_enumerate= []
    night_table = []
    all_tasks = []
    for one_row in data_from_WORK_TIME:
        if one_row[1] == real_date:
            all_tasks.append(one_row)
        new_row = []
        night_row = []
        if one_row[2] == 'g' and one_row[1] == real_date:
            date_cell = one_row[1]
            location_cell = one_row[5]
            user_name = one_row[6]
            problem = one_row[7]
            what_have_done = one_row[8]
            new_row.append(date_cell)
            new_row.append(location_cell)
            new_row.append(user_name)
            new_row.append(problem)
            new_row.append(what_have_done)
            table_to_enumerate.append(new_row)
        if one_row[3] == 'n' and one_row[1] == real_date:
            date_cell = one_row[1]
            location_cell = one_row[5]
            user_name = one_row[6]
            what_have_done = one_row[8]
            spent_time = one_row[4]
            night_row.append(day_of_week)
            night_row.append(date_cell)
            night_row.append(spent_time)
            night_row.append(location_cell)
            night_row.append(user_name)
            night_row.append(what_have_done)
            night_table.append(night_row)
    print("Today you did: \n",len(all_tasks), " all tasks\n",len(table_to_enumerate), " global tasks\n",len(night_table), " night tasks")
    print("Congrats!!! I have wrote all this information in all Google tables")
    table_outside_working_hours = []    
    new_table_to_REPORT_FOR_EMAIL= []
    if table_to_enumerate:
        for i, item in enumerate(table_to_enumerate):
            item.insert(0,str(i+1))
            new_table_to_REPORT_FOR_EMAIL.append(item)
        table_REPORT_FOR_EMAIL = "report_for_email!1:1000"
        all_info_from_table_REPORT_FOR_EMAIL = read_sheets(table_REPORT_FOR_EMAIL, id_sheets)
        new_data = [i for i in new_table_to_REPORT_FOR_EMAIL if i not in all_info_from_table_REPORT_FOR_EMAIL]
        where_to_write = "report_for_email!1:1000"
        data_write = write_final_result(new_data, where_to_write, id_sheets)
    if night_table:
        #print("what was at night",night_table)
        for i, item in enumerate(night_table):
            item.insert(0,str(i+1))
            table_outside_working_hours.append(item)
        table_REPORT_FOR_EMAIL = "outside_working_hours!1:1000"
        all_info_from_table_OUTSIDE_HOURS = read_sheets(table_REPORT_FOR_EMAIL, id_sheets)
        new_data = [i for i in table_outside_working_hours if i not in all_info_from_table_OUTSIDE_HOURS]
        #print(all_info_from_table_OUTSIDE_HOURS)
        where_to_write = "outside_working_hours!1:1000"
        data_write = write_final_result(new_data, where_to_write, id_sheets)




if __name__ == "__main__":
    auto_script()