from utils import runCmd
import psutil


def getListOfProcessSortedByMemory():
    """
    Get list of running process sorted by Memory Usagepython
    """
    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
        try:
            # Fetch process details as dict
            pInfo = proc.as_dict(attrs=["pid", "name", "username"])
            pInfo["rss"] = proc.memory_info().rss / (1024 * 1024)
            # Append dict to list
            listOfProcObjects.append(pInfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(
        listOfProcObjects, key=lambda procObj: procObj["rss"], reverse=True
    )
    return listOfProcObjects


def getProcessRunning():
    print("pid", " | ", "user", " | ", "pName", " | ", "rss")
    listOfRunningProcess = getListOfProcessSortedByMemory()
    for p in listOfRunningProcess[:10]:
        print(p["pid"], " | ", p["username"], " | ", p["name"], " | ", p["rss"])

