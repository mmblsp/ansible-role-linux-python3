node {
    stage('Get Latest Code') {
        checkout scm
    }

    try {
        stage('Python') {
            script {
                    sh '''#!/bin/bash
                    # Create/Activate virtualenv
                    python3 -m venv .venv39
                    source ~/workspace/.venv/bin/activate
                    cd ssh_user
                    pip install -r requirements.txt'''
                }
        }
        stage('molecule lint') {
            script {
                    sh '''#!/bin/bash
                    source ~/workspace/.venv/bin/activate
                    cd ssh_user
                    molecule lint'''
                }
        }
        stage('molecule test') {
                script {
                    sh '''#!/bin/bash
                    source ~/workspace/.venv/bin/activate
                    cd ssh_user
                    molecule test'''
                }
        }
    }
    catch (all) {
        currentBuild.result = 'FAILURE'
        throw err
    }
}
