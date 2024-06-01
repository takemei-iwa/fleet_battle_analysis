import json
import os
import glob

ship_point_path = "ship_point/000.json"
white_mark_point_path = "white_mark_point/000.json"

ship_point_dir = "ship_point"
white_mark_point_dir = "white_mark_point"
output_path = "whole_data.json"

def get_ship_data(ship_point_path, white_mark_point_path):
    with open(ship_point_path, 'r', encoding='utf-8') as json_file:
        ships = json.load(json_file)

    with open(white_mark_point_path, 'r', encoding='utf-8') as json_file:
        whmarks = json.load(json_file)    

    print(ships)
    print(whmarks)

    data=[]
    for ship in ships:
        cont = False
        print("a")
        for whmark in whmarks:
            print(f"{whmark['x']}, {whmark['y']} {ship['x']}, {ship['y']}")
            if whmark['x'] == ship['x'] and \
                whmark['y'] == ship['y']:
                cont = True
                break
        if cont :
            continue
        print("b")        
        data.append([ship['x'], ship['y']])

    return data

def get_all_ship_data(ship_point_dir, white_mark_point_dir):
    ship_point_files = glob.glob(os.path.join(ship_point_dir,'*'), recursive=False)
    white_mark_point_files = glob.glob(os.path.join(white_mark_point_dir,'*'), recursive=False)

    whole_data=[]
    for sh_file, wm_file in zip(ship_point_files, white_mark_point_files):
        whole_data.append(get_ship_data(sh_file, wm_file))        
    return whole_data

whole_data = get_all_ship_data(ship_point_dir, white_mark_point_dir)
with open(output_path, 'w',encoding='utf-8') as json_file:
        json.dump(whole_data, json_file, indent=4,ensure_ascii=False)