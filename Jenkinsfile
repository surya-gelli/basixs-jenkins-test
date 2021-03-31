pipeline {
	agent  any
	environment{
    	//TARGET = "${changeRequest() ? url:'https://github.com/surya-gelli/basixs-jenkins-test/tree/$BRANCH_NAME/lambdas/rollback/'}"
		CHANGED = sh(returnStdout: true, script: "git diff-tree origin master --stat=999 lambdas/rollback/") 
		//CHANGED_DEV = sh(returnStdout: true, script: "git diff-tree origin development $GIT_PREVIOUS_COMMIT...$GIT_COMMIT $DIR_PATH")
		//CHANGED = sh(returnStdout: true, script: 'git diff-tree origin/$BRANCH_NAME --stat=999 lambdas/rollback | awk "{print $1}"'
	}
	stages {
		stage ("lambdas") {
			parallel 
		    {
				stage("rollback")
				{    
					when {
						anyOf {
						    expression {return env.CHANGED = ""}
						    expression {return env.CHANGED != ""}
						//} //changeset 'lambdas/rollback/**'
                            //changeRequest branch: 'master'
						    //changeRequest branch: 'development'
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
