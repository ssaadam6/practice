pipeline {
    agent any

    parameters {
        string(name: "username", defaultValue: "", description: "Verify yourself")
    }

    stages {
        stage('node1') {
            steps {
                echo "User is ${params.username}"
                sh 'ls -lrt'
            }
        }
    }
}