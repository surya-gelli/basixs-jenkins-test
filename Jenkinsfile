changed = "lambdas"

pipeline {
	agent  any
	stages {
		stage ("lambdas") {
            when {
				anyOf {
					changeRequest url: 'git@github.com:surya-gelli/basixs-jenkins-test.git'
				}
			}
			parallel {	
				stage("rollback")
				{
					steps
					{
						script 
						{
							if (env.BRANCH_NAME == 'master') 
							{
								sh ''' cd lambdas/rollback/ && cat ECSRollbackfunction.py '''
							}
							else 
							{
								sh ''' echo "Hello from development" '''
							}
						}
					}
				}	
				stage("slack")
				{
					steps
					{
						script
						{
							if (env.BRANCH_NAME == 'master') 
							{
								sh ''' cd lambdas/slack && cat lambda_slacknotify.py '''
							}
							else 
							{
								sh ''' echo "Hello from development" '''
							}
						}
					}
				 }
			}
		}
		
	}
}