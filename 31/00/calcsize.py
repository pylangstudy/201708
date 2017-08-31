import struct
import FORMATS
for f in FORMATS.Types.keys(): print(f, struct.calcsize(f))

