import subprocess
import os


filename = "/home/lmq/new_GUI/config/lmq/exp2.json"
master_ip = "8.152.160.205"
username = "root"
passwd = "hycB509!"
cmd = "bash /root/exp2/MergeCDC/script/helloworld.sh"
print(f" exec {cmd} start")
exec_cmd = f"sshpass -p {passwd} ssh {username}@{master_ip} \"{cmd}\"" 
os.system(exec_cmd)
print(f" exec {exec_cmd} end")


cmd = "cat /root/exp2/MergeCDC/result.out"
exec_cmd = f"sshpass -p {passwd} ssh {username}@{master_ip} \"{cmd}\"" 
ret = subprocess.getstatusoutput(exec_cmd)
print(ret)