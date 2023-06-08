pipeline {
    agent any

    environment {
        PATH = "${PATH}:${HOME}/.local/bin"
    }

    stages {
        stage('Cloning Apache Airflow repo the repo') {
            steps {
                git branch: 'ApacheAirflowPipelinw', url: 'https://github.com/Zahid07/MLOPS-Project.git'
                // print all the files in the repo and use bat
                bat 'dir'
            }
        }

        // add a stage cloning dvc repo
        stage('Cloning DVC repo') {
            steps {
                // go in directory example/intro-example/dags
                dir('example/intro-example/dags') {
                    // clone the dvc repo
                    git branch: 'DVC', url: 'https://github.com/Zahid07/MLOPS-Project.git'
                    // print all the files in the repo and use bat
                    bat 'dir'
                }

            }
        }
        

        

        

    }
}
