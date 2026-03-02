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

        stage('List Files') {
            steps {
                sh 'ls -lrt'
            }
        }

        stage('Conditional Stage') {
            steps {
                script {
                    if (params.USERNAME != 'Guest') {
                        echo "Hello ${params.USERNAME}, you are not the default Guest!"
                    } else {
                        echo "User identification FAILED ❌"
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
        // always {
        //     echo "This runs every time."
        // }
    }
}