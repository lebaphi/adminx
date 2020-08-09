import subprocess


def runCmd(arg1, arg2=None):
    args = [arg1]
    if arg2 != None:
        args = [arg1, arg2]
    print(args)
    result = subprocess.run(args, stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))

