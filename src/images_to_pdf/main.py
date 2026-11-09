from PIL import Image
from datetime import datetime
import os
from pathlib import Path

suitable_image_extensions = ('.jpeg', '.jpg', '.png', '.gif', '.webp')

def save_pdf(out_path, images):
    try:
        images[0].save(out_path, 'PDF', resolution=100.0, save_all=True, append_images=images[1:])
    except IndexError:
        print("Error:\nNo files to convert.")

def make_out_path():
    # date_time = str(datetime.now()).replace(':', '_').replace(' ', '_')[:-7]
    date_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_name = f"{date_time}.pdf"
    return out_name

def make_list_of_images(path: Path):
    try:
        images = []
        for file in path.iterdir():
            if file.name.endswith(suitable_image_extensions):
                image = Image.open(path / file)
                images.append(image)
    except Exception as ex:
        print("Error: ", ex, '\n', "Unexpectable format or smth idk", sep='')
    return images
        
def main(path: Path = Path.cwd(), out_path = ""):
    images = make_list_of_images(path)
    out_path = out_path if out_path else make_out_path()
    save_pdf(out_path, images)

if __name__ == "__main__":
    main()
