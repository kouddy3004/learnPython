import subprocess, re

ipConfig_result = subprocess.check_output(["ipconfig","/all"])
ipaddress = re.search(r"IPv4 Address. . . . . . . . . . . : \w\w\w.\w\w\w.\w\w.\w\w", str(ipConfig_result))
print(ipaddress[0])
macaddress = re.search(r"Physical Address. . . . . . . . . : \w\w-\w\w-\w\w-\w\w-\w\w-\w\w", str(ipConfig_result))
print(macaddress[0])