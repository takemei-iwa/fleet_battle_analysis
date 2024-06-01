import glob

import get_ship_mask as sm


img_list = glob.glob('mask/*', recursive=False)

for img_path in img_list:
    sm.get_ship_mask(img_path)
    sm.get_ship_point(img_path)
    sm.get_white_mark_point(img_path,"wh_template.jpg")