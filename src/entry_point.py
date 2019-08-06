import cv2
import sys
import numpy
from  matplotlib import pyplot as plt
from image_enhancer import ImageEnhancer

def main():
    image_path = None
    try:
        image_path = sys.argv[1]
    except:
        image_path = input("Enter path to the image : ")
        image_path = image_path.strip()
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    enhancer = ImageEnhancer(image, 16, 0.1)

if __name__ == "__main__":
    main()
