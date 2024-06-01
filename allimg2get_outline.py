import glob

import get_outline


img_list = glob.glob('image_name/*', recursive=False)

for img_path in img_list:
    get_outline.get_outline(img_path)