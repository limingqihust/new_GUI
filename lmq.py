import gui
import subprocess
import json
import time
from PyQt5.QtWidgets import QApplication
root = "/home/lmq/MergeCDC"

from PyQt5.QtCore import QThread
class Worker(QThread):
    def __init__(self, master_ip, master_user, master_passwd, cmd):
        super().__init__()
        self.master_ip = master_ip
        self.master_user = master_user
        self.master_passwd = master_passwd
        self.cmd = cmd
    def run(self):
        ret = exec(self.master_ip, self.master_user, self.master_passwd, self.cmd)
        print(ret)
            

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
    # while True:
    #     Ui_Form.exp2_text = Ui_Form.exp2_text + "hello world\n"
    #     print(f"modify exp2_text: {Ui_Form.exp2_text}")
    #     Ui_Form.textEdit_8.setText(Ui_Form.exp2_text)
    #     QApplication.processEvents()
    #     time.sleep(1)
    # return
    root = "/root/exp2/MergeCDC"
    filename = Ui_Form.lineEdit_29.text()
    master_ip = Ui_Form.lineEdit_30.text()
    username = Ui_Form.lineEdit_32.text()
    passwd = Ui_Form.lineEdit_31.text()
    filename = "/home/lmq/new_GUI/config/lmq/exp2.json"
    master_ip = "8.152.160.205"
    username = "root"
    passwd = "hycB509!"
    with open(filename) as file:
        conf = json.load(file)
        distribution = conf["file_distribution"]
        combination = conf["node_combination"]
    # copy config file to master node
    scp(master_ip, username, passwd, filename, f"{root}/config/")
    scp(master_ip, username, passwd, distribution, f"{root}/Distribution/")
    scp(master_ip, username, passwd, combination, f"{root}/Distribution/")
    Ui_Form.textEdit_8.append("[INFO] copy config file to master node done")
    QApplication.processEvents()
    print("[INFO] copy config file to master node done")
    # clear old bandwidth config
    ret = exec(master_ip, username, passwd, f"bash {root}/script/clear.sh")
    Ui_Form.textEdit_8.append("[INFO] clear old bandwidth config done")
    QApplication.processEvents()
    print("[INFO] clear old bandwidth config done")
    # modify bandwidth config
    ret = exec(master_ip, username, passwd, f"bash {root}/script/update.sh")
    Ui_Form.textEdit_8.append("[INFO] modify bandwidth config done")
    QApplication.processEvents()
    print("[INFO] modify bandwidth config done")

    # run TeraSort and CodedTeraSort
    Ui_Form.textEdit_8.append("[INFO] run TeraSort and CodedTeraSort start")
    QApplication.processEvents()
    print("[INFO] run TeraSort and CodedTeraSort start")

    thd = Worker(master_ip, username, passwd, f"bash {root}/script/run_1_terasort.sh")
    thd.start()
    print("[INFO] wait for TeraSort done")
    thd.wait()
    # ret = exec(master_ip, username, passwd, f"bash {root}/script/run_8.sh")
    # Ui_Form.textEdit_8.append("[INFO] run TeraSort and CodedTeraSort done")
    # QApplication.processEvents()
    # print("[INFO] run TeraSort and CodedTeraSort done")
    # Ui_Form.textEdit_8.append("[INFO] result:")
    # Ui_Form.textEdit_8.append(ret[1])
    # QApplication.processEvents()

def run_lmq_exp3(Ui_Form):
    filename = Ui_Form.lineEdit_33.text()
    master_ip = Ui_Form.lineEdit_34.text()
    username = Ui_Form.lineEdit_35.text()
    passwd = Ui_Form.lineEdit_36.text()

    