import os


def runCmd(cmd):
    # args = cmd.split(" ")
    # result = subprocess.call(
    #     args, stdout=subprocess.PIPE, shell=True, universal_newlines=True, check=True
    # )
    # print(result.stdout.decode("utf-8"))
    os.system(cmd)

