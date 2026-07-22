#!/usr/bin/env python3

import sys
import zipfile

with zipfile.ZipFile(sys.argv[1], "r") as zf:
    for info in sorted(zf.infolist(), key=lambda x: x.filename):
        data = zf.read(info)
        print("File:", info.filename)
        try:
            print(data.decode("UTF-8"))
        except UnicodeDecodeError:
            print("Binary file, CRC: {:x}".format(info.CRC))
        print()
