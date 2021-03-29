changed = "lambdas"

pipeline {
	agent  any
	stages {
		stage ("lambdas") {
			parallel {
				stage("rollback")
				{
					when { 
						anyOf {
						    changeset 'lambdas/rollback/**' 
						}
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
						anyOf {
						    changeset 'lambdas/slack/**' 
							changeRequest url: 'https://github.com/surya-gelli/basixs-jenkins-test/tree/master/lambdas/rollback'

						}
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