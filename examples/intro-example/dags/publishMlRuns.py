import os

def pushToGit():
    # check if MLFlow-Project exists
    if os.path.exists("MLOPS-Project"):
        # remove the MLFlow-Project folder
        os.system("rm -rf MLOPS-Project")

    # add username and email to git
    os.system("git config --global user.email 'zahidmuhammad127@gmail.com'")
    os.system("git config --global user.name 'Zahid07'")
    

    # clone the repo again
    os.system("git clone -b mlFlow --single-branch https://github.com/Zahid07/MLOPS-Project.git")	
    # copy and replace the mlruns folder into the MLFlow-Project folder
    os.system("cp -r mlruns MLOPS-Project")
    # change the directory to MLFlow-Project
    os.chdir("MLOPS-Project")
    # add the files
    os.system("git add .")
    # commit the changes
    os.system('git commit -m "Added mlruns"')
    # push the changes
    os.system("git push origin mlFlow")
    print("Pushed to git successfully.")




    
