pipeline {
    agent any

    tools {
        nodejs 'NodeJS'
    }

    environment {
        SONAR_PROJECT_KEY = 'yyj_sonarqube'
        PATH = "${tool 'NodeJS'}/bin:${tool 'SonarScanner'}/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/yyeojeong/sonarqube.git']]])
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'cd nodejs && npm install'
            }
        }

        stage('Run tests') {
            steps {
                sh 'cd nodejs && npm test'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQubeServer') {
                    sh """
                        sonar-scanner \
                        -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                        -Dsonar.sources=./nodejs \
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
