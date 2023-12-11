from sagemaker.tensorflow import TensorFlowModel
from sagemaker import get_execution_role
import sagemaker

sagemaker_session = sagemaker.Session()
role = get_execution_role()

# Push the Docker image to ECR
account = sagemaker_session.account_id()
region = sagemaker_session.boto_region_name
image_uri = f"{account}.dkr.ecr.{region}.amazonaws.com/iris-classification:latest"

# Set up TensorFlowModel
iris_model = TensorFlowModel(
    model_data=image_uri,
    role=role,
    framework_version="2.6.0",
    sagemaker_session=sagemaker_session,
)

# Deploy the model
predictor = iris_model.deploy(instance_type="ml.m5.large", endpoint_name="iris-classification-endpoint")
