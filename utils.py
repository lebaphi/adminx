import subprocess


def runCmd(cmd):
    args = cmd.split(" ")
    result = subprocess.run(
        args, stdout=subprocess.PIPE, shell=True, universal_newlines=True, check=True
    )
    print(result.stdout.decode("utf-8"))

