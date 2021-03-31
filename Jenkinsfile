pipeline {
	agent  any
	//environment{
    	//TARGET = "${changeRequest() ? CHANGE_TARGET:BRANCH_NAME}"
		//CHANGED = sh(returnStdout: true, script: "git diff-tree origin $CURRENTBRANCH $GIT_PREVIOUS_COMMIT...$GIT_COMMIT $DIR_PATH") 
		//CHANGED_DEV = sh(returnStdout: true, script: "git diff-tree origin development $GIT_PREVIOUS_COMMIT...$GIT_COMMIT $DIR_PATH")
	//}
	stages {
		stage ("lambdas") {
			parallel 
		    {
				stage("rollback")
				{    
					when {
						anyOf{

						    //expression {return env.CHANGED = "lambdas/rollback/"}
						    //expression {return env.CHANGED = "lambdas/rollback/"}
						//} //changeset 'lambdas/rollback/**'
                            changeRequest branch: 'master'
						    changeRequest branch: 'development'
						}
					}	
					steps
					{
						script 
						{
							if ( env.BRANCH_NAME == 'master') 
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
						    //changeset 'lambdas/slack/**' 
							changeRequest url: 'https://github.com/surya-gelli/basixs-jenkins-test/tree/$BRANCH_NAME/lambdas/rollback'

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
