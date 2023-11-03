import pyperclip
import os
import configparser
import boto3
import click
import platform
import psutil

os.environ['NO_PROXY'] = '*.amazonaws.com.cn,169.254.169.254'


def get_identity(region, profile=None):
    session = boto3.Session(profile_name=profile, region_name=region)
    sts_client = session.client('sts')
    response = sts_client.get_caller_identity()
    return response


def get_parent_process_name():
    current_process = psutil.Process()
    parent_process = current_process.parent().parent()
    return parent_process.name()


def copy_env_command_to_clipboard(profile):
    system = platform.system()
    if system == "Windows":
        process_name = get_parent_process_name()
        if process_name == "cmd.exe":
            cmd = f"set AWS_PROFILE={profile}"
        elif process_name == "powershell.exe":
            cmd = f"$Env:AWS_PROFILE='{profile}'"
        else:
            cmd = "not powershell or cmd, pls check your platform and process"
    elif system in ["Linux", "Darwin"]:  # Darwin是MacOS的系统名称
        cmd = f"export AWS_PROFILE={profile}"
    else:
        cmd = "# Unsupported OS"
    return cmd


def list_aws_profiles():
    credentials_path = os.path.expanduser("~/.aws/credentials")
    config = configparser.ConfigParser()
    config.read(credentials_path)
    return config.sections()


def get_region_from_profile(profile):
    config_path = os.path.expanduser("~/.aws/config")
    config = configparser.ConfigParser()
    config.read(config_path)
    return config.get(f"profile {profile}", "region", fallback=None)


def switch_aws_profile_interactive():
    profiles = list_aws_profiles()
    for index, profile in enumerate(profiles, start=1):
        print(f"{index}. {profile}")

    choice = int(input("Select the AWS profile number to switch to: "))
    if choice < 1 or choice > len(profiles):
        print("Invalid choice!")
        return None, None

    chosen_profile = profiles[choice - 1]
    region_for_chosen_profile = get_region_from_profile(chosen_profile)

    return chosen_profile, region_for_chosen_profile


@click.command()
@click.option('--profile', is_flag=True, default=False, help='Prompt for AWS CLI profile or use the one provided')
@click.option('--region', default='cn-north-1',
              help='AWS region. Defaults to cn-north-1 if not provided and not found in profile config.')
@click.argument('profilename', required=False)
def role_token(profile, region, profilename):
    if profile:
        if profilename:
            chosen_profile = profilename
            region_from_profile = get_region_from_profile(profilename)
            if region_from_profile:
                region = region_from_profile
        else:
            chosen_profile, region_from_profile = switch_aws_profile_interactive()
            if region_from_profile:
                region = region_from_profile
    else:
        chosen_profile = None

    try:
        identity = get_identity(region, chosen_profile)
    except Exception as e:
        identity = get_identity("us-east-1", chosen_profile)

    if profile:
        print(f"Switched to: {identity['Arn']}")
        print("The following command has been copied to the clipboard, please paste it to set environment variables")
        cmd = copy_env_command_to_clipboard(chosen_profile)
        
        try:
            pyperclip.copy(cmd)
        except:
            print("If you're a Linux user, you lack dependencies on the clipboard or graphics. Please copy and paste the following command manually:")
        finally:
            print(cmd)

    else:

        session = boto3.Session(profile_name=chosen_profile, region_name=region)
        credentials = session.get_credentials()
        print(f"User ID: {identity['UserId']}")
        print(f"ARN: {identity['Arn']}")
        print(f"Access Key: {credentials.access_key}")
        print(f"Secret Key: {credentials.secret_key}")


# if __name__ == "__main__":
#     role_token()
