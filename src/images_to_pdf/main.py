from PIL import Image, ImageFile
from datetime import datetime
from pathlib import Path

suitable_image_extensions = ('.jpeg', '.jpg', '.png', '.gif', '.webp')

def save_pdf(out_path: str | Path, images: list[ImageFile.ImageFile]):
    # Images with transparency (such as PNGs in RGBA mode)
    # must be converted to RGB first to prevent errors.
    images_RGB: list[ImageFile.ImageFile] = []
    for image in images:
        if image.mode in ("RGBA", "P"):
            images_RGB.append(image.convert("RGB"))
        else:
            images_RGB.append(image)
    try:
        images_RGB[0].save(out_path, 'PDF', dpi=(300,300), save_all=True, append_images=images_RGB[1:])
    except IndexError:
        print("Error:\nNo files to convert.")

def make_out_path():
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
