from utils import runCmd


def getProcessRunning():
    runCmd("ps aux --sort -rss |head")

