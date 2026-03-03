pipeline {
    agent any
    
    parameters {
        string(name: 'USERNAME', defaultValue: 'Guest', description: 'Enter your name')
    }
    
    stages {
        stage('Print Message') {
            steps {
                echo "Hello, ${params.USERNAME}!"
            }
        }
        
        }
        
        stage('Privileged Operations') {
            when {
                allOf {
                    expression { params.USERNAME != null }
                    expression { params.USERNAME.trim() != '' }
                    expression { params.USERNAME != 'Guest' }
                }
            }
            steps {
                echo "✅ User '${params.USERNAME}' validated - executing privileged commands"
                sh '''
                    echo "=== Privileged Block ==="
                    ls -lrt
                    pwd
                    whoami
                    echo "=== End Privileged Block ==="
                '''
            }
        }
        
        stage('Conditional Stage') {
            steps {
                script {
                    if (params.USERNAME != 'Guest') {
                        echo "Hello ${params.USERNAME}, you are not the default Guest!"
                    } else {
                        echo "User identification FAILED"
                    }
                }
            }
        }
        
        stage('Done') {
            steps {
                echo "Pipeline finished stages."
            }
        }
    }
    
    post {
        success {
            echo "Build was SUCCESSFUL ✅"
        }
        failure {
            echo "Build has FAILED ❌"
        }
        always {
            echo "Pipeline completed for user: ${params.USERNAME}"
        }
    }
}