import csv
import git
import os
import shutil
import stat


def clone_project_from_github():
    with open("src/project_list_C.csv", "r", encoding="utf-8") as project_list:
        reader = csv.reader(project_list)
        for item in reader:
            if reader.line_num == 1:
                continue

            user_name = str(item[2])
            project_name = str(item[0])
            project_url = str(item[1])
            root_dir = "../../data/"

            if not os.path.exists(root_dir):
                os.makedirs(root_dir)
            print(project_url)

            if user_name not in os.listdir(root_dir):  ## data 目录下没有当前用户，直接克隆
                print("cloning project ------------->>>>> " + user_name + "/" + project_name)
                repo = git.Repo.clone_from(project_url, root_dir + user_name + "/" + project_name)
                repo.close()

            elif user_name in os.listdir(root_dir):  # data 目录下有当前用户
                if project_name not in os.listdir(root_dir + user_name + "/"):  # 当前用户下没有该项目
                    print("cloning project ------------->>>>> " + user_name + "/" + project_name)
                    repo = git.Repo.clone_from(project_url, root_dir + user_name + "/" + project_name)
                    repo.close()
                else:  # 当前用户下有该项目
                    git_list = os.listdir(root_dir + user_name + "/" + project_name)
                    if len(git_list) == 1 and git_list[0] == ".git":  # 当前项目只clone 一部分
                        for root, dirs, files in os.walk(root_dir + user_name + "/" + project_name, topdown=False):
                            for name in files:
                                os.chmod(os.path.join(root, name), stat.S_IWRITE)
                                os.remove(os.path.join(root, name))
                            for name in dirs:
                                os.rmdir(os.path.join(root, name))
                        print("cloning project ------------->>>>> " + user_name + "/" + project_name)
                        repo = git.Repo.clone_from(project_url, root_dir + user_name + "/" + project_name)
                        repo.close()


if __name__ == '__main__':
    clone_project_from_github()
