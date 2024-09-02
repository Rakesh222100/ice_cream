pipeline {
    agent {
        label 'my_new_node'
    }

    environment {
        // Define environment variables here if needed
        IMAGE_NAME = "my-docker-image"
        IMAGE_TAG = "latest"
        CONTAINER_NAME = "my-docker-container"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                script {
                    sh "cd backend && sudo docker compose up --build"
                }
            }
        }

    }
}
