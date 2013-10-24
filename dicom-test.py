__author__ = 'dhan'
from PIL import Image
import dicom

import dicom
from dicom.contrib.pydicom_PIL import show_PIL

fname = "/home/dhan/data/emma/1.3.12.2.1107.5.1.4.54912.30000013032209515682800002391_4/IMG15.dcm"



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

# PIL size = (width, height)
size = (ds.Columns, ds.Rows)

im = Image.frombuffer(mode, size, ds.PixelData, "raw", mode, 0, 1)
im.show()

