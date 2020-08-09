def getUsage():
    msg = "Welcome to the Admino system information script\nPlease follow the instructions to use it\n\n"
    msg += "- admino -h --> provides hostname information\n"
    msg += (
        "- admino -i <interface> --> provides the IP address of provided <interface>\n"
    )
    msg += "- admino -u --> provides the list of user of the system\n"
    msg += (
        "- admino -g <groupname> --> provides the list of users for an specifg <user>\n"
    )
    msg += (
        "- admino -t <user> --> provides the directory list tree for a system <user>\n"
    )
    msg += "- admino -l --> provides the list of IPs from last remote connections\n"
    msg += (
        "- admino -p --> provides the top 10 processed which are using more % memory\n"
    )
    msg += "- admino -s --> provides the list of SUDO invoked commands from auth.log\n"
    msg += "- admino -d --> distintive function of your choice\n"
    print(msg)
