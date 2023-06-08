import os

def pushToGit():
    # check if MLFlow-Project exists
    if os.path.exists("MLOPS-Project"):
        # remove the MLFlow-Project folder
        os.system("rm -rf MLOPS-Project")

    # clone the repo again
    os.system("git clone -b mlFlow --single-branch https://github.com/Zahid07/MLOPS-Project.git")	
    # add fodler mlruns to git
    os.system("git add mlruns")
    # commit the changes
    os.system("git commit -m \"Added mlruns folder\"")
    # push the changes to the remote repo
    os.system("git push origin mlFlow")
    print("Pushed mlruns folder to remote repo successfully.")


    
