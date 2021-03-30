pipeline {
	agent  any
	environment {
        CHANGED = sh(returnStdout: true, script: 'git diff origin/$BRANCH_NAME --name-only')
    } 
	stages {
		stage ("lambdas") {
			parallel {	
				stage("rollback")
				{
				
					when {
	                    expression { return env.CHANGED =~ 'lambdas/rollback/';}
					}
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
					when {
	                    changeRequest()
					}
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