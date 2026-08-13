import os
import cv2
import glob
import shutil
import traceback

class Generator:
  def __init__(self):
    pass

  def generate(self, images_dir, masks_dir, output_images_dir, output_masks_dir):
     image_files =sorted(glob.glob(images_dir + "/*.png"))  
     mask_files = sorted(glob.glob(masks_dir + "/*.png"))
     n = len(image_files)
     print("image_files", n,)
     num = len(mask_files)
     print("Number of mask_files", num)
     n = 0
     input("SSS")
     for i in range(num): 
       image_file = image_files[i]
       mask_file = mask_files[i]
       mask = cv2.imread(mask_file)
       gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
       
       if gray.any() > 0:
         basename = os.path.basename(mask_file)
         #image_file = os.path.join(images_dir, basename)
         shutil.copy2(mask_file, output_masks_dir)
         shutil.copy2(image_file, output_images_dir)
         n += 1
         print("Copied", n)
         
       else:
         print("Skipped")

if __name__ == "__main__":
  try:
    images_dir = "./mini_test/images"
    masks_dir  = "./mini_test/masks"
    output_dir = "./Brain-Hemorrhage-CT"
    if os.path.exists(output_dir):
      shutil.rmtree(output_dir)
    output_images_dir = os.path.join(output_dir, "images")
    output_masks_dir = os.path.join(output_dir, "masks")
    os.makedirs(output_images_dir)
    os.makedirs(output_masks_dir)
    generator = Generator()
    generator.generate(images_dir, masks_dir, output_images_dir, output_masks_dir)
  except:
    traceback.print_exc()


                   
      

