pipeline {
	
	agent any

	stage('Test') {
		steps {
			sh python -m unittest api_test
		}

		post {
			failure {
				mail to: 'team@example.com',
				subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
				body: "Something is wrong with ${env.BUILD_URL}"
			}
		}
	}
}