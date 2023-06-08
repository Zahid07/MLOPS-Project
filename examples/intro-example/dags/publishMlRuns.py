import os

def pushToGit():
    # print the folders in current directory
    print(os.listdir())
    # push folder mlruns to github branch mlFlow from the current directory
    os.system("git add mlruns")
    os.system("git commit -m 'mlruns added'")
    os.system("git push origin mlFlow")
    print("mlruns pushed to github successfully.")
    
    
