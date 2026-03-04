pipeline {
    agent any
    parameters {
        string(name: 'USERNAME', defaultValue: 'Guest', description: 'Enter your name')
        choice(name: 'BRANCH_SELECT', choices: ['main', 'jenkinsfolder', 'devlop'], description: 'Select branch')
    }
    
    stages {
        stage('checkout'){
            steps{
                // Use the selected parameter for Git branch
                git branch: 'devlop', url: 'https://github.com/ssaadam6/practice.git'
            }
        }

        stage('Print Message') {
            steps {
                echo "Hello, ${params.USERNAME}!"
                echo "Selected branch: ${params.BRANCH_SELECT}"
            }
        } 
        
        stage('Conditional Commands') {
            when {
                expression { params.BRANCH_SELECT == 'jenkinsfolder' }
            }
            steps {
                echo "Running commands because 'jenkinsfolder' branch is selected..."
                sh '''
                    pwd
                    ls -lrt
                '''
            }
        } 
        
        stage('Parallel Tasks') {
            when {
                expression { params.BRANCH_SELECT == 'jenkinsfolder' }
            }
            parallel {
                stage('Task A') {
                    steps {
                        echo "Running Task A"
                        sh 'pwd'
                    }
                }
                stage('Task B') {
                    steps {
                        echo "Running Task B"
                        sh 'ls -lrt'
                    }
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