import os
import getpass
import shutil

path = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Local\\MojaveDynamic'
os.system(r'schtasks /create /tn "MojaveDynamic" /tr ' + path + r'/MojaveDynamic.pyw /sc minute  /mo 10')
shutil.copytree('MojaveDynamic', path) 
os.system('python ' + path + '\\MojaveDynamic.pyw')

#We also need to decide
print('MojaveDynamic was successfully installed!')
input()