import subprocess


def runCmd(cmd):
    args = cmd.split(" ")
    result = subprocess.run(args, stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))

