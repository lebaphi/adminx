from utils import runCmd

def getListSudoCMD():
    runCmd("bash -i -c  'history -r;history' ")

