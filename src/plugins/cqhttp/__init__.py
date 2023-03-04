import os
import platform

os.chdir("./src/plugins/cqhttp/")
if platform.system() == "Windows":
    os.system('start cmd /K "go-cqhttp.exe"')
elif platform.system() == "Linux":
    os.system('./go-cqhttp &')
else:
    print("No cqhttp in package")
os.chdir("../../..")
