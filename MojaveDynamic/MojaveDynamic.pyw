import os
import time
import datetime
import random
import getpass

def set_wallpaper(path):
    import ctypes
    cs = ctypes.c_buffer(path.encode())
    SPI_SETDESKWALLPAPER = 0x14
    return ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, cs, 0)

def read_conf():
	import json
	path = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Local\\MojaveDynamic'
	f = open(path + '\\conf.json')
	json_string = ''
	for l in f:
		json_string += l.rstrip()
	return json.loads(json_string)

def work(conf):
	cur_hour = datetime.datetime.now().hour
	path = 'C:\\Users\\' + getpass.getuser() + '\\AppData\\Local\\MojaveDynamic'
	
	for e in conf:
		if e['start'] <= cur_hour < e['finish']:
			set_wallpaper(path +'\\'+ random.choice(e['image']))

if __name__ == "__main__":
	conf = read_conf()
	work(conf)
