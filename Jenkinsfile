pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent any
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
    }
}