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
                                sh '''ssh instance-5 << BOB
				      export BUILD_NUMBER="${BUILD_NUMBER}"
				      #docker stack deploy --compose-file docker-compose.yaml project2
                                      docker service update --image instance-3:5000/service2:build-${BUILD_NUMBER} --replicas "3" --update-order "start-first" --update-parallelism "1" test_service2
                                      '''
                        }
                }
        }
}
