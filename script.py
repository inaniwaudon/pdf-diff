import argparse
import os
import tempfile
from pdf2image import convert_from_path
from PIL import Image, ImageChops

def pdf_to_images(pdf_path: str, output_dir: str):    
    images = convert_from_path(pdf_path)
    image_paths: list[str] = []
    for i, image in enumerate(images):
        image_path = os.path.join(output_dir, f"{i + 1}.png")
        image_paths.append(image_path)
        image.save(image_path)
    return image_paths

def compare_images(image0_path, image1_path, diff_dir):
    image0 = Image.open(image0_path)
    image1 = Image.open(image1_path)
    diff = ImageChops.difference(image0, image1)

    filename = os.path.basename(image0_path)
    diff_path = os.path.join(diff_dir, filename)

    if diff.getbbox():
        diff.save(diff_path)
        print(f"{filename}: Difference saved")
    else:
        print(f"{filename}: No differences found")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf0")
    parser.add_argument("pdf1")
    parser.add_argument("diff_dir")
    args = parser.parse_args()

    if not os.path.exists(args.diff_dir):
        os.makedirs(args.diff_dir)

    with (
        tempfile.TemporaryDirectory() as dname0, 
        tempfile.TemporaryDirectory() as dname1
    ):
        pdf0_images = pdf_to_images(args.pdf0, dname0)
        pdf1_images = pdf_to_images(args.pdf1, dname1)
    
        for img0, img1 in zip(pdf0_images, pdf1_images):
            compare_images(img0, img1, args.diff_dir)
