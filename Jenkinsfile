pipeline {
    agent any

    environment {
        PATH = "${PATH}:${HOME}/.local/bin"
    }

    stages {
        stage('Cloning the repo') {
            steps {
                git branch: 'DV ApacheAirflowPipelinw', url: 'https://github.com/Zahid07/MLOPS-Project.git'
                // print all the files in the repo and use bat
                bat 'dir'
            }
        }

        

    }
}
