import gui
import subprocess
import json

root = "/home/lmq/MergeCDC"

def scp(master_ip, master_user, master_passwd, file, dst):
    if master_user == "root":
        scp_cmd = "sshpass -p " + master_passwd + " scp " + file + " " + master_user + "@" + master_ip + ":" + dst
    else:
        scp_cmd = "sshpass -p " + master_passwd + " scp " + file + " " + master_user + "@" + master_ip + ":" + dst
    
    # print(scp_cmd)
    return subprocess.getstatusoutput(scp_cmd)

def exec(master_ip, master_user, master_passwd, cmd):
        exec_cmd = f"sshpass -p {master_passwd} ssh {master_user}@{master_ip} \"{cmd}\""
        return subprocess.getstatusoutput(exec_cmd)

def run_lmq_exp1(Ui_Form):
    filename = Ui_Form.lineEdit_25.text()
    master_ip = Ui_Form.lineEdit_26.text()
    username = Ui_Form.lineEdit_27.text()
    passwd = Ui_Form.lineEdit_28.text()
    
def run_lmq_exp2(Ui_Form):
    filename = Ui_Form.lineEdit_29.text()
    master_ip = Ui_Form.lineEdit_30.text()
    username = Ui_Form.lineEdit_32.text()
    passwd = Ui_Form.lineEdit_31.text()

    with open(filename) as file:
        conf = json.load(file)
        distribution = conf["file_distribution"]
        combination = conf["node_combination"]

    scp(master_ip, username, passwd, filename, f"{root}/config/")
    scp(master_ip, username, passwd, distribution, f"{root}/Distribution/")
    scp(master_ip, username, passwd, combination, f"{root}/Distribution/")
    ret = exec(master_ip, username, passwd, f"mpirun -np 32 --oversubscribe {root}/CodedTeraSort")
    Ui_Form.textEdit_8.append(ret[1])

def run_lmq_exp3(Ui_Form):
    filename = Ui_Form.lineEdit_33.text()
    master_ip = Ui_Form.lineEdit_34.text()
    username = Ui_Form.lineEdit_35.text()
    passwd = Ui_Form.lineEdit_36.text()

    