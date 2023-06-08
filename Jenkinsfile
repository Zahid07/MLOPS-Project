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
                    

                    // go in dvc folder and print all the files
                    dir('dvc') {
                        
                        // run command dvc pull
                        bat 'dvc pull'
                        dir ('data') {
                            bat 'dir'
                        }
                    }
                }

                dir('examples/intro-example/dags') {
                    // clone the dvc repo
                    git branch: 'DVC', url: 'https://github.com/Zahid07/MLOPS-Project.git'
                    // print all the files in the repo and use bat
                    

                    // go in dvc folder and print all the files
                    dir('dvc') {
                        
                        // run command dvc pull
                        bat 'dvc pull'
                        dir ('data') {
                            bat 'dir'
                        }
                    }
                }

            }
        }

        // add a stage to run the airflow
        stage('Running Airflow') {
            steps {
                // print all the files in the repo and use bat
                bat 'docker-compose up -d'
            }
        }
        

        

        

    }
}
