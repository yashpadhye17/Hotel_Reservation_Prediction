pipeline{
    agent any

    stages{
        stage("Cloning Github Repo To Jenkins"){
            steps{
                script{
                    echo 'Cloning github repo to jenkins....'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/yashpadhye17/Hotel_Reservation_Prediction.git']])
                }
            }
        }
    }
}