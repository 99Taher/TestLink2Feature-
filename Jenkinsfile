pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull code from GitHub or other repository
                git branch: 'main', url: 'https://github.com/99taher/TestLink2Feature-'
            }
        }

       
        stage('Run Tests') {
            steps {
                
                // OR run each file separately
                bat 'python3 creation.py'
                // sh 'python3 creationsuitetest.py'
                // sh 'python3 creation_base_de_doner.py'
                // sh 'python3 recupertiontest.py'
            }
        }
    }
}
