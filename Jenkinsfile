pipeline {
	agent  any
	stages {
		stage ("lambdas") {
			parallel {
				stage("rollback")
				{
					when { changeset "lambdas/rollback/**" }
					steps
					{
						script 
						{
							if (env.BRANCH_NAME == 'master') 
							{
								sh """ echo "Hello world" """
							}
							else 
							{
								sh """ echo "Hello from development" """
							}
						}
					}
				}	
				stage("slack")
				{
					when { changeset "lambdas/slack/**" }
					steps
					{
						script
						{
							if (env.BRANCH_NAME == 'master') 
							{
								sh """ echo "Hello world" """
							}
							else 
							{
								sh """ echo "Hello from development" """
							}
						}
					}
				}
			}
		}
		
	}
}