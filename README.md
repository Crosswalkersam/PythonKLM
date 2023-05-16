# PythonKLM
A minimalistic decoder to extract AVHRR images from NOAA KLM frames.
This decoder takes in NOAA-KLM encoded frames and turns them into .png images.

## Disclaimer
This project should be considered a "guide" for those that want to get into the world of satellite decoding.
Its by no means efficient or fast (it's Python, duh), but instead intended to be easily readable.
Thats why its commented so much.

## Usage
Before you run this, you need to install Pillow and tqdm by running 'Pip install tqdm Pillow' in your console.
Then just point line 12 and 14 to your frame-file and run the script. Created images will be saved in the script directory.
This path may be changed by adjusting lines 34-38.
