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
            sys.exit()
        elif opt == "-h":
            getHostInfo()
            sys.exit()
        elif opt == "-i":
            getIPInterface(arg)
            sys.exit()
        elif opt == "-u":
            getSystemUser()
            sys.exit()
        elif opt == "-g":
            getSystemUser(arg)
            sys.exit()
        elif opt == "-t":
            getUserTree(arg)
            sys.exit()
        elif opt == "-l":
            getLastRemoteIp()
            sys.exit()
        elif opt == "-p":
            getProcessRunning()
            sys.exit()
        elif opt == "-s":
            getListSudoCMD()
            sys.exit()
        elif opt == "-d":
            distintFunc()
            sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])
