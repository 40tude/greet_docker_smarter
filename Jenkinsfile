pipeline {
    agent any
    stages {
        stage('Generate .env') {
            steps {
                script {
                    // Créer .env dans le répertoire ./app
                    writeFile file: 'app/.env', text: """
                    PASSWORD=Zoubida_For_Ever
                    #EXAMPLE_VAR2="Avec espaces"
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
                sh 'docker-compose up greet_test -d'
            }
        }

        stage('Archive Reports') {
            steps {
                script {
                    // create .zip
                    sh '''
                        REPORT_DIR="./test_reports"
                        ARCHIVE_NAME="test_reports_$(date +'%Y-%m-%d').zip"

                        if [ -d "$REPORT_DIR" ]; then
                            zip -r "$ARCHIVE_NAME" "$REPORT_DIR"
                        else
                            echo "$REPORT_DIR does not exist."
                            exit 1
                        fi
                    '''
                }
            }
        }

        stage('Send Email') {
            steps {
                script {
                    // send e-mail with archive enclosed
                    sh '''
                        RECIPIENT="philippe.baucour@gmail.com"
                        SUJET="Test report from Jenkins - $(date +'%Y-%m-%d')"
                        CORPS="Hi,\\n\\nFind enclose the test reports.\\n\\nRegards,\\nJenkins"
                        ARCHIVE_NAME="test_reports_$(date +'%Y-%m-%d').zip"

                        # Send e-mail with mailx
                        echo -e "$CORPS" | mailx -s "$SUJET" -a "$ARCHIVE_NAME" "$RECIPIENT"
                    '''
                }
            }
        }
    }
}