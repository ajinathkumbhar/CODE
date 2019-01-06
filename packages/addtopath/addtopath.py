import os
import sys
from sys import platform
import shutil as shutil
import getopt

# Get file name
TAG = os.path.basename(__file__)
# version
vMaj = 1
vMin = 0

class Options(object):
    """ Options class to store command line args/options
    """
    def __init__(self):
        self.path = None
        self.cpath = None

# Option object
OPT = Options()

def getVersion():
    ver = str(vMaj) + '.' + str(vMin)
    return ver

def isLinux():
    """ Check supported platform
    """
    if platform == 'linux' or platform == 'linux2':
        return True
    return False

def getHomeDir():
    """ Get cureent user home dir location
    """
    return os.path.expanduser('~')

def backupShellConfig():
    """ Take backup current  bashrc
    """
    bashrcBkup = mHomedir + '/.bashrc.orig'
    if os.path.exists(bashrcBkup):
        return
    shutil.copyfile(mBashrc,bashrcBkup)

# Get home dir and bashrc path
mHomedir = getHomeDir()
mBashrc = mHomedir + '/.bashrc'


def usage():
    """ print usage
    """
    print ' '
    print TAG + ' ' + '<options>'
    print 'options:'
    print '\t-v, --version\t print version'
    print '\t-h, --help\t print help'
    print '\t--cpath\t\t print current PATH value'
    print '\t--path\t\t add path to PATH variable'
    print ' '

def parseArgs(argv):
    """ Parse argument from commandline
    """
    long_opts = ['help', 'version', 'cpath', 'path' ]
    short_opts = 'hv'

    try :
        opts_list, args_pos = getopt.getopt(argv[1:], short_opts, long_opts)
    except getopt.GetoptError:
        return False

    try :
        print argv[1]
    except IndexError:
        return False

    if args_pos:
        print args_pos
        return False

    for opt, val in opts_list:
        if opt == '--cpath':
            OPT.cpath = val
        elif opt == '--path':
            OPT.path = val
        elif opt in [ '-h', '--help']:
            usage()
            sys.exit(0)
        elif opt in ['-v','--version']:
            print 'v'+ getVersion()
        else:
            print 'error: wrong option : ' + opt
            return False

    return True


def main():

    if not isLinux():
        print 'This utility does not support for your current'
        print 'system platform : ' + platform
        print 'Please create issue at '
        print 'https://github.com/ajinathkumbhar/CODE/issues'
        sys.exit(0)

    if not parseArgs(sys.argv):
        print 'error: failed to parse args'
        usage()
        sys.exit(0)

    # take backup of current bashrc file
    backupShellConfig()

if __name__ == '__main__':
    main()

