pipeline {
	agent  any
	environment {
		CHANGED = sh(returnStdout: true , script: 'git diff --name-only $GIT_PREVIOUS_COMMIT $GIT_COMMIT')
    	//TARGET = "${changeRequest() ? branch: 'master'}"
		//COMMIT =  sh(returnStdout: true , script:'./changes.sh')
		//CHANGED_DEV = sh(returnStdout: true, script: "git diff-tree origin/$BRANCH_NAME --stat=999 //$GIT_PREVIOUS_COMMIT...$GIT_COMMIT lambdas/rollback")
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
							//changeset 'lambdas/rollback/**'
						    //expression {sh(returnStdout:true, script: './changes.sh')==0 } 
                            //changeRequest ( url: 'https://github.com/surya-gelli/basixs-jenkins-test/tree/$BRANCH_NAME/lambdas/rollback/', branch: 'master' )
						    //changeRequest branch: 'development
							expression {return env.CHANGED =~ "lambdas/rollback/" }
						}		
					}	
					steps
					{
						script {
							if ( env.BRANCH_NAME == 'master') 
							{
								sh ''' cd lambdas/modify-configuration-actions/ cat app.html '''
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
						    expression {return env.CHANGED =~ "lambdas/slack" }   
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