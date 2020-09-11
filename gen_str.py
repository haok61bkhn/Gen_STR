import cv2
import glob
import random
import tqdm
fonts=glob.glob("font/*")

from trdg.generators import (
    GeneratorFromDict,
    GeneratorFromRandom,
    GeneratorFromStrings,
    GeneratorFromWikipedia,
)
string = open("str/final.txt","r+").read().split("\n")
random.shuffle(string)
# The generators use the same arguments as the CLI, only as parameters
generator = GeneratorFromStrings(
    string,
    blur=1,
    count=30,
    random_blur=True,
    background_type=3,
    random_skew=False,
    space_width=1,
    size=45,
    character_spacing=1,
    fit=True,
    alignment=3,
    margins=(5, 5, 5, 5),
    #text_color="#a07081",
    fonts=fonts,
    image_dir="./background",
)
d=0

for img, lbl in tqdm.tqdm(generator):
  img.save("data/"+str(d)+".jpg")
  f=open("data/"+str(d)+".txt","w+")
  f.write(lbl)
  f.close()
  d+=1 
