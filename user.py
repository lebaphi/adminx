import grp
from utils import runCmd


def getSystemUser(inputGroup=None):
    groups = grp.getgrall()
    for group in groups:
        for user in group[3]:
            if group[0] == inputGroup:
                print(user)
            elif inputGroup == None:
                print(user)


def getUserTree(user):
    print("Directory list for user: " + user)
    runCmd("tree /home/" + user)
