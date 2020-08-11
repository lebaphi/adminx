import subprocess


def getListSudoCMD():
    result = subprocess.run(
        "bash -i -c  'history -r;history' ", stdout=subprocess.PIPE, shell=True, universal_newlines=True, check=True
    )
    print(result.stdout)

