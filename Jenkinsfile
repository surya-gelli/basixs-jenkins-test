pipeline {
	agent  any
	//environment{
    	//TARGET = "${changeRequest() url:'https://github.com/surya-gelli/basixs-jenkins-test/tree/$BRANCH_NAME/lambdas/rollback/'}"
		//CHANGED = sh(returnStdout: true, script: "git diff origin/master --name-only") 
		//CHANGED_DEV = sh(returnStdout: true, script: "git diff-tree origin/$BRANCH_NAME --stat=999 //$GIT_PREVIOUS_COMMIT...$GIT_COMMIT lambdas/rollback")
		//CHANGED = sh(returnStdout: true, script: 'git diff-tree origin/$BRANCH_NAME --stat=999 lambdas/rollback | awk "{print $1}"'
	//}
	stages {
		stage ("lambdas") {
			parallel 
		    {
				stage("rollback")
				{    
					when {
						anyOf {
						    expression {sh(returnStatus: true, script: './changes.sh') == 0}
						    changeset 'lambdas/rollback/**'
                            //changeRequest branch: 'master' 
						    //changeRequest branch: 'development
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
						    expression {sh(returnStatus: true, script: './changes.sh') == 0}
						    changeset 'lambdas/slack/**'
                            //changeRequest branch: 'master' 
						    //changeRequest branch: 'development
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
