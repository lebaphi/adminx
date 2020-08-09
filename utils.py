import subprocess


def runCmd(*args):
    result = subprocess.run(args, stdout=subprocess.PIPE)
    print(result.stdout.decode("utf-8"))

