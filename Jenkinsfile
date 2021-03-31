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


def changeLogSets = currentBuild.changeSets
for (int i = 0; i < changeLogSets.size(); i++) {
    def entries = changeLogSets[i].items
    for (int j = 0; j < entries.length; j++) {
        def entry = entries[j]
        echo "${entry.commitId} by ${entry.author} on ${new Date(entry.timestamp)}: ${entry.msg}"
        def files = new ArrayList(entry.affectedFiles)
        for (int k = 0; k < files.size(); k++) {
            def file = files[k]
            echo "  ${file.editType.name} ${file.path}"
        }
    }
}