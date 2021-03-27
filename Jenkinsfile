changed = "lambdas"

pipeline {
	agent  any
	stages {
		stage ("lambdas") {
			parallel {
				stage("rollback")
				{
				   when { changeRequest { changeset 'lambda/rollback/**'} }
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
					when { expression {return changed.contains ==~ 'slack/*' } }
				    //when { changeset comparator: 'EQUALS', pattern: 'lambdas/slack/**'}
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