from utils import runCmd


def getSystemUser(inputGroup=None):
    if inputGroup == None:
        print("The list of users of your system are:")
        runCmd("awk -F':' '{print $1}' /etc/passwd|awk '$0=-$0'")
    else:
        print("List of users into group " + inputGroup)
        runCmd(
            "getent group "
            + inputGroup
            + "|awk -F: '{print $4}'|tr ',' '\n'|awk '$0= - $0'"
        )


def getUserTree(user):
    print("Directory list for user: " + user)
    runCmd("tree /home/" + user)
