__author__ = 'dhan'
from PIL import Image
import dicom
import numpy
from PIL import ImageMath

import dicom
from dicom.contrib.pydicom_PIL import show_PIL

fname = "/home/dhan/data/emma/1.3.12.2.1107.5.1.4.54912.30000013032209584548400000055_0/IMG0.dcm"



ds=dicom.read_file(fname)

bits = ds.BitsAllocated
samples = ds.SamplesPerPixel
if bits == 8 and samples == 1:
    mode = "L"
elif bits == 8 and samples == 3:
    mode = "RGB"
elif bits == 16:
    mode = "I;16"  # not sure about this -- PIL source says is 'experimental' and no documentation. Also, should bytes swap depending on endian of file and system??
else:
    raise TypeError("Don't know PIL mode for %d BitsAllocated and %d SamplesPerPixel" % (bits, samples))

print mode

data = ds.PixelData
data  = ds.pixel_array

# rescale
print "Shape: ", data.shape
const = float(data.max())
#print const
data2 = numpy.divide(data, const / 255.0)
#print data3[310]
#print data3.shape
print ds
print data2[350]
im = Image.fromarray(data,"I;16")
im.save("some.tiff")
out = im.point(lambda i: i * (255.0 / const))

im2 = out.convert("L")
import PIL
from PIL import ImageOps
im3 = ImageOps.invert(im2)
im3.save("some2.jpg")
Mrugendrata
