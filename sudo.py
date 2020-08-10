from utils import runCmd


def getListSudoCMD():
    runCmd(
        "HISTTIMEFORMAT=\"Date %d %b %T \" history|awk '{$1=\"\"}1''{$5=\"SUDO COMMAND=\"}5'"
    )

