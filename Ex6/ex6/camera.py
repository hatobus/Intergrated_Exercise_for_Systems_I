import webiopi
import os
import datetime

SAVEDIR = '/home/pi/ex6'

@webiopi.macro
def camera(fileno):
    save_no = int(fileno)
    path = SAVEDIR + '/camera_' + str(save_no) + '.jpg'

    command = 'fswebcam -r 320x240 -d /dev/video0 ' + path
    os.system(command)

    os.system('sync')

@webiopi.macro
def camera_time(fileno): 
    save_no = int(fileno)
    path = SAVEDIR + '/camera_' + str(save_no) + '.jpg'

    command = 'fswebcam -r 320x240 -d /dev/video0 ' + path
    os.system(command)

    os.system('sync')

    now = datetime.datetime.now()
    took_time = ""

    for d in [now.year, now.month, now.day]:
        took_time += str(d) + "-"

    took_time = took_time[:-1]
    took_time += " "

    for t in [now.hour, now.minute, now.second]:
        took_time += str(t) + ":"

    took_time = took_time[:-1]
    return took_time
