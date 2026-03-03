pipeline {
    agent any
    
    parameters {
        string(name: 'USERNAME', defaultValue: 'Guest', description: 'Enter your name')
        choice(name: 'BRANCH_SELECT', choices: ['main', 'jenkinsfolder', 'develop'], description: 'Select branch')
    }
    
    stages {
        stage('Print Message') {
            steps {
                echo "Hello, ${params.USERNAME}!"
                echo "Selected branch: ${params.BRANCH_SELECT}"
            }
        }
        
        stage('Conditional Commands') {
            when {
                // Only run this stage if 'jenkinsfolder' branch is selected
                expression { params.BRANCH_SELECT == 'jenkinsfolder' }
            }
            steps {
                echo "Running commands because 'jenkinsfolder' branch is selected..."
                sh '''
                        ls -lrt
                         pwd
                         '''
                    
                }
            }
        
        
        stage('Parallel Tasks') {
            when {
                // Only run parallel stage if 'jenkinsfolder' branch is selected
                expression { params.BRANCH_SELECT == 'jenkinsfolder' }
            }
            parallel {
                stage('Task A') {
                    steps {
                        echo "Running Task A"
                        sh 'echo "Task A completed"'
                    }
                }
                stage('Task B') {
                    steps {
                        echo "Running Task B"
                        sh 'echo "Task B completed"'
                    }
                }
            }
        }
    
    post {
        always {
            echo "Pipeline finished!"
        }
    }
}