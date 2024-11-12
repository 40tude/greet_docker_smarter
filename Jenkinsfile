pipeline { 
    agent any
    stages {
        stage('Generate .env') {
            steps {
                script {
                    // Créer .env dans le répertoire ./app
                    writeFile file: 'app/.env', text: """
                    PASSWORD=Zoubida_For_Ever
                    EXAMPLE_VAR2="Avec espaces"
                    """
                }
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/40tude/greet_docker_smarter'
            }
        }
        
        stage('Test') {
            steps {
                // sh 'docker-compose --env-file ./app/.env up greet_test -d'
                sh 'docker-compose --env-file ./app/.env up greet_test'
            }
        }

        stage('Archive Reports') {
            steps {
                script {
                    // Définir les variables en dehors du bloc sh pour les rendre disponibles dans la section post
                    env.REPORT_DIR = "./test_reports"
                    env.ARCHIVE_NAME = "test_reports_${new Date().format('yyyy-MM-dd-HHmmss')}.zip"
                    
                    // Créer l'archive .zip
                    sh """
                        if [ -d "${env.REPORT_DIR}" ]; then
                            zip -r "${env.ARCHIVE_NAME}" "${env.REPORT_DIR}"
                        else
                            echo "${env.REPORT_DIR} does not exist."
                            exit 1
                        fi
                    """
                }
            }
        }
    }
    post {
        success {
            script {
                echo "Success"
                emailext(
                    subject: "Jenkins build success: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """
                    <p>Success</p>
                    <p>${env.JOB_NAME} #${env.BUILD_NUMBER}</p>
                    """,
                    to: 'philippe.baucour@gmail.com',
                    attachmentsPattern: "${env.ARCHIVE_NAME}"
                )
            }
        }
        failure {
            script {
                echo "Failure"
                emailext(
                    subject: "Jenkins build failure: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                    body: """
                    <p>Failure</p>
                    <p>${env.JOB_NAME} #${env.BUILD_NUMBER}</p>
                    """,
                    to: 'philippe.baucour@gmail.com',
                    attachmentsPattern: "${env.ARCHIVE_NAME}"
                )
            }
        }
    }
}