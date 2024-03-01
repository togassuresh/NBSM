import argparse
import getpass
from azure.identity import ClientSecretCredential, DefaultAzureCredential
from azure.mgmt.subscription import SubscriptionClient
import boto3
from google.auth import default

parser = argparse.ArgumentParser(description='Generic Cloud Service Script')
parser.add_argument('--cloud', choices=['aws', 'azure', 'gcp'], help='Specify the cloud service (aws, azure, gcp)')
parser.add_argument("--use-credentials", action="store_true", help="Use credentials")
parser.add_argument('--list-vms', action='store_true', help='List all available VMs')
parser.add_argument('--list-disks', action='store_true', help='List all disks')
args = parser.parse_args()

def check_azure_credentials(client_id, tenant_id, secret_id):
    try:
        cloud = "AZURE_PUBLIC_CLOUD"  # Specify the Azure public cloud environment
        credentials = ClientSecretCredential(tenant_id=tenant_id, client_id=client_id, client_secret=secret_id, cloud_environment=cloud)
        # Placeholder for additional Azure credential validation logic if needed
        return credentials
    except Exception as e:
        print(f"Error validating Azure credentials: {str(e)}")
        return None

def check_aws_credentials(access_key, secret_key):
    try:
        session = boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key)
        sts_client = session.client('sts')
        sts_client.get_caller_identity()
        return session
    except Exception as e:
        print(f"Error validating AWS credentials: {str(e)}")
        return None

def check_gcp_credentials(service_account_key_path):
    try:
        credentials, project_id = default(scopes=["https://www.googleapis.com/auth/cloud-platform"], quota_project_id=None)
        return credentials
    except Exception as e:
        print(f"Error fetching GCP credentials: {str(e)}")
        return None

# Prompt the user for authentication details based on the selected cloud service
if args.cloud:
    if args.cloud == 'azure':
        if args.use_credentials:
            AZ_CLIENT_ID = input("Enter AppID (Client ID) for Azure: ")
            AZ_TENANT_ID = input("Enter Tenant ID for Azure: ")
            AZ_SECRET_ID = getpass.getpass("Enter Client Secret for Azure: ")
        
            azure_credentials = check_azure_credentials(AZ_CLIENT_ID, AZ_TENANT_ID, AZ_SECRET_ID)
            if azure_credentials:
                cloud = "AZURE_PUBLIC_CLOUD"
                credential_scopes = ["{} {}{}".format(
                        "openid profile offline_access",
                        cloud.endpoints.active_directory_resource_id, "/.default")]
            
                cloud_base_url = cloud.endpoints.resource_manager
                sc = SubscriptionClient(
                    azure_credentials, base_url=cloud_base_url,
                    credential_scopes=credential_scopes)
                print("Azure credentials are valid.")
                # Return the Azure credentials object to the calling function or use it as needed
                if args.list_vms:
                    list_vms("Azure")
                if args.list_disks:
                    list_disks("Azure")
            else:
                print("Invalid Azure credentials. Please check your client ID, tenant ID, and client secret.")
        else:
            azure_credentials = get_default_azure_credential()
            if azure_credentials:
                cloud = "AZURE_PUBLIC_CLOUD"
                credential_scopes = ["{} {}{}".format(
                        "openid profile offline_access",
                        cloud.endpoints.active_directory_resource_id, "/.default")]
            
                cloud_base_url = cloud.endpoints.resource_manager
                sc = SubscriptionClient(
                    azure_credentials, base_url=cloud_base_url,
                    credential_scopes=credential_scopes)
                print("Azure credentials are valid.")
                # Return the Azure credentials object to the calling function or use it as needed
                if args.list_vms:
                    list_vms("Azure")
                if args.list_disks:
                    list_disks("Azure")
            else:
                print("Invalid Azure credentials. Please check your client ID, tenant ID, and client secret.")
    
    elif args.cloud == 'aws':
        if args.use_credentials:
            AWS_ACCESS_KEY = input("Enter Access Key for AWS: ")
            AWS_SECRET_KEY = getpass.getpass("Enter Secret Key for AWS: ")

            aws_session = check_aws_credentials(AWS_ACCESS_KEY, AWS_SECRET_KEY)

            if aws_session:
                ec2 = boto3.client('ec2')
                response = ec2.describe_instances()
                for reservation in response['Reservations']:
                    for instance in reservation['Instances']:
                        print(instance['InstanceId'])
            else:
                print("Invalid AWS credentials. Please check your access key and secret key.")
        
        else:
            aws_session = get_default_aws_credential()

            if aws_session:
                print("Using default AWS credentials.")
                # Proceed with AWS actions using the default session
                ec2 = boto3.client('ec2')
                response = ec2.describe_instances()
                for reservation in response['Reservations']:
                    for instance in reservation['Instances']:
                        print(instance['InstanceId'])

    elif args.cloud == 'gcp':
        if args.use_credentials:
            GCP_SERVICE_ACCOUNT_KEY_PATH = input("Enter the path to your GCP service account key file: ")

            gcp_credentials = check_gcp_credentials(GCP_SERVICE_ACCOUNT_KEY_PATH)

            if gcp_credentials:
                client = resource_manager.Client()
                for project in client.list_projects():
                    print(project.project_id)
            else:
                print("Invalid GCP credentials. Please check your configuration.")
        
        else:
            gcp_credentials = check_gcp_credentials(None)

            if gcp_credentials:
                client = resource_manager.Client()
                for project in client.list_projects():
                    print(project.project_id)
            else:
                print("Invalid GCP credentials. Please check your configuration.")