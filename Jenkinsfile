changed = "lambdas"

pipeline {
	agent  any
	stages {
		stage ("lambdas") {
			parallel {	
				stage("rollback")
				{
					when {
	                    expression { file("lambdas/rollback/**")}
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
	                    expression { file("lambdas/slack/**")}
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