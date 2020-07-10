pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {label 'python', docker 'python:3.7.2'}
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
    }
}