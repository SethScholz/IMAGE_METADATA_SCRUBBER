# METADATA_SCRUBBER

## Introduction
Welcome! If you're viewing this repository, it's because you either landed here on accident OR because you know that metadata 
in images has been used to identify individuals, such as through GPS coordinates, the date the picture was taken, information 
specific to the device the image was taken on, etc., and you want to completely scrub any trace of identifiable information 
from the image metadata.

## Repository Contents
- Contains an executable (METADATA_SCRUBBER.exe) to run the program.
- Includes the Python Source File (METADATA_SCRUBBER.py) so all may view the program's code, ensure it is safe, and make edits
as desired.

## What's Needed/What to Expect
If your goal is simply to remove personally identifiable metadata from images, you will only need the METADATA_SCRUBBER.exe file. 
Once you run this file, it will open your file explorer so that you can select the image whose data you wish to scrub. Once you
have selected your file and clicked 'Open', the program will automatically scrub EXIF data, ICC profiles, XMP metadata, and IPTC
metadata, depending on the image format and software used. The program will mostly focus on removing EXIF data, which includes, 
but it not limited to: the camera model, timestamp, GPS coordinates, etc.  

If, however, you wish to improve upon the design on this program (it is rather basic), I have included the Python Source File
METADATA_SCRUBBER.py for your **personal use only.**

## Warning
This program is intended to remove metadata embedded within the image file itself—EXIF, ICC, XMP, and IPTC formats, where 
applicable. However, no tool can guarantee complete anonymity if the original file was uploaded or shared in environments where
additional metadata (such as file system data, timestamps, or cloud service watermarks) might have been attached externally.

Additionally, this program does not modify or erase file names, operating system-level metadata, or forensic watermarks 
sometimes inserted by proprietary software or surveillance tools. If you're under surveillance, distributing or using original
image files (even scrubbed ones) can still carry risks. It is strongly advised to convert images to completely new formats
after sanitizing them and avoid reusing images captured by known devices.

## Notes on Image formats
- JPEG/JPG: Full EXIF metadata removal supported. ICC profiles also stripped.
- PNG: Typically doesn't contain EXIF, but may include ancillary chunks like tEXt, zTXt, 
and iTXt—some of which are removed via Pillow automatically.
- TIFF, BMP, GIF: These are supported to the extent that Pillow can handle metadata.
- RAW formats (e.g., CR2, NEF): Not supported. These formats embed metadata differently and require specialized libraries.

## Licensing
This project is released under a non-commercial open use license: you may copy, share, modify, and redistribute it as 
long as you do not charge money for its use or distribution. This program is provided as-is, with no warranties. 
Use it **at your own risk.**