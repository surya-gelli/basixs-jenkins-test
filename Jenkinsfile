pipeline {
	agent  any
	environment{
		CHANGED = sh(returnStdout: true, script: "git diff-tree origin/$BRANCH_NAME --stat=999 $DIR_PATH") 
	}
	stages {
		stage ("lambdas") {
			parallel {	
				stage("rollback")
				{    
					when {
						expression {return env.CHANGED != ""}
						//changeset 'lambdas/rollback/**'
                           //changeRequest branch: 'master', comparator: 'GLOB', url: "https://github.com/surya-gelli/basixs-jenkins-test/tree/master/lambdas/rollback"
					}
					steps
					{
						script 
						{
							sh ''' echo env.CHANGED '''
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