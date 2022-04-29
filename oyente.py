# 使用
# python3 oyente.py [文件路径]

import hashlib
import sys

with open(sys.argv[1], "r") as rf:
    filename = rf.name
    bytecode = rf.readline()
    hash = hashlib.md5(bytecode.encode(encoding='UTF-8')).hexdigest()
    print("%s#%s" % (filename[-42:], hash))