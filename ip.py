import socketclear
from utils import runCmd


def getIPInterface(interface):
    print("Your ip for " + interface + " interface is:")
    print(socket.gethostbyname(interface))


def getLastRemoteIp():
    runCmd("pinky")
