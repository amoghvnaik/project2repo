pipeline{
        agent any
        
        stages{
		stage('--building--'){
			steps{
				sh '''. ~/.bashrc
				      docker-compose build
				      docker-compose push
				      '''
			}
		}
                stage('--deployment--'){
                        steps{
                                sh '''ssh deployment << BOB
				      export BUILD_NUMBER="${BUILD_NUMBER}"
                                      docker service update --image project-jenkins:5000/service2:build-${BUILD_NUMBER} --replicas "3" --update-order "start-first" --update-parallelism "1" project2_service2
                                      '''
                        }
                }
        }
}
