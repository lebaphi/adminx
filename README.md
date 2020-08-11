# adminx - usage

- install pip: sudo apt install python3-pip
- install psutil: pip3 install psutil -> use to get process information
- insatall grp: pip3 install grp -> use to get user information in the system

# run

- navigate to the root folder: cd adminx
- run by this command: python3 admino.py --help

- get host information by running command `runCmd("hostnamectl")` in the termianl
- get interface ip by running command `socket.gethostbyname(interface)`
- get last remote ip by runing command: `runCmd("pinky")`
- get top 10 process mem by using `psutil` package, get all process rss `proc.memory_info().rss` then filter top 10
- get sudo command by running this command: `runCmd("bash -i -c  'history -r;history' ")`
- get all system user by using `grp` packages, get all group of user by `grp.getgrall()`
- get tree of directory user by running this command: `runCmd("tree /home/{user}")`
