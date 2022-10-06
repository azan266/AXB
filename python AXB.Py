#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')

import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf AXB.so brand.so')
except:
    pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('AXB.so'):
        os.system('curl -L https://github.com/azan266/Azan/blob/main/Azan.cpython-310.so?raw=true -o Jutt.so')
        from AXB import reg
        reg()
    else:
        from AXB import reg
        reg()
elif bit == '32bit':
    if not os.path.isfile('AXB.so'):
        os.system('curl -L https://github.com/azan266/AXB/blob/main/Azan.cpython-310.so?raw=true -o brand.so')
        from AXB import reg
        reg()
    else:
        from AXB import reg
        reg()
