from utils import runCmd


def getHostInfo():
    runCmd("hostnamectl")

