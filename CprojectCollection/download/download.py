import csv
import git
import os

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

            if user_name not in os.listdir(root_dir):
                print("cloning project ------------->>>>> " + user_name + "/" + project_name)
                repo = git.Repo.clone_from(project_url, root_dir + user_name)
                repo.close()

            elif user_name in os.listdir(root_dir):
                if project_name not in os.listdir(root_dir + user_name):
                    print("cloning project ------------->>>>> " + user_name + "/" + project_name)
                    repo = git.Repo.clone_from(project_url, root_dir + user_name)
                    repo.close()


if __name__ == '__main__':
    clone_project_from_github()
