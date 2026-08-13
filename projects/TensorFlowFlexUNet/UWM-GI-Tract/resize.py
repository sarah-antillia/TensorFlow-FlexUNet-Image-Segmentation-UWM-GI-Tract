

import glob
import os
import cv2
import shutil
import traceback

def crop(image):
    h, w = image.shape[:2]
    if w > h:
        y1 = 0
        y2 = h
        x1 = (w - h)//2
        x2 = x1 + h
        image = image[y1:y2,x1:x2]
        return image
    else:
      input("Error")

def resize(images_dir, name, output_dir):
    index = 10000
    image_files = sorted(glob.glob(images_dir + "/*.jpg"))
    for image_file in image_files:
        index +=1
        image = cv2.imread(image_file)
        basename = os.path.basename(image_file)
        #image = crop(image)
        image = cv2.resize(image, (512,512))
        filename = name + "_" +  str(index) + ".png"
        #filename = basename.replace(".jpg", ".png")
        output_file  = os.path.join(output_dir, filename)
        cv2.imwrite(output_file, image)
        print("Saved", output_file)

if __name__ == "__main__":
  try:
    output_dir = "./png_images"
    if os.path.exists(output_dir):
       shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    images_dir = "./mini_test/xxximages"
    resize(images_dir, "Brain_Hemorrhage", output_dir)

 

  except:
     traceback.print_exc()
