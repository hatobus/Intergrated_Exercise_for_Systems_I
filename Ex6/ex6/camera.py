import webiopi
import os

SAVEDIR = '/home/pi/ex6'

@webiopi.macro
def camera(fileno):
    save_no = int(fileno)
    path = SAVEDIR + '/camera_' + str(save_no) + '.jpg'

    command = 'fswebcam -r 320x240 -d /dev/video0 ' + path
    os.system(command)

    os.system('sync')
