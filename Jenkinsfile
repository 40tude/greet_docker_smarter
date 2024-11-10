pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/40tude/greet_docker_smarter'
            }
        }
        
        stage('Test') {
            steps {
                sh 'docker-compose --env-file ./app/.env up greet_test -d'
            }
        }
    }
}