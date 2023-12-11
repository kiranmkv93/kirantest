pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
        ECR_REPOSITORY = 'https://8823679081.dkr.ecr.us-east-1.amazonaws.com/iris-classification'
	AWS_ACCOUNT_ID = '8823679081'
        SAGEMAKER_ENDPOINT_NAME = 'iris-classification-endpoint'
    }

    stages {
        stage('Checkout') {
            steps {
                git clone https://github.com/kiranmkv93/kirantest.git
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    sh 'aws ecr create-repository --repository-name $ECR_REPOSITORY'
                    sh 'aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$ECR_REPOSITORY'
                    sh 'docker build -t $ECR_REPOSITORY .'
                    sh 'docker tag $ECR_REPOSITORY:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$ECR_REPOSITORY:latest'
                    sh 'docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$ECR_REPOSITORY:latest'
                }
            }
        }

        stage('Deploy to SageMaker') {
            steps {
                script {
                    def model = 's3://deploy-model-kiran-test-us-east-1/model.tar.gz'
                    def script = 'deploy_script.py'

                    withAWS(region: AWS_DEFAULT_REGION, credentials: 'aws-credentials-id') {
                        sh "python $script $model $SAGEMAKER_ENDPOINT_NAME"
                    }
                }
            }
        }
    }
}

