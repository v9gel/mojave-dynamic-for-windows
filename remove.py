import os
import getpass
import shutil

path = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Local\\MojaveDynamic'
os.system(r'schtasks /delete /tn "MojaveDynamic"')
shutil.rmtree(path, ignore_errors=True, onerror=None) 

print('MojaveDynamic was successfully removed!')
input()