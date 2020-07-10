pipeline {
  agent any
  stages {
    stage('build') {
      steps {

          bat 'virtualenv venv --distribute'
          bat '. venv/bin/activate'
          bat 'pip install -r requirements.txt'
          echo "Ho gya bhai run"
      }
    }
  }
}