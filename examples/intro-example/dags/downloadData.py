import os
# import git 



def cloneRepo():
    print("Cloning the repo...")
    # if MLOPS-Project exists then delete it
    if os.path.exists("MLOPS-Project"):
        os.system("rm -rf MLOPS-Project")
    os.system("git clone -b DVC --single-branch https://github.com/Zahid07/MLOPS-Project.git")
    os.system("ls MLOPS-Project")
    print("Repo cloned successfully.")