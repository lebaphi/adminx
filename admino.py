import sys, getopt
from usage import getUsage
from host import getHostInfo
from ip import getIPInterface, getLastRemoteIp
from user import getSystemUser, getUserTree
from processes import getProcessRunning
from sudo import getListSudoCMD
from distint import distintFunc


def main(argv):
    try:
        opts, _ = getopt.getopt(argv, "hi:ug:t:lpsd", ["help"])
    except getopt.GetoptError as err:
        print(err)
        getUsage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == "--help":
            getUsage()
        elif opt == "-h":
            getHostInfo()
        elif opt == "-i":
            getIPInterface(arg)
        elif opt == "-u":
            getSystemUser()
        elif opt == "-g":
            getSystemUser(arg)
        elif opt == "-t":
            getUserTree(arg)
        elif opt == "-l":
            getLastRemoteIp()
        elif opt == "-p":
            getProcessRunning()
        elif opt == "-s":
            getListSudoCMD()
        elif opt == "-d":
            distintFunc()
    sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
