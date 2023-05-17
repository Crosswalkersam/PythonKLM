#Disclaimer: This decoder is ONLY for NOAA KLM formatted satellites.
#NOAA is not CCSDS compliant and uses a custom frame-format.
#This frame-format is very easy to decode, since every frame contains everything.
#General structure will be: Read in frames - Extract data - convert data into .png or whatever.
#This is the light-variant of my HRPT decoder which only does AVHRR images.
#If you need the full version that does AIP/TIP frame extraction, scan mirror position and Space calibration data aswell, let me know.

from PIL import Image
from tqdm import tqdm
import os

file = open("noaa_hrpt_19.raw16", 'rb')

filesize = os.stat("noaa_hrpt_19.raw16").st_size
framecount = int(filesize / 22180)  #one frame is 22180 Bytes. Calculate the number of frames in this file.

buffer = [0 for a in range(11090)]  #Create a full-sized, empty buffer. This is easier than appending to a zero-entry buffer.
AVHRR1 = Image.new("I", (2048, framecount))     #Create images to write our pixels to
AVHRR2 = Image.new("I", (2048, framecount))     #width is always 2048, height is the number of frames (each frame contains a single scanline)
AVHRR3 = Image.new("I", (2048, framecount))
AVHRR4 = Image.new("I", (2048, framecount))
AVHRR5 = Image.new("I", (2048, framecount))

for i in tqdm(range(framecount)):       #do this for every frame
    for j in range(11090):        #read in one frame
        buffer2 = file.read(2)      #Yay, custom formats. Two bytes are one word, which is little endian encoded. Usually One word is 10Bit, but .raw16 is repacked as 16, which makes stuff a lot easier.
        buffer[j] = buffer2[1] << 8 | buffer2[0]     #Save little endian encoded 16-Bit files in our buffer.
    for k in range(2048):
        AVHRR1.putpixel((k, i), 20 * buffer[750 + 5 * k])   #x20 because otherwise the images will be insanely dark.
        AVHRR2.putpixel((k, i), 20 * buffer[751 + 5 * k])   #One can get around this by choosing a more suitable image mode than 32Bits in Pillow
        AVHRR3.putpixel((k, i), 20 * buffer[752 + 5 * k])   #But I didnt bother. Maybe someone has the patience to fix this.
        AVHRR4.putpixel((k, i), 20 * buffer[753 + 5 * k])   #This works. And since calibration isnt implemented either way, it doesnt really matter.
        AVHRR5.putpixel((k, i), 20 * buffer[754 + 5 * k])
AVHRR1.save("AVHRR-1.png")  #Write our images to dir
AVHRR2.save("AVHRR-2.png")
AVHRR3.save("AVHRR-3.png")
AVHRR4.save("AVHRR-4.png")
AVHRR5.save("AVHRR-5.png")
