from utils import runCmd


def getIPInterface(interface):
    print("Your ip for " + interface + " interface is:")
    runCmd("ifconfig " + interface + " |sed -n 2p | awk {'print " + interface + "'}")


def getLastRemoteIp():
    print("(Con. #)  (IP Addr)")
    runCmd(
        "last|grep -i 'still logged in' |awk '{print $4}'| last|grep -i 'pts' |awk '{print $3}'|sort|uniq -c"
    )
