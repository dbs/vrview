#!/usr/bin/env python
#
# Google Cardboard Camera extractor
# Extracts audio and second image from the XMP header in Cardboard Camera images
# Requires python-xmp-toolkit ( pip install python-xmp-toolkit )
# License: MIT
#
# Usage:
# $ carboardcam_extract.py myimage_vr.jpg
#
# Creates two new files - myimage_vr_audio.mp4 and myimage_vr_righteye.jpg
 
import sys
from os import path
from base64 import b64decode
from libxmp.utils import file_to_dict
 
img_filename = sys.argv[1]
xmp = file_to_dict(img_filename)
 
#audio_b64 = xmp[u'http://ns.google.com/photos/1.0/audio/'][1][1]
# 
#afh = open(path.splitext(img_filename)[0]+"_audio.mp4", 'wb')
#afh.write(b64decode(audio_b64))
#afh.close()
 
image_b64 = xmp[u'http://ns.google.com/photos/1.0/image/'][1][1]
 
ifh = open(path.splitext(img_filename)[0]+"_righteye.jpg", 'wb')
ifh.write(b64decode(image_b64))
ifh.close
