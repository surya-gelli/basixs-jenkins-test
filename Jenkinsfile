pipeline {
	agent  any
	stages {
		stage("rollback")
		{
			when { changeRequest target: "lambdas/rollback/**" }
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
			when { changeRequest target: "lambdas/slack/**" }
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
