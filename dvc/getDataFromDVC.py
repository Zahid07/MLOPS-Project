import os
import dvc.api
import git

def download_data():
    data_path = "data"
    # get all files in current folder


    # Get the list of DVC files in the folder
    dvc_files = [
        file
        for file in os.listdir(os.path.join(data_path))
        if file.endswith(".dvc")
    ]

    # run the command dvc pull
    for file in dvc_files:
        os.system(f"dvc pull {os.path.join(data_path, file)}")

# if __name__ == "__main__":
#     download_data()

    # c