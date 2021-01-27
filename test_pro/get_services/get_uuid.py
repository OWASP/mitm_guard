import subprocess
aaa = subprocess.Popen(['dmidecode','-s','system-uuid'], stdout=subprocess.PIPE)
output, err = aaa.communicate()
aaa = str(output).split("'")[1].split("\\")[0]
