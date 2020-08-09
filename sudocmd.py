from utils import runCmd


def getListSudoCMD():
    runCmd(
        "HISTFILE=~/.bash_history set -o history HISTTIMEFORMAT='Date %d %b %T ' history|awk '{$1="
        "}1''{$5='SUDO COMMAND='}5'"
    )

