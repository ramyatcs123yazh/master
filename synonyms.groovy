def config
pipeline {
    agent any
    options {
        timestamps() // print timestamps in the console output
    }
    parameters {

        choice(name: 'ENV_TAG', choices: ['dev', 'qa', 'prod','corpdev','corpqa','corpprod'], description: 'environment')
    }
    stages {
        stage('LW indexing job') {
         
            steps {
                script {
                    sh 'python "${WORKSPACE}/jenkins/index/test.py"'
                }
            }
        }

    }
    post {
         failure {
            sendStatusEmail(params.FAILURE_EMAIL, 'FAILED')
        }
        aborted {
            sendStatusEmail(params.FAILURE_EMAIL, 'ABORTED')
        }
        always {
            cleanWs()
        }
    }
}
