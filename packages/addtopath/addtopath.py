import os
import sys
from sys import platform
import shutil as shutil


def isLinux():
    if platform == 'linux' or platform == 'linux2':
        return True
    return False

def getHomeDir():
    return os.path.expanduser('~')

def backupShellConfig():
    bashrcBkup = mHomedir + '/.bashrc.orig'
    if os.path.exists(bashrcBkup):
        return
    shutil.copyfile(mBashrc,bashrcBkup)

# Get home dir and bashrc path
mHomedir = getHomeDir()
mBashrc = mHomedir + '/.bashrc'


def main():

    if not isLinux():
        print 'This utility does not support for your current'
        print 'system platform : ' + platform
        print 'Please create issue at '
        print 'https://github.com/ajinathkumbhar/CODE/issues'
        sys.exit(0)

    # take backup of current bashrc file
    backupShellConfig()

if __name__ == '__main__':
    main()

