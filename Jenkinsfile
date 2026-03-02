pipeline {
    agent any

    parameters {
        string(name: 'USERNAME', defaultValue: 'Guest', description: 'Enter your name')
    }

    options {
        timeout(time: 5, unit: 'MINUTES') // Pipeline will stop after 5 minutes
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
            when {
                expression { params.USERNAME != 'Guest' }
            }
            steps {
                echo "Hello ${params.USERNAME}, Kindly verify yourself!"
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
        aborted {
            echo "Build was ABORTED ⏹️"
        }
        // always {
        //     echo "This runs every time."
        // }
    }
}