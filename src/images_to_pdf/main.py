from PIL import Image
from datetime import datetime
import os
from pathlib import Path

directory_path = Path(__file__).parent
suitable_image_extensions = ('.jpeg', '.jpg', '.png', '.gif', '.webp')

try:
    images = [Image.open(directory_path / file)
            for file in os.listdir(directory_path) if file.endswith(suitable_image_extensions)]
except Exception as ex:
    print("Error: ", ex, '\n', "Unexpectable format or smth idk", sep='')
    os.system('pause')
    exit()
date_time = str(datetime.now()).replace(':', '_').replace(' ', '_')[:-7]
pdf_path = directory_path / f"pdfile_{date_time}.pdf"
images[0].save(pdf_path, 'PDF', resolution=100.0, save_all=True, append_images=images[1:])
