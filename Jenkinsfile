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
            // Condition: Only run this stage when branch is 'jenkinsfolder'
            when {
                expression { params.BRANCH_SELECT == 'jenkinsfolder' }
            }
            steps {
                echo "Running commands because 'jenkinsfolder' branch is selected..."
                // Execute shell commands: show current directory then list files
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
                // Sub-stage A
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
        
    } 
    
    
    post {
        always {
            
            echo "Pipeline finished!"
        }
    }
    
} 