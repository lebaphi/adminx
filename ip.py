from utils import runCmd


def getIPInterface(interface):
    print("Your ip for " + interface + " interface is:")
    runCmd("ifconfig " + interface + " |sed -n 2p | awk {'print " + interface + "'}")


def getLastRemoteIp():
    print("(Con. #)  (IP Addr)")
    runCmd("pinky")
