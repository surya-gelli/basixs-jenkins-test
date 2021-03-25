pipeline{
	agent{
		label "any"
	}
	stages{
		stage("test") {
			when { changeRequest target: "lambdas/**" }
			steps{
				script{
					if (env.BRANCH_NAME = 'master') 
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
