import csv
import os
import shutil


def classification():
    root_dir = "../../data/XXXX_code/"
    CWE = root_dir + "CWE/"
    if not os.path.exists(CWE):
        os.makedirs(CWE)

    with open("src/flawfinder-result.csv", "r", encoding="utf-8") as result_list:
        reader = csv.reader(result_list)
        for item in reader:
            if reader.line_num == 1:
                continue
            cwes = str(item[9])
            if cwes.find("!/") != -1:
                cwes = cwes.replace("!/", "#")
                if not os.path.exists(CWE + cwes):
                    os.makedirs(CWE + cwes)
                name = str(item[0])
                shutil.copy(root_dir + name, CWE + cwes)
            elif cwes.find(",") != -1:
                for cwes_name in cwes.split(","):
                    cwes_name = cwes_name.strip()
                    if not os.path.exists(CWE + cwes_name):
                        os.makedirs(CWE + cwes_name)
                    name = str(item[0])
                    shutil.copy(root_dir + name, CWE + cwes_name)
            else:
                if not os.path.exists(CWE + cwes):
                    os.makedirs(CWE + cwes)
                name = str(item[0])
                shutil.copy(root_dir + name, CWE + cwes)


if __name__ == '__main__':
    classification()
