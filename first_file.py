import argparse
import getpass
import sys
import boto3
sys.path.append('/opt/VRTScloudpoint/lib')
sys.path.append('/tmp/cloudpoint/libs/azure/lib')
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource.resources import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.resource import SubscriptionClient
from azure.mgmt.resource.locks import ManagementLockClient
from azure.mgmt.resource.locks.models import ManagementLockObject
from azure.mgmt.compute.models import HardwareProfile, StorageProfile
from azure.mgmt.compute.models import NetworkProfile
from azure.mgmt.compute.models import OSDisk, ManagedDiskParameters
from azure.mgmt.compute.models import DiskCreateOption, CreationData
from azure.mgmt.compute.models import Snapshot, VirtualMachine
from azure.mgmt.network.models import PublicIPAddress, NetworkInterface
from azure.mgmt.network.models import NetworkSecurityGroup
from azure.mgmt.network.models import NetworkInterfaceIPConfiguration
from msrestazure.azure_exceptions import CloudError

from azure.identity import ClientSecretCredential, DefaultAzureCredential


parser = argparse.ArgumentParser(description='Generic Cloud Service Script')
parser.add_argument('--cloud', choices=['aws', 'azure', 'gcp', 'azurestack'], help='Specify the cloud service (aws, azure, gcp, azurestack)')
parser.add_argument("--use-credentials", action="store_true", help="Use credentials")
parser.add_argument("--debug", action="store_true", help="Enable debug")
parser.add_argument("--log-location",  metavar='', type=str, help="Debug log location")
parser.add_argument('--list-vms', action='store_true', help='List all available VMs')
parser.add_argument('--list-snap', action='store_true', help='List all snapshots ')
parser.add_argument('--list-disks', action='store_true', help='List all disks')
parser.add_argument('--list-rg', action='store_true', help='List all resources group ')
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


if __name__ == "__main__":
    if args.cloud == 'azure':
        if args.use_credentials:
            AZ_CLIENT_ID = input("Enter AppID (Client ID) for Azure: ")
            AZ_TENANT_ID = input("Enter Tenant ID for Azure: ")
            AZ_SECRET_ID = getpass.getpass("Enter Client Secret for Azure: ")
        
            azure_credentials = check_azure_credentials(AZ_CLIENT_ID, AZ_TENANT_ID, AZ_SECRET_ID)
            if azure_credentials:
                print("success with cred")
                if args.debug:
                    print("enable debug")
                    if args.log_location:
                        print("Use log location")
                    else:
                        print("default log location")
                if args.list_vms:
                    print("list azure vm")
                if args.list_disks:
                    print("list azure disk")
                if args.list_snap:
                    print("List azure snap") 
                if args.list_rg:
                    print("List azure rg")
        else:
            print("without cred")
            if args.debug:
                print("enable debug")
                if args.log_location:
                    print("Use log location")
                else:
                    print("default log location")
            if args.list_vms:
                print("list azure vm")
            if args.list_disks:
                print("list azure disk")
            if args.list_snap:
                print("List azure snap")
            if args.list_rg:
                print("List azure rg")

    elif args.cloud == 'aws':
        if args.use_credentials:
            AWS_ACCESS_KEY = input("Enter Access Key for AWS: ")
            AWS_SECRET_KEY = getpass.getpass("Enter Secret Key for AWS: ")
            print("AWS cred")
            if args.debug:
                print("enable debug")
                if args.log_location:
                    print("Use log location")
                else:
                    print("default log location")
            if args.list_vms:
                print("list aws vm")
            if args.list_disks:
                print("list aws disk")
            if args.list_snap:
                print("List aws snap")
            if args.list_rg:
                print("List aws rg")
        else:
            print("Without cred")
            if args.debug:
                print("enable debug")
                if args.log_location:
                    print("Use log location")
                else:
                    print("default log location")
            if args.list_vms:
                print("list aws vm")
            if args.list_disks:
                print("list aws disk")
            if args.list_snap:
                print("List aws snap")
            if args.list_rg:
                print("List aws rg")
    elif args.cloud == 'gcp':
        if args.use_credentials:
            GCP_SERVICE_ACCOUNT_KEY_PATH = input("Enter the path to your GCP service account key file: ")
            print("GCP with cred")
            if args.debug:
                print("enable debug")
                if args.log_location:
                    print("Use log location")
                else:
                    print("default log location")
            if args.list_vms:
                print("list gcp vm")
            if args.list_disks:
                print("list gcp disk")
            if args.list_snap:
                print("List gcp snap")
            if args.list_rg:
                print("List gcp rg")
        else:
            print("GCP Without cred")
            if args.debug:
                print("enable debug")
                if args.log_location:
                    print("Use log location")
                else:
                    print("default log location")
            if args.list_vms:
                print("list gcp vm")
            if args.list_disks:
                print("list gcp disk")
            if args.list_snap:
                print("List gcp snap")
            if args.list_rg:
                print("List gcp rg")

        