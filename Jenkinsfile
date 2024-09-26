pipeline {
    agent any

    tools {
        nodejs 'NodeJS' // Make sure to have NodeJS installed in Jenkins
    }

    environment {
        SONAR_PROJECT_KEY = 'badsaarow_sonarqube'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/badsaarow/sonarqube.git']]])
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'npm install'
            }
        }

        stage('Run tests') {
            steps {
                sh 'npm test'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQubeServer') {
                    sh """
                        sonar-scanner \
                        -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=https://sonarqube.momoiot.co.kr \
                        -Dsonar.exclusions=node_modules/**,test/**
                    """
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}