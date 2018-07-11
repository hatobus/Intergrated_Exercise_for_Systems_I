import time
import subprocess
import sys
import os


class takePic():
    def __init__(self, savedir="./tookpic", fname="uploadpic.jpg"):
        self.name = fname
        self.savedir = savedir

    def takePic(self):
        path = os.path.abspath(self.savedir)
        filepath = os.path.join(path, self.name)
        print(filepath)

        cmd = "fswebcam -d /dev/video0 -r 640x480 {}".format(filepath)

        subprocess.call(cmd.strip().split(" "))

        print("Save collectly "+filepath)


if __name__ == '__main__':
    PIC = takePic()
    PIC.takePic()
