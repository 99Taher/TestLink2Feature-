pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull code from GitHub or other repository
                git branch: 'main', url: 'https://github.com/99taher/TestLink2Feature-'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh './run_tests.sh'
                // OR run each file separately
                // sh 'python3 creationtestcase.py'
                // sh 'python3 creationsuitetest.py'
                // sh 'python3 creation_base_de_doner.py'
                // sh 'python3 recupertiontest.py'
            }
        }
    }
}
